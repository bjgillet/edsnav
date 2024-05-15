# edsnav : Elite Dangerous Session Navigator

Objective is to have a graphical session browser and exploration planning tool.
It will focus on the "diary" aspect of game sessions, only based on personal achievement (so not connected to existing or ever explored sources)
As having a good number of platforms, and traveling a lot, I often need to sychronize between my Windows TUF laptop and my more serious Linux platforms.
When at home (and sometime when travelling) I have multi-screen display, so one screen for the game, one for the tool is fine.

Therefore it will be a simple tool, but with the following targeted keypoints :

- Post session log analysis and events display.
- Live session log analysis.
- Local or Multi hosts : Game platform to send logs/events, reciever platform to display results and archive them.
- DataBase for log/sessions storage, local or remote
- Database parsing for known objects and stats (ie. where did I discovered XXX material at closest from current location, cmdr carreer, etc...)
- Database and logs synchronisations in multihosts environments.

It will be wrtten in python 3. GUI will be designed in GTK4 for Linux environments, with probably a simpler interface in TK/TCL tkinter for Windows (when not wanting to install GTK on Windows).

**This project is in early build stage - not even an alpha release**
**It currently have to be considered as a dev branch as I code from several different platforms and need git to synchronize**

This comment will evolved as it will start becoming mature.


