'''
This is just "main" module that launchs our game
and start the cmdloop()

Currently working on graph_rooms in dungeon.py
See notes at graph_rooms function
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
    classtype = ""
    while not (classtype in ['1','2','3','cheat']):
        classtype = input("Pick Your Class:\n1) Daggerman\n2) Armorlady\n3) Richtwitch\n#> ")
    me = Player(yername, 10, WEAPONS[FIST])

    world = dungeon.Dungeon(me, ROOMS)
    world.setClass(classtype)
    world.cmdloop()

if __name__ == '__main__':
    main()
