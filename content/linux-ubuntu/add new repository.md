---
title: "Adding new repositories"
author: "Hadir Garcia-Castro"
date: 2017-12-20T11:53:49-07:00
description: "Adding new repositories in Ubuntu."
type: technical_note
draft: false
---

# Adding new repositories

to add a new repository in ubuntu linux, it is necessary to run the terminal as root.

To run terminal as root, use:

```bash
  sudo -i
```
Then run the command line on bash:

```bash
add-apt-repository 'deb uri distribution [component1] [component2] [...]'
```
or

```bash
add-apt-repository ppa:<ppa_name>
```

Example

```bash
add-apt-repository 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main'
add-apt-repository ppa:postgresql
```
