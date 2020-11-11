 [[ -f ~/.bashrc ]] && . ~/.bashrc

# Default programs:
export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="qutebrowser"

if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then exec startx; fi
#export READER="zathura"
