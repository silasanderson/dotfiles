#!/bin/sh
# ~/.xinitrc

# set defaults
export EDITOR="nvim"
export TERM="st"
export BROWSER="qutebrowser"

# set backlight
doas xbacklight -set 50

# set trackpoint to full speed
xinput set-prop "TPPS/2 IBM TrackPoint" "332" 1.0

# set key repeat rate. delay 300 milisecond, 80 per sec
xset r rate 300 80

# set  
setxkbmap colemak_wide

# run "togele track pad" script
ttp

# set wallpaper
xwallpaper --zoom ~/.config/gloryhammer.jpg

#xcompmgr &
unclutter &
dunst &
pulseaudio &

# start dwm 
while true; do 
	dwm >/dev/null 2>&1
done
exec dwm
