#!/usr/bin/env python

# Dependencies: python-tldextract, pass

import argparse
import enum
import fnmatch
import functools
import os
import re
import shlex
import subprocess
import sys

import tldextract

PASSWORD_STORE_PATH = os.path.expanduser('~/.password-store')
DMENU_INVOCATION = 'dmenu -l'
ENCODING = 'UTF-8'

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('url', nargs='?', default=os.getenv('QUTE_URL'))
argument_parser.add_argument('--password-store', '-p', default=PASSWORD_STORE_PATH)
argument_parser.add_argument('--username-pattern', '-u', default=r'.*/(.+)')
argument_parser.add_argument('--username-target', '-U', choices=['path', 'secret'], default='path')
argument_parser.add_argument('--password-pattern', '-P', default=r'(.*)')
argument_parser.add_argument('--dmenu-invocation', '-d', default='rofi -dmenu')

stderr = functools.partial(print, file=sys.stderr)


class ExitCodes(enum.IntEnum):
    SUCCESS = 0
    COULD_NOT_DETERMINE_URL = 1
    COULD_NOT_DETERMINE_DOMAIN = 2
    NO_PASS_CANDIDATES = 3
    COULD_NOT_MATCH_USERNAME = 4
    COULD_NOT_MATCH_PASSWORD = 5


def qute_command(command):
    with open(os.environ['QUTE_FIFO'], 'w') as fifo:
        fifo.write(f'{command}\n')
        fifo.flush()


def find_pass_candidates(domain, password_store_path=PASSWORD_STORE_PATH):
    candidates = []
    for path, directories, file_names in os.walk(password_store_path):
        if directories or domain not in path.split(os.path.sep):
            continue

        # Strip password store path prefix to get the relative pass path
        pass_path = path[len(password_store_path) + 1:]
        secrets = fnmatch.filter(file_names, '*.gpg')
        candidates.extend(os.path.join(pass_path, os.path.splitext(secret)[0]) for secret in secrets)
    return candidates


def pass_(path):
    process = subprocess.run(['pass', path], stdout=subprocess.PIPE, encoding=ENCODING)
    return process.stdout.strip()


def dmenu(items, invocation=DMENU_INVOCATION):
    command = shlex.split(invocation)
    process = subprocess.run(command, input='\n'.join(items), stdout=subprocess.PIPE, encoding=ENCODING)
    return process.stdout.strip()


def main(arguments):
    # Domain wasn't overriden using CLI argument or found in qutebrowser environment variable
    if not arguments.url:
        stderr('Could not determine URL!')
        return ExitCodes.COULD_NOT_DETERMINE_URL

    domain = tldextract.extract(arguments.url).registered_domain
    if not domain:
        stderr(f'Could not determine domain from URL: {arguments.url!r}!')
        return ExitCodes.COULD_NOT_DETERMINE_DOMAIN

    candidates = find_pass_candidates(domain, arguments.password_store)
    if not candidates:
        stderr(f'No candidates for domain {domain!r} found!')
        return ExitCodes.NO_PASS_CANDIDATES

    selection = candidates[0] if len(candidates) == 1 else dmenu(candidates, arguments.dmenu_invocation)
    secret = pass_(selection)
    data = selection if arguments.username_target == 'path' else secret
    match = re.match(arguments.username_pattern, data)
    if not match:
        stderr(f'Failed to match username pattern on {arguments.username_target}!')
        return ExitCodes.COULD_NOT_MATCH_USERNAME
    username = match.group(1)

    match = re.match(arguments.password_pattern, secret)
    if not match:
        stderr('Failed to match password pattern on secret!')
        return ExitCodes.COULD_NOT_MATCH_PASSWORD

    password = match.group(1)
    # Enter back into insert-mode so the user can immediately continue working
    qute_command(f'fake-key {username} ;; fake-key <Tab> ;; fake-key {password} ;; enter-mode insert')
    return ExitCodes.SUCCESS


if __name__ == '__main__':
    arguments = argument_parser.parse_args()
    sys.exit(main(arguments))
