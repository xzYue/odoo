#!/usr/bin/env bash

sudo mount -o remount,rw /
sudo git --work-tree=/home/pi/modoo/ --git-dir=/home/pi/modoo/.git pull
sudo mount -o remount,ro /
(sleep 5 && sudo reboot) &
