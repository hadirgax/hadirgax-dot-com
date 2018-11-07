---
title: The .gitignore file
date: 2018-10-31T22:36:29.479
draft: true
author: "Hadir Garcia-Castro"
---
# The .gitignore file

This file allows to ignore/untrack the specified files and folders. To creates a `.gitignore` file, open you prefered text editor and saves a new file with the name `.gitignore` into the folder to be tracked by Git.

To ignoring files/folders, do write the following comands in the `.gitignore` file previously created:

## Ignoring a folder

Starts the line writing `*` followed by `/` and then the name of the folder to be ignored. All the files into that folder will be untraked by the version control manager.

Example:

```cmd
# Untraked Folders
*/foo
*/bar
*/untracked
```

## Ignoring a file

[to be doing]
