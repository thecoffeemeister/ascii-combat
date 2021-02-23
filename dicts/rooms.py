'''
Stores all unique rooms in game, every type of room got its own description and features,
this is intended to be used as the building block for the dungeon generation function which
is not yet implemented

> Must-have room attributes:
NAME, USERDESC, DESC, NORTH, SOUTH, EAST, WEST, UP, DOWN, GROUND, SHOP, ENEMIES, SEEN

> Optional room attributes:
SHOPINTRO (Greetings if room is shop)
'''
# Imports package namespace which contain all constants
from dicts import *
from dicts.proc_gen import make_dungeon_map

# Returns rooms exits as a dictionary of {DIRECTION: DESTINATION, ...}
def get_room_exits(room):
    exits = {}
    for dir in DIRECTIONS:
        if room[dir]:
            exits[dir] = ROOMS[room[dir]][NAME]
        else:
            pass
            # exits[dir] = str(None)
    return exits

# USERDESC is written in the form "You ...", It explains the player's feelings and orientation from his POV (Max 2 lines)
# DESC usually starts with (The, This, There is), describing the room and its components (Min 2 lines)
# GROUND stores items on the room ground
# SHOP stores items for sale, if empty there is no shop
# ENEMIES stores enemy ids, if empty there is no combat
# SEEN tracks wether the room was seen or it is first time
ROOMS = {
    'town_square': {
        NAME: 'Town Square',
        USERDESC: 'You are in the middle of a square, you feel lost in the crowd of people.',
        DESC: 'The square is large with a fountain in the middle, narrow, paved roads lead into all directions.',
        NORTH: 'courtyard',
        SOUTH: 'butchery',
        EAST: 'bakery',
        WEST: 'house_63',
        UP: None,
        DOWN: 'pawn_shop',
        GROUND: ['fountain', 'evergreen', 'apple', 'bread', 'coin'],
        SHOP: [],
        ENEMIES: [],
        SEEN: False,
    },
    'house_63': {
        NAME: "House 63's Entrance",
        USERDESC: 'You are inside an old, deserted house. You see a dark staircase leading upwards.',
        DESC: 'This house looks like it is going to collapse.',
        NORTH: None,
        SOUTH: None,
        EAST: 'town_square',
        WEST: None,
        UP: 'house_63_1',
        DOWN: None,
        GROUND: ['coin', 'apple','chocolate','brigandine'],
        SHOP: [],
        ENEMIES: [],
        SEEN: False,
    },
    'house_63_1': {
        NAME: "House 63's Attic",
        USERDESC: 'You are in a dark, gloomy attic, there is a staircase leading downward.',
        DESC: 'Everything is untouched, covered in dust.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: 'house_63',
        GROUND: ['dagger'],
        SHOP: [],
        ENEMIES: ['spider','spider'],
        SEEN: False,
    },
    'bakery': {
        NAME: 'Bakery',
        USERDESC: 'You are looking at various kinds of delicious pastry, making your stomach growl.',
        DESC: 'The air smells of warm, tasty bread.',
        NORTH: None,
        SOUTH: None,
        WEST: 'town_square',
        EAST: None,
        UP: None,
        DOWN: None,
        GROUND: [],
        SHOP: ['flatbread', 'bread', 'cake'],
        SHOPINTRO: 'The bakery has some freshly baked pastry for sale\n# Have a look:',
        ENEMIES: [],
        SEEN: False,
    },
    'butchery': {
        NAME: 'Butchery',
        USERDESC: "You are at the Butchery's entrance, You observe an old man as he sharpens his knife.",
        DESC: 'The air smells of meat and blood, it is unclean and stinky.',
        NORTH: 'town_square',
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: [],
        SHOP: ['beef', 'sausage'],
        SHOPINTRO: 'The butcher has some cuts ready to go\n# Have a look:',
        ENEMIES: [],
        SEEN: False,
    },
    'courtyard': {
        NAME: 'Courtyard',
        USERDESC: 'You come to a courtyard strewn with flowers, protected by small ornate cast-iron fences.',
        DESC: 'A cardinal sings, sitting atop a distant fence. You faintly make out the smell of bread, and hear voices from the south.',
        NORTH: 'satan_entrance',
        SOUTH: 'town_square',
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['evergreen'],
        SHOP: [],
        ENEMIES: [],
        SEEN: False,
    },
    'satan_entrance': {
        NAME: 'Satan\'s Reach',
        USERDESC: 'You come to a large and forbidding castle made from massive blood colored stones',
        DESC: 'The howling of terrible beasts can be faintly heard within. The smell of decay and feces hangs strong in the air.',
        NORTH: None,
        SOUTH: 'courtyard',
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['sausage'],
        SHOP: None,
        ENEMIES: ['guard','guard'],
        SEEN: False
    },
    'pawn_shop': {
        NAME: 'Goblin Pawn',
        USERDESC: 'You duck under inside of a sewage grate and descend a long and winding tunnel.',
        DESC: 'The tunnel opens into a foul chamber. A goblin in a hat has converted this space into a pawn shop.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: 'town_square',
        DOWN: None,
        GROUND: ['idol'],
        SHOP: ['sword','dagger','brigandine'],
        SHOPINTRO: "Oi-Oi Oi-Oi! Chu Want, Gov?\n<sell>? <buy>?",
        ENEMIES: ['chicken'],
        SEEN: False
    }
}

