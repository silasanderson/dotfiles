# set some defalt colors
base00 = "#000000"
base01 = "#3D4048"
base02 = "#53555D"
base03 = "#686A71"
base04 = "#7E8086"
base05 = "#939599"
base06 = "#A9AAAE"
base07 = "#BEBFC2"
base08 = "#B21889"
base09 = "#786DC5"
base0A = "#438288"
base0B = "#5eff99"
base0C = "#00A0BE"
base0D = "#790EAD"
base0E = "#B21889"
base0F = "#C77C48"
basebl = "#000000"
basewh = "#ffffff"
baseg  = "#5eff99"
base =   "~/.local/share/qutebrowser/startpage/index.html"
# base =   "about:blank"
search = "https://searx.ninja/search?q={}"

c.fonts.default_family = "Hack"
c.fonts.default_size = "10pt" 

# Bind
config.bind(' q',   'quit')
config.bind(';w',   'hint all window')
config.bind(',q',   'open https://qutebrowser.org/doc/help/settings.html')
config.bind(',gm',  'open https://mail.google.com/mail/u/0/?pli=1#inbox')
config.bind(',ch',  'open https://raw.githubusercontent.com/qutebrowser/qutebrowser/master/doc/img/cheatsheet-big.png')
config.bind (',gs', 'open https://github.com/silasanderson')
config.bind (',y',  'open https://www.youtube.com')
config.bind (',d',  'open https://github.com/silasanderson/dotfiles')
config.bind (',a',  'open https://artstation.com')
#config.unbind('https://google.com/search?q={}<d>', mode='normal')
config.bind('m',    'set-cmd-text -s :quickmark-load')
config.bind('xt', 'config-cycle tabs.show always switching')
config.bind('xb', 'config-cycle statusbar.show always in-mode')
config.bind('xx', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always never')
config.bind('<Ctrl-r>', 'restart')
config.bind(';M', 'spawn mpv {url}')
config.bind(';m', 'hint links spawn mpv {hint-url}')
config.bind(';D', 'hint {right-click}')
config.bind('dd', 'tab-close')
config.bind('<Shift-d>', 'tab-clone')
config.bind('<Ctrl-e>', 'scroll down')
config.bind('<Ctrl-y>', 'scroll up')
config.bind('<Alt-Escape>', 'leave-mode', mode='passthrough')
config.unbind('<Shift-Escape>', mode='passthrough')
#config.bind('<Shift-k>', 'tab-next')
#config.bind('<Shift-j>', 'tab-prev')
# config.bind(',d' 'config-cycle content.user_stylesheets = '~/.local/share/qutebrowser/stylesheet/discord.css' ;; content.user_stylesheets ')

# c.content.user_stylesheets = "~/solarized-everything-css/css/apprentice/apprentice-all-sites.css"

# defalt text editor
c.editor.command = [ 'st', '-e', 'nvim', '{file}']
c.editor.encoding = 'utf-8'

# Dark mode 

# c.colors.webpage.prefers_color_scheme_dark = True
# config.set("colors.webpage.darkmode.enabled", True)
# c.colors.webpage.darkmode.enabled = True
# c.colors.webpage.darkmode.policy.images = "smart"

c.qt.args = [ "blink-settings=darkMode=4" ]  
ccw = c.colors.webpage
ccw.bg = "black"
ccw.darkmode.enabled = True
ccw.darkmode.threshold.background = 100
ccw.darkmode.threshold.text = 256 - ccw.darkmode.threshold.background
ccw.darkmode.policy.images = 'smart'
ccw.prefers_color_scheme_dark = True

# tabs
c.tabs.indicator.width = 0
c.tabs.padding = {'top': 1, 'bottom': 1, 'left': 2, 'right': 2}
c.tabs.position = 'top'
#c.tabs.title.format = '{index}'
#c.tabs.title.format_pinned = '{index}'
c.tabs.width = 31

# Bookmarks
config.unbind('<d>', mode='normal')

# scroll bar

c.scrolling.bar = "never"

#c.tabs.position = "left"
c.tabs.last_close = "close"
c.statusbar.show = "in-mode"
c.tabs.show = "never"

# urls
c.url.searchengines = {
    "DEFAULT": search,
    "g":   "https://google.com/search?q={}",
    "gh":  'https://github.com/search?o=desc&q={}&s=stars',
    'w':   'https://en.wikipedia.org/wiki/{}',
    'aw':   'https://wiki.archlinux.org/index.php/{}',
    'ud':   'https://www.urbandictionary.com/define.php?term={}',
    'y':   'https://www.youtube.com/results?search_query={}'
}

#searchengines
#c.url.searchengines = {

#    'DEFAULT':  'https://searx.ninja/search?q={}',
 #   'gh':      'https://github.com/search?o=desc&q={}&s=stars',
  #  'w':       'https://en.wikipedia.org/wiki/{}',
   # 'g':       'https://www.google.com/results?search_query={}'
    #'yt';      'https://www.youtube.com/results?search_query={}'
#}

# defalt pacges
c.url.default_page = base
c.url.start_pages = base
c.editor.command = ["st", "-t", "edit_text", "-e", "nvim", "-f", "{}"]

# downloads location
c.downloads.location.directory = "~/download"

###################################################
###################################################

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base00

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0A

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base01

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base0A

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base0A

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base0A

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base08

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base0B

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = base01

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = base04

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = basebl

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base0A

#Foreground color: of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base01

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = basebl

# Background color for prompts.
c.colors.prompts.bg = basebl

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base0A

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base0B

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base00

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base0D

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base00

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base0C

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base00

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base01

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base00

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base05

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base00

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base00

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base0E

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base00

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base0D

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base05

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = basebl

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = basebl

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = basebl

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0C

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base07

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base07

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base05

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base00

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base05

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base0E

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base00

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base05

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base00

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base05

# Background color for webpages if unset (or empty to use the theme's color).
c.colors.webpage.bg = base00
