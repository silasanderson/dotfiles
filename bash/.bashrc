#
# ~/.bashrc
#
# If not running interactively, don't do anything

[[ $- != *i* ]] && return

shopt -s autocd 

alias vim="nvim"

alias V="nvim"

alias P="doas pacman"

alias sudo="doas"

alias S="doas"

alias ls='ls --color=auto'

alias wtr='curl wttr.in/?m'

alias ntest='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -'

alias A='alsamixer'

alias ttp="~/script/ttp.sh"

# PS1='[\u@\h \W]\$ '
