to add a new repository in ubuntu linux, it is necessary to run the terminal as root.

to run terminal as root, use:
  sudo -i

then run the command line on bash

add-apt-repository 'deb uri distribution [component1] [component2] [...]'
or
add-apt-repository ppa:<ppa_name>

example

add-apt-repository 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main
add-apt-repository ppa:postgresql
