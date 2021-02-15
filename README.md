[![Run on Repl.it](https://repl.it/badge/github/aelmosalamy/ascii-combat)](https://repl.it/github/aelmosalamy/ascii-combat)

NOTE 5th March 2020 - The project have been discontinued, I am planning to work on it, but I am busy working on other stuff lately, right now one of the most necessary missing features is procedural dungeon generation, the game right now works with the same dungeon every single time, the core basics are already done, more items need to be added, winning/losing elements don't exist yet, there is 2 modes: Explore mode where you can go, drop, pick, buy, eat, look on things and move accross the dungeon AND the Combat mode where you can atk, pwr and fight multiple enemies and eventually beat them (which was how this project started before I decided to expand it into a whole 1000 LOC not-so-messy but definitely need sometime to get used to the code and the project structure), I am open to any feedback or commnets and even PRs.

Fork specific Note (5th Feb 2021): This fork is live, baby. Got the basis of a procedurally generated dungeon up and running, geometry is whack though. Implemented losing (through sweet sweet death), as well as a few other things I lost track of. Existing issues in the comments.

## ASCII Combat
A simple CLI text adventure game, created for learning purposes.

### Project objectives

* Fully functional dungeon system for exploration.
* Creating an inventory system with the ability to pickup, eat and get info about items found throughout the dungeon
* Enemies distributed over dungeon entrances, explore further by beating them in a role-based combat system.

### Usage instructions
#### Note: This game uses Python 3 ONLY. Using Python 2 will not work!
- Get sources either by downloading `.zip` file and extracting it
- Or by cloning the master branch `git clone https://github.com/aelmosalamy/ascii-combat`
- To setup: run `pip3 install colorama` or `pipenv install`
- To play: run `python3 main.py`

### Game Modules

* The game mainly uses two modules: Cmd (to run the a generic command-line interface with several useful features) and colorama (an amazing ANSI sequence text colorizer).

### Pull Requests

* I really welcome pull requests, specially if it is your first time, checkout the current issues and any little correction, bugfix, new feature will be reviewed and added if possible.
* Feel free to send PRs (Check open issues first).
* Clean, well-documented code is pretty appreciated.
* THIS IS VERY IMPORTANT: If you are using Unix-based system for writing code, make sure to convert your code's newlines to CRLF (The default terminator used by Windows) since this causes tons of merge conflicts!

### Future Plans

* We all agree its fun to play text-based games as this genre got its very own fans, however we further agree on the beauty of graphics, so I am planning to make a pygame version of this, exactly same concept with simplistic, yet beautiful 8-bit pixel art graphics, I intend to create a roguelike exploration system + a role-based combat system which acts like an obstacle to the advance of exploration in the dungeons of ASCII Combat, mmm... shall we say 'Pixel Combat'? :)
