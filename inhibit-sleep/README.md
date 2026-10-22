# Inhibit sleep

This simple application opens a terminal window a stops the computer from suspending (or reacting to lid switch).

The app normally runs with sudo and prompts for password on each start. This is because cosmic requiers root permissions to actually inhibit sleep. This can be turned off with the -s flag.

## Install

To install this app, run "install" from this folder. There are optional flags:
- -v Give more detailed info about the installation process
- -s When this flag is given, the program will run WITHOUT sudo.

To uninstall, run "uninst" from this folder.
