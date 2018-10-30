---
title: "Using VirtualBox to install Ubuntu"
author: "Hadir Garcia-Castro"
date: 2017-12-20T11:53:49-07:00
description: "Using VirtualBox to install Ubuntu."
type: technical_note
draft: false
---

# Install Guest Additions on Ubuntu
1. Click on Install Guest Additions… from the Devices menu, then choose to browse the content of the CD when requested.
2. Check if sudo is installed, otherwise install it.
``` bash
su -
password:
apt-get install sudo -y
usermod -aG sudo yourusername
sudo apt-get install linux-headers-amd64
````

if it is not running, then install gcc :bash:'sudo apt-get install build-essential gcc make perl'

2. Run :bash:"sudo sh /media/your_username/VBoxLinuxAdditions.run", and follow the instructions on screen.


# Share a folder between Host and Guest
1. Install Guest Additions in your guest Ubuntu
2. Restart your virtual machine
3. Try to access /media/sf_your_shared_folder_name. If you still don't have access, that means you don't belong to the vboxsf group.

:code-block:: bash
    sudo adduser your_username vboxsf

4. Restart your virtual machine to apply changes of adduser.
