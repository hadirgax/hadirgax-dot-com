---
title: "Working with dates and time functions"
author: "Hadir Garcia-Castro"
date: 2018-10-22T16:32:58.713
type: technical-note
draft: false
---
# Working with dates and time functions

Examples of date/time functions in Julia.

## Preliminaries

Load the required packages (if not installed or not updated), it is not necessary to execute every time.


```julia
#In
using Pkg
Pkg.add("Dates")

#Out
```

    [32m[1m Resolving[22m[39m package versions...
    [32m[1m  Updating[22m[39m `C:\Users\Hadir Castro\.julia\environments\v1.0\Project.toml`
    [90m [no changes][39m
    [32m[1m  Updating[22m[39m `C:\Users\Hadir Castro\.julia\environments\v1.0\Manifest.toml`
    [90m [no changes][39m
    

Call the 'Dates' package.


```julia
#In
using Dates
```

## `now()` function

A simple function that returns the just now time in `'YYYY-MM-DDTHH:mm:ss.ms'` format.


```julia
#In
now = Dates.now()

#Out
```




    2018-11-06T18:25:48.97


