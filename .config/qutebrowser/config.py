config.load_autoconfig(False)
import subprocess
import os
from qutebrowser.api import interceptor

config.load_autoconfig()

# taken from https://qutebrowser.org/doc/help/configuring.html
def read_xresources(prefix):
    """
    read settings from xresources
    """
    props = {}
    x = subprocess.run(["xrdb", "-query"], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split("\n")
    for line in filter(lambda l: l.startswith(prefix), lines):
        prop, _, value = line.partition(":\t")
        props[prop] = value
    return props


xresources = read_xresources("*")

base =   "~/.local/share/qutebrowser/startpage/index.html"
# search = "https://searx.be/search?q={}"
search = "https://google.com/search?q={}"

c.fonts.default_family = "jetbrains-mono"
c.fonts.default_size = "11pt" 

# Zoom
c.zoom.default = "100%"

# Characters used for hint strings.
# Type: UniqueCharString
c.hints.chars = 'abcdefghijklmnopqrstuvwxy'

# Bind
# config.bind(' q',   'quit')
config.bind(';O',   'set-cmd-text :open !g')
config.bind(';w',   'hint all window')
config.bind(',q',   'open https://qutebrowser.org/doc/help/settings.html')
# config.bind(',gm',  'open https://mail.google.com/mail/u/0/?pli=1#inbox')
config.bind (',gh', 'open https://github.com/silasanderson')
config.bind (',gl', 'open https://gitlab.com/silasanderson')
config.bind (',y',  'open https://www.youtube.com')
config.bind (',d',  'open https://github.com/silasanderson/dotfiles')
#config.unbind('https://google.com/search?q={}<d>', mode='normal')
config.bind('m',    'set-cmd-text -s :quickmark-load')
config.bind('M',    'quickmark-save')
# config.bind('xt', 'config-cycle tabs.show always switching')
# config.bind('xb', 'config-cycle statusbar.show always in-mode')
# config.bind('<Alt-b>', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always never')
config.bind('<Alt-b>', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always never')
config.bind('<Ctrl-r>', 'restart')
# config.bind(';M', 'spawn mpv {url}')
config.bind(';m', 'hint links spawn -d mpv {hint-url}')
config.bind(';M', 'spawn -d mpv {url}')
config.bind(';a', 'hint links spawn -d st -g 61x1 -t media -e mpv  --no-video {hint-url}')
config.bind(';A', 'spawn -d st -g 61x1 -t media -e mpv --no-video {url}')
config.bind(';ch', 'hint links spawn -d st -f "Mono:pixelsize=5" -n "float" -g 200x75 -e mpv {hint-url} --quiet --vo=tct')
config.bind(';D', 'hint {right-click}')
config.bind('dd', 'tab-close')
config.bind('<Shift-d>', 'tab-clone')
config.bind('<Ctrl-e>', 'scroll down')
config.bind('<Ctrl-y>', 'scroll up')
config.bind('ys', 'yank selection')
config.bind('ps', 'insert-text {primary}')
config.bind('<<Ctrl-Escape>', 'mode-leave', mode='passthrough')
config.bind('<<Ctrl-Shift-j>', 'tab-move +')
config.bind('<<Ctrl-Shift-k>', 'tab-move -')
config.unbind('<Shift-Escape>', mode='passthrough')
config.bind('<<Ctrl-Shift-k>', 'tab-move -')
config.bind('<<Ctrl-m>', 'tab-mute')

config.bind('<Ctrl-n>', 'search-next', mode='command')
config.bind('<Ctrl-N>', 'search-prev', mode='command')
# command mode
config.bind('<Alt-x>', 'set-cmd-text : {url}')
# config.bind('<Up>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-p>', 'command-history-prev', mode='command')
# config.bind('<Down>', 'command-history-next', mode='command')
# config.bind('<Ctrl-n>', 'command-history-next', mode='command')
# config.bind('<Escape>', 'leave-mode', mode='command')
# config.bind('<Ctrl-g>', 'leave-mode', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Ctrl-m>', 'command-accept', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Ctrl-Shift-i>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')

config.bind('J', 'completion-item-focus next', mode='command')
config.bind('K', 'completion-item-focus prev', mode='command')

# config.bind('<Shift-k>', 'tab-next')
# config.bind('<Shift-j>', 'tab-prev')
# config.bind(',d' 'config-cycle content.user_stylesheets = '~/.local/share/qutebrowser/stylesheet/discord.css' ;; content.user_stylesheets ')

# c.content.user_stylesheets = "~/solarized-everything-css/css/apprentice/apprentice-all-sites.css"

# # defalt text editor
c.editor.command = [ 'st', '-e', 'nvim', '{file}']
c.editor.encoding = 'utf-8'

# Dark mode 
c.colors.webpage.preferred_color_scheme = "dark"
config.set("colors.webpage.darkmode.enabled", True)
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = "smart"

ccw = c.colors.webpage
ccw.bg = "black"
ccw.darkmode.enabled = True
ccw.darkmode.threshold.background = 100
ccw.darkmode.threshold.text = 256 - ccw.darkmode.threshold.background
ccw.darkmode.policy.images = 'smart'
# ccw.prefers_color_scheme_dark = True

# tabs
c.tabs.indicator.width = 0
c.tabs.padding = {'top': 1, 'bottom': 1, 'left': 2, 'right': 2}
c.tabs.position = 'top'
#c.tabs.title.format = '{index}'
#c.tabs.title.format_pinned = '{index}'
c.tabs.width = 31

# Bookmarks
config.unbind('<d>', mode='normal')

# notification
# content.notifications = "false"

# scroll bar

c.scrolling.bar = "never"

#c.tabs.position = "left"
c.tabs.last_close = "close"
c.statusbar.show = "in-mode"
c.tabs.show = "never"

# addblock
# c.content.blocking.hosts.lists = ["https://easylist.to/easylist/easylist.txt", "https://easylist.to/easylist/easyprivacy.txt", "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt"]
c.content.blocking.method = "both"
c.fileselect.single_file.command = ['["st", "-e", "vifm", "--choose-file", "{}"]', "vifm in st"]
c.fileselect.multiple_files.command = ['["st", "-e", "vifm", "--choose-file", "{}"]', "vifm in st"]




# urls
c.url.searchengines = {
    "DEFAULT": search,
    "!g":   "https://google.com/search?q={}",
    "!gh":  "https://github.com/search?o=desc&q={}&s=stars",
    "!gl":  "https://gitlab.com/#stq={}",
    '!r':   'https://www.reddit.com/search/?q={}',
    '!s':   'https://searx.be/search?q={}',
    '!sp':  'https://open.spotify.com/search/{}',
    '!tw':  'https://twitter.com/search?q={}',
    '!p':   'https://tpb.party/search/{}',
    "!w":   'https://en.wikipedia.org/wiki/{}',
    '!aw':  'https://wiki.archlinux.org/index.php/{}',
    '!y':   'https://www.youtube.com/results?search_query={}'
}

# defalt pacges
c.url.default_page = base
c.url.start_pages = base
c.editor.command = ["st", "-t", "edit_text", "-e", "nvim", "-f", "{}"]

# downloads location
c.downloads.location.directory = "~/download"

###################################################
c.content.autoplay = False
###################################################

    # """Block the given request if necessary."""
    # url = info.request_url
    # if (
    #     url.host() == "www.youtube.com"
    #     and url.path() == "/get_video_info"
    #     and "&adformat=" in url.query()
    # ):
    #     info.block()


# interceptor.register(filter_yt)

######################################################
# set qutebrowser colors
######################################################

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = xresources["*.foreground"]

# background color of the completion widget for odd rows.
c.colors.completion.odd.bg = xresources["*.background"]

# background color of the completion widget for even rows.
c.colors.completion.even.bg = xresources["*.background"]

# foreground color of completion widget category headers.
c.colors.completion.category.fg = xresources["*.color7"]

# background color of the completion widget category headers.
c.colors.completion.category.bg = xresources["*.color12"]

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = xresources["*.background"]

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = xresources["*.background"]

# foreground color of the selected completion item.
c.colors.completion.item.selected.fg = xresources["*.background"]

# background color of the selected completion item.
c.colors.completion.item.selected.bg = xresources["*.color2"]

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = xresources["*.color12"]

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = xresources["*.color12"]

# foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = xresources["*.color10"]

# foreground color of the matched text in the completion.
c.colors.completion.match.fg = xresources["*.color2"]

# background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = xresources["*.color8"]

# foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = xresources["*.foreground"]

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = xresources["*.background"]

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = xresources["*.background"]

# background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = xresources["*.background"]

# foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  xresources["*.foreground"]

# background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = xresources["*.color12"]

#foreground color: of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = xresources["*.background"]

# background color for the download bar.
c.colors.downloads.bar.bg = xresources["*.background"]

# Color gradient start for download text.
c.colors.downloads.start.fg = xresources["*.background"]

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = xresources["*.color5"]

# Color gradient end for download text.
c.colors.downloads.stop.fg = xresources["*.background"]

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = xresources["*.color2"]

# foreground color for downloads with errors.
c.colors.downloads.error.fg = xresources["*.color1"]

# Font color for hints.
c.colors.hints.fg = xresources["*.foreground"]

# background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = xresources["*.background"]

# Font color for the matched part of hints.
c.colors.hints.match.fg = xresources["*.color2"]

# Text color for the keyhint widget.
c.colors.keyhint.fg = xresources["*.foreground"]

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = xresources["*.foreground"]

# background color of the keyhint widget.
c.colors.keyhint.bg = xresources["*.background"]

# foreground color of an error message.
c.colors.messages.error.fg = xresources["*.color0"]

# background color of an error message.
c.colors.messages.error.bg = xresources["*.color1"]

# Border color of an error message.
c.colors.messages.error.border = xresources["*.color0"]

# foreground color of a warning message.
c.colors.messages.warning.fg = xresources["*.background"]

# background color of a warning message.
c.colors.messages.warning.bg = xresources["*.color1"]

# Border color of a warning message.
c.colors.messages.warning.border = xresources["*.color0"]

# foreground color of an info message.
c.colors.messages.info.fg = xresources["*.color2"]

# background color of an info message.
c.colors.messages.info.bg = xresources["*.background"]

# Border color of an info message.
c.colors.messages.info.border = xresources["*.background"]

# foreground color for prompts.
c.colors.prompts.fg = xresources["*.foreground"]

# Border used around UI elements in prompts.
c.colors.prompts.border = xresources["*.background"]

# background color for prompts.
c.colors.prompts.bg = xresources["*.background"]

# background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = xresources["*.color12"]

# foreground color of the statusbar.
c.colors.statusbar.normal.fg = xresources["*.foreground"]

# background color of the statusbar.
c.colors.statusbar.normal.bg = xresources["*.background"]

# foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = xresources["*.background"]

# background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = xresources["*.color4"]

# foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = xresources["*.background"]

# background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = xresources["*.color9"]

# foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = xresources["*.color0"]

# background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = xresources["*.color5"]

# foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = xresources["*.color2"]

# background color of the statusbar in command mode.
c.colors.statusbar.command.bg = xresources["*.background"]

# foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = xresources["*.color5"]

# background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = xresources["*.background"]

# foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = xresources["*.background"]

# background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = xresources["*.color11"]

# foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = xresources["*.background"]

# background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = xresources["*.color5"]

# background color of the progress bar.
c.colors.statusbar.progress.bg = xresources["*.color5"]

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = xresources["*.foreground"]

# foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = xresources["*.color2"]

# foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = xresources["*.color11"]

# foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = xresources["*.color13"]

# foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = xresources["*.color13"]

# foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = xresources["*.color1"]

# background color of the tab bar.
c.colors.tabs.bar.bg = xresources["*.background"]

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = xresources["*.color5"]

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = xresources["*.color11"]

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = xresources["*.color1"]

# foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = xresources["*.foreground"]

# background color of unselected odd tabs.
c.colors.tabs.odd.bg = xresources["*.color0"]

# foreground color of unselected even tabs.
c.colors.tabs.even.fg = xresources["*.foreground"]

# background color of unselected even tabs.
c.colors.tabs.even.bg = xresources["*.color8"]

# background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = xresources["*.color11"]

# foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = xresources["*.background"]

# background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = xresources["*.color10"]

# foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = xresources["*.foreground"]

# background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = xresources["*.color2"]

# foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = xresources["*.background"]

# background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = xresources["*.color2"]

# foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = xresources["*.color12"]

# foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = xresources["*.foreground"]

# background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = xresources["*.color12"]

# foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = xresources["*.foreground"]

# background color of selected even tabs.
c.colors.tabs.selected.even.bg = xresources["*.color12"]

# background color for webpages if unset (or empty to use the theme's color).
c.colors.webpage.bg = xresources["*.background"]
