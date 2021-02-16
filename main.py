'''
This is just "main" module that launchs our game
and start the cmdloop()
'''
from dicts.weapons_skills import *
from dicts.rooms import *
from dicts.utils import *
from dicts.monsters import give_monster
import combat, dungeon, sys

def main():
    sys.path.append(os.getcwd())
    set_console_size()
    yername = input('What is your name?> ')
    me = Player(yername, 10, WEAPONS[FIST])

    world = dungeon.Dungeon(me, ROOMS)
    world.cmdloop()

if __name__ == '__main__':
    main()
