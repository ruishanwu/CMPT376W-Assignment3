# LogLens - find all your log problems fast

LogLens is a really simple program that tells you what's happening in your logs. It is useful for developers, IT staff, customers, and anybody who has a computer. You don't really need to know anything about log files to get started. It finds problems in your files, so you can use it to make decisions about your system. Your data is always 100% secure.

## Requirements and things

You need Python. Most computers already have it, and version 3.6 or later should be good enough. It works on Windows, Mac, and Linux. Other than that, there is not much to know.

## Get started

First, get the project files from GitHub. Then install the program using `pip install log-lens` and run it by typing `loglens`. If you can't make it work, see docs/INSTALL.md. You probably won't need those instructions.

## Using the program

Run the following command after you have found the correct folder:

`loglens --input mylog.csv --severity error`

The software scans your log, fixes mistakes, and shows you what went wrong. You will see a number once it is finished. You can also run it on real production files without worrying about any side effects.

## Input format

The input should be a CSV file. Log files tend to have fields describing the time and what happened, but LogLens is flexible and will work with whatever columns your monitoring system uses. A small example is included somewhere in this repository.

## Questions

If something doesn't work, just contact the developers or create an issue. Make sure you describe the problem so somebody can help. This is a basic tool, so the instructions should be pretty obvious.
