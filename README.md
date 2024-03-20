# Computer Spy Games

These files are a translation of an old programming book from the 1980s
called 'Computer Spy Games'. The idea was to teach children programming
using basic. Due to multiple different systems back in the day there were marks
advising of when the code needed to be changed for a specific machine.

I used a Commodore 64 for my machine, though I never owned this book as a kid
and have only recently got access to it.

However, I have decided to translate them into modern computer languages. Initially
I was going to do it using C++, Java, and Python however issues arose that made me
decide to just use python, due to things that don't exist in modern langauges and would
require threading to be able to execute properly (though not necessarily in the same way
as it was executed on the older computers)

[The book is now available online to download for free](https://archive.org/details/Computer_Spy_Games)

## Executing the Games

A *shebang* has been included in the files so that they can be executed directly from the
command line. However, for that to work you will need to make the file executable. Since these
games run only on Linux, you will need to go to the directory on the command line and type

*chmod +x [game name].py*

However, a loader program has been included, so that is the only one that theoretically needs to be
executed as all of the other programs can be executed from that one.

## Issues
The issue regarding getting the INKEY to work properly is still present.

## Games

**Spy Eyes**


## Updates
**20 March 2024**
Created the initial folder to hold the contents on the game and configured the loader program
