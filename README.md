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
To run the games you will need to install sshkeyboard (see below).

## Issues
The issue regarding getting the INKEY to work properly is still present.

I have since found a solution to this, using sshkeyboard. However it is a separate library and has to be added. To add it you type:

pip install sshkeyboard

## Games

**Spy Eyes**: This game involves the player noticing a slight change in the
board. One of the numbers will move, and the player must then advise what
number moved. A high score function has been added that saves the high score
and reloads it whenever a new game is started.

**Searchlight**: In this game the player has to travel from one side of the
board to the other and avoid being spotted. A searchlight will turn on and off.
If the player is not behind cover when the searchlight is on, the then player
is spotted and loses. Due to the complexity of this game, a graphical interface
has been added.

**Robospy**: This game displays directions and you need to remember them, and then repeat them once
they disappear. Every five moves another direction is added, and the game speeds up a bit making it
more difficult. I have managed to find a library for python that will take a key input. However the
library seems to be rather new, and a global variable is required to take the value out of the function.

**Spy Q Test**: I won't call it a guess game, but rather a game where you need to arrange random numbers
in order. However, the catch is that you don't know the numbers, and you only have 10 spots. Also, you
only have a limited number of numbers that you can discard. So, when the numbers appear, you need to
place them in a position, but also be aware that there are more numbers that will appear, and you don't
know what they are. Further, the higher you go up levels, the less discards you get.

**Secret Message Maker**: This is a simple encryption program that coverts a message to ASCII, changes the
number by a random number, switches the letters and returns a coded message. To decode it, it reverses it.
In a way it reminds me a bit of the encyrption course we did at university, though RSA encryption and the like
is much, much more complicated. You could say this is like a Ceaser Cypher, though it does a bit more than that
such as switching the letters around.

**Rendezvous**: This game seems to be a really basic style of adventure game. Basically you are in a town and
have to perform a number of tasks before the last flight leaves. This includes finding a password, a key, and
arranging a meeting time for your agent all the while avoiding the enemy agent. Initially there is only a 
single word parser, but I made some modifications to add a multi word one. Also, I added some extra commands 
including displaying valid commands, the locations, and also the ability to quit the game.


## Updates
**20 March 2024**
Created the initial folder to hold the contents on the game and configured the loader program.
Started adding Spy Eyes

**22 March 2024**
Finished set up and display for Spy Eyes.

**24 March 2024**
Completed Spy Eyes with the suggested added functions

**1 April 2024**
Completed the command line version of Searchlight

**6 April 2024**
Completed the graphical interface for Searchlight and added sound

**12 May 2024**
Started building Robospy, and have found a way of taking a key press without
using pygame. This one uses sshkeyboard.

**13 May 2024**
Finished Robospy. All need to do is test it.

**15 May 2024**
Finished bug testing Robospy and it now works.

**17 July 2024**
Added Spy Q Test

**26 July 2024**
Adding Secret Message Maker

**28 July 2024**
Completed Secret Message Maker

**10 August 2024**
Completed and tested Rendezvous

**11 August 2024**
Added multi word parser to Rendezvous

**23 August 2024**
Completed Morse Encoder


