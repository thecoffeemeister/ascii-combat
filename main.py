'''
This is just "main" module that launchs our game
and start the cmdloop()
'''

#og creator issues: -make death permanent (which I can do in enemies attack, but going to try to do in dungeon, so the messages are maintained)
#                   -combat mode transtions apparently only works in runlevel 3, lol
#                    everything works as it should in atom terminal as well, one fuck of problem, probably
#                    I think I figured out part of it, when the terminal is wide enough to fuck
#                    up the bottom of the transition box it works... emphasis on 'I think'
#                   -All of which is indicative of a larger problem, which is properly fusing
#                    the exploration and combat systems
#updates:           -better character creation
#                   -update installer to add a link to bin
#                   -use the photo to ascii art tool to generate ascii art for combat and
#                    transition screens
#                   -eating food for those sweet sweet heals
#                   -as well as whatever notes I left in proc_gen and rooms
from dicts.weapons_skills import *
from dicts.rooms import *
#from dicts.proc_gen import make_dungeon_map
from dicts.utils import *
from dicts.monsters import give_monster
import combat, dungeon, sys

def main():
    sys.path.append(os.getcwd())
    set_console_size()
    name = input ('What is your name? > ')
    me = Player(name, 10, WEAPONS[FIST]g)

    # currently in the process of joining world and combat systems
    world = dungeon.Dungeon(me, ROOMS)
    world.cmdloop()

if __name__ == '__main__':
    main()
