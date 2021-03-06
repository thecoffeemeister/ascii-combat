[![Run on Repl.it](https://repl.it/badge/github/aelmosalamy/ascii-combat)](https://repl.it/github/aelmosalamy/ascii-combat)
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
