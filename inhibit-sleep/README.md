# Inhibit sleep

This simple application opens a terminal window a stops the computer from suspending (or reacting to lid switch).

The works as an terminal command, but can also be installed as an application (which runs in the terminal) with the -d flag. For the command to work, make sure that $HOME/.local/share/bin/ is in $PATH

The app normally runs without sudo. Some desktops, such as Cosmic, require root permissions to successfully inhibit suspend. If that is your case, use the -s flag.

## Install

To install this app, run "install" from this folder. There are optional flags:
- -d Creates a inhibit-sleep.desktop file in $HOME/.local/share/applications/
- -s When this flag is given, the program will run with sudo. Only user for the .desktop file.
- -v Give more detailed info about the installation process

To uninstall, run "uninst" from this folder.
