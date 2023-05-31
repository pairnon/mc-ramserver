#!/bin/bash

source .env

sudo mkdir /ramdisk

sudo echo "" >> /etc/fstab
sudo echo "" >> /etc/fstab
sudo echo "" >> /etc/fstab

sudo echo "tmpfs   /ramdisk   tmpfs   defaults,noatime,mode=1777,size=${RAMDISK_SIZE}   0   0" >> /etc/fstab

sudo systemctl daemon-reload

sudo mount -a