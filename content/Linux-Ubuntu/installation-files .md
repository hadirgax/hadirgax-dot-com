---
title: "Installing '.sh' files"
author: "Hadir Garcia-Castro"
date: 2017-12-20T11:53:49-07:00
description: "Installing '.sh' files to Ubuntu."
type: technical_note
draft: false
---

# Installing '.sh' files

1. Make the file executable:
Here we have two options:
  a) right click  over the file, go to properties, then click on the Permissions tab and then in Execute, check the 'Allow executing file as program' option.
  b) In the terminal write this command line `chmod ug+x ./file_name.sh`

2. Execute the file in the terminal using the command line, `./file_name.sh`


# Installing a '.deb' file
-------------------
1. Execute in the terminal using the command line, `sudo dpkg -i filename.deb`
