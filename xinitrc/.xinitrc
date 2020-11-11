#!/bin/sh
# ~/.xinitrc

# set defaults
export EDITOR="nvim"
export TERM="st"
export BROWSER="qutebrowser"

# set backlight
doas xbacklight -set 25

# set trackpoint to full speed
xinput set-prop "TPPS/2 IBM TrackPoint" "332" 1.0

# set key repeat rate. delay 300 milisecond, 80 per sec
xset r rate 200 30

# set  
setxkbmap colemak_wide

# run "togele track pad" script
xinput --disable "TPPS/2 IBM TrackPoint"
xinput --disable "Synaptics TM3276-022"

# set wallpaper
# xwallpaper --zoom .config/wall.png &

# color
xrdb .config/Xresources &

# xcompmgr &
unclutter --timeout "1" --ignore-scrolling &
dunst &
bar &
# compton &
sxhkd &
doas powertop --auto-tune &


# start dwm 
while true; do 
	dwm >/dev/null 2>&1
done
exec dwm
