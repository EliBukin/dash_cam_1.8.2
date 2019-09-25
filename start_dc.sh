#!/bin/bash

# get the path (name) of the usb connected:
usb=`lsblk -a -o MOUNTPOINT | grep /media/pi`
echo "$usb"

# check if $usb variable has content and update the PY section in config file with the DESTINATION:
if [ -z "$usb" ]
then
      echo "\$usb is null"
else
      sed  -i 's|/media/pi.*|'"$usb"'/videos/|' /home/pi/Desktop/dash_cam_1.8.2/dc.config
fi

# allow access to config file:
. /home/pi/Desktop/dash_cam_1.8.2/dc.config

# call the scripts:
sudo bash $limit_folder_size_filepath & sudo python $start_recording_filepath