#for the room code, the first number indicates the number of allowable connections
#the second number indicates the dissalowed connections
ROOMS_TEMPLATE = {
    '5u': {
        NAME: 'Large Cave',
        USERDESC: 'You are in a large cavern, the ceiling above is dripping with unmentionable fluids.',
        DESC: 'A foul wind whistles through the cavern. Black crystals in the wall pulse with an evil light.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['beef','snot'],
        SHOP: [],
        ENEMIES: ['bear','slime'],
        SEEN: False,
    },
    '2': {
        NAME: "Small Cave",
        USERDESC: 'You are in a tiny tunnel. You spot the decayed remains of another adventurer under a pile of rocks.',
        DESC: 'This cave looks like it is going to collapse.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['coin', 'dagger'],
        SHOP: [],
        ENEMIES: [],
        SEEN: False,
    },
    '4ud': {
        NAME: "Medium Cave",
        USERDESC: 'You are in a perfectly cylindrcal cave. It smells like poop and fear. ...Wait, that\'s just you.',
        DESC: 'Rusted cages full of mewling homeless people fill the room. Oil brazers fill the room with smoke and carbonmonoxide',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['flatbread','evergreen'],
        SHOP: [],
        ENEMIES: ['werewolf','alligator'],
        SEEN: False,
    },
    '3ud': {
        NAME: 'Chasm',
        USERDESC: 'You stand at the edge of a vast abyss. A sentient wind, howling with wicked glee attempts to pull you down.',
        DESC: 'The air is charged with evil sorcery.',
        NORTH: None,
        SOUTH: None,
        WEST: None,
        EAST: None,
        UP: None,
        DOWN: None,
        GROUND: [],
        ENEMIES: ['knight','wolf'],
        SHOP: ['sausage','beef','sword'],
        SHOPINTRO: 'The evil wind loots your corpses and tries to resell it TO. YOU.\n# Have a look:',
        SEEN: False,
    },
    '1': {
        NAME: 'Alter',
        USERDESC: 'You come to a dimly lit room full of hellish chanting. A corpse strewn alter brightens one side of the room.',
        DESC: 'A group of children, aged 6 to 10 dance about in mad frenzy. The fattest child, wearing the skin of the town mayor like a robe, slits the throat of what is clearly their parent. They scatter at your approach.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['fountain','idol','dagger'],
        SHOP: [],
        ENEMIES: ['ogre'],
        SEEN: False,
    },
    '6': {
        NAME: 'Ball Room',
        USERDESC: 'You enter the what was once a grand ball room. Now all that remains is ruin.',
        DESC: 'Skellingtons dance in the hall, in mad parody of the dances they danced in life.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: ['goblet','coin','chocolate'],
        SHOP: [],
        ENEMIES: ['skelly','skelly'],
        SEEN: False,
    }
}


PROCGEN_ROOMS = make_dungeon_map('m',ROOMS_TEMPLATE)
PROCGEN_STARTING_POINT = [*PROCGEN_ROOMS][0]
ROOMS.update(PROCGEN_ROOMS)
ROOMS['satan_entrance'][NORTH] = PROCGEN_STARTING_POINT
ROOMS[PROCGEN_STARTING_POINT][SOUTH] = 'satan_entrance'
