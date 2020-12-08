# # Enable colors and change prompt:
autoload -U colors && colors	# Load colors

export TERM=st-256color

autoload colors; colors
for color (${(k)fg})
  eval "$color() {print -n \$fg[$color]; cat; print -n \$reset_color}"

setopt autocd		# Automatically cd into typed directory.
stty stop undef		# Disable ctrl-s to freeze terminal.
unsetopt BEEP
# unset DISPLAY

# History in cache directory:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history
source ~/.local/share/zsh/plugin/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.local/share/zsh/plugin/zsh-system-clipboard/zsh-system-clipboard.zsh


# Enable searching through history
# bindkey '^R' history-incremental-pattern-search-backward

# Load aliases and shortcuts if existent.
# [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/shortcutrc" ] && source "${XDG_CONFIG_HOME:-$HOME/.config}/shortcutrc"
[ -f "${XDG_CONFIG_HOME:-$HOME/.config}/aliasrc" ] && source "${XDG_CONFIG_HOME:-$HOME/.config}/aliasrc"
# [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/zshnameddirrc" ] && source "${XDG_CONFIG_HOME:-$HOME/.config}/zshnameddirrc"

# Basic auto/tab complete:
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

# Auto complete with case insenstivity
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
# bindkey -M menuselect 'left' vi-backward-char
# bindkey -M menuselect 'down' vi-down-line-or-history
# bindkey -M menuselect 'up' vi-up-line-or-history
# bindkey -M menuselect 'right' vi-forward-char

# bindkey -v '^?' backward-delete-char
bindkey -v
export KEYTIMEOUT=1

# Change cursor with support for inside/outside tmux
function _set_cursor() {
    if [[ $TMUX = '' ]]; then
      echo -ne $1
    else
      echo -ne "\ePtmux;\e\e$1\e\\"
    fi
}

function _set_block_cursor() { _set_cursor '\e[2 q' }
function _set_beam_cursor() { _set_cursor '\e[6 q' }

function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] || [[ $1 = 'block' ]]; then
      _set_block_cursor
  else
      _set_beam_cursor
  fi
}
zle -N zle-keymap-select
# ensure beam cursor when starting new terminal
precmd_functions+=(_set_beam_cursor) #
# ensure insert mode and beam cursor when exiting vim
zle-line-init() { zle -K viins; _set_beam_cursor }

# # Use lf to switch directories and bind it to ctrl-o
# lfcd () {
#     tmp="$(mktemp)"
#     lf -last-dir-path="$tmp" "$@"
#     if [ -f "$tmp" ]; then
#         dir="$(cat "$tmp")"
#         rm -f "$tmp" >/dev/null
#         [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
#     fi
# }
# bindkey -s '^o' 'lfcd\n'

bindkey '^ ' 'autosuggest-accept'

# bindkey -s '^f' 'cd "$(dirname "$(fzf)")"\n'

bindkey '^[[P' delete-char

# # Edit line in vim buffer ctrl-v
autoload edit-command-line; zle -N edit-command-line
bindkey '^v' edit-command-line
# # Enter vim buffer from normal mode
autoload -U edit-command-line && zle -N edit-command-line && bindkey -M vicmd "^v" edit-command-line


PROMPT='%F{cyan}%3~%f %F{green}% |> %F{white}'
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=yello"

source ~/.local/share/zsh/plugin/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 
