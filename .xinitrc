#!/bin/sh
# ~/.xinitrc

# unset DISPLAY
export EDITOR="nvim"
export READER="zathura"
# export VISUAL="nvim"
export TERM="st"
export BROWSER="qutebrowser"
# export COLORTERM="truecolor"
export PAGER="less"
export WM="dwm"
export VIEW="sxiv"


# clear tmp
# doas rm -rf /tmp/*

# set backlight
# xbacklight -inc .04

# set trackpoint to full speed
xinput set-prop "TPPS/2 IBM TrackPoint" "332" .3

# set key repeat rate. delay 300 milisecond, 80 per sec
xset r rate 200 30

# set  
setxkbmap colemak_wide

# run "togele track pad" script
xinput --disable "TPPS/2 IBM TrackPoint"
xinput --disable "Synaptics TM3276-022"

# set wallpaper
# xwallpaper --zoom	~/.local/share/bg
# xwallpaper --zoom	~/.config/black.png

# color
xrdb .config/Xresources

# xcompmgr &
# unclutter -idle 0 &
# picom --experimental-backends &
# dunst &
# compton &
# shotkey &
mpd &
sxhkd &
if [ $WM = dwm ]; then
	dwmblocks &
	hhpc &
fi

# start $WM 
while true; do 
	$WM >/dev/null 2>&1
done
exec $WM
