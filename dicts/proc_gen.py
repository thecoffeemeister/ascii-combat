from random import randrange
from random import choice
from dicts import *

#upgrade: enforce realistic-ish geometry, maybe... (on a related note, no way to escape proc_gen map)
#ALL HAIL THE GREAT OLD ONES ^(;,;)^
#                              {|}
class Graph:
    #creates a graph with a set number of nodes, completely disconected, the default node val is 0
    def __init__(self,nodes:int):
        if nodes > 0:
            self.pathMat = [[0 for i in range(nodes)] for j in range(nodes)]
            self.numNodes = nodes
            self.nodeVals = [0 for i in range(nodes)]
            self.nodeIDs = [i for i in range(nodes)]
        else:
            self.pathMat = []
            self.numNodes = 0
            self.nodeVals = []

    #allows len to be used on this class
    def __len__(self):
        return self.numNodes

    #iterates over the nodes [0] and the associated paths with each node [1]
    #as well as the id of each node [2]
    def __iter__(self):
        nodind = []
        for i in range (self.numNodes):
            nodind.append([self.nodeVals[i],self.pathMat[i],self.nodeIDs[i]])
        return iter(nodind)

    #add a path between two nodes, with a weight of inpath, defaults to 1
    def addPath(self,i,j,inpath = 1):
        if self.pathMat != []:
            if (i >= 0) and (j >= 0):
                if (i < self.numNodes) and (j < self.numNodes):
                    self.pathMat[i][j] = inpath

    #get the connection between two nodes, 0 is no connection
    def getPath(self,i,j):
        if self.pathMat != []:
            if (i >= 0) and (j >= 0):
                if (i < self.numNodes) and (j < self.numNodes):
                    return self.pathMat[i][j]
        return None

    #store data inside of a node
    def addNodeVal(self,i,inVal,ident=0):
        if (i >= 0) and (i < self.numNodes):
            self.nodeVals[i] = inVal
            self.nodeIDs[i] = ident

    #fetch the data from a node
    def getNodeVal(self,i):
        if (i >= 0) and (i < self.numNodes):
            return self.nodeVals[i]
        else:
            return None

    #fetches the id of the node
    def getNodeID(self,i):
        if (i >= 0) and (i < self.numNodes):
            return self.nodeIDs[i]
        else:
            return None

#applies random.choice to dictionaries
def dchoice(indict):
    thech = choice([dcho for dcho in range(len(indict))])
    cholito = list (indict)
    cholo = cholito[thech]
    return (indict[cholo],cholito[thech])

#procedurally generates a version of the dungeon map, storing it in a graph.
#Should not be used top level, for use with make_dungeon_map
#issues?: cthonic geometry (one way paths, divergent paths leading to the same room
#rents in the fabric of space time, dead ends, etc)
def make_dungeon_graph(rooms:int,roomTypes):
    dungeonMap = Graph(rooms)
    for i in range(rooms):
        randochoice = dchoice(roomTypes)
        dungeonMap.addNodeVal(i,randochoice[0],randochoice[1] + str(i))
        for j in range(rooms):
            randomRoom = randrange(rooms)
            for k in range (randrange(6) + 1):
                if (dungeonMap.getPath(j,randomRoom) == 0) and (choice([False,True])):
                    dungeonMap.addPath(j,randomRoom,choice([NORTH,SOUTH,EAST,WEST,UP,DOWN]))
    return dungeonMap

#makes a procedurally generated dungeon using room templates
#update:procedurally generate enemies and drops, don't simply rely on templates only
def make_dungeon_map(dunSize, roomTypes):
    if dunSize == 'b':
        dunSize = 50
    elif dunSize == 'm':
        dunSize = 25
    else:
        dunSize = 10
    dungeonGraph = make_dungeon_graph(dunSize,roomTypes)
    dungeonList = []
    for room in dungeonGraph:
        roomKey = room[2]
        roomList = [(NAME      ,room[0][NAME]),
                    (USERDESC  ,room[0][USERDESC]),
                    (DESC      ,room[0][DESC]),
                    (GROUND    ,room[0][GROUND]),
                    (SHOP      ,room[0][SHOP]),
                    (ENEMIES   ,room[0][ENEMIES]),
                    (SEEN      ,room[0][SEEN])]
        if SHOPINTRO in room[0]:
            roomList.append((SHOPINTRO ,room[0][SHOPINTRO]))
        for i in range(len(room[1])):
            if room[1][i] != 0:
                roomList.append((room[1][i],dungeonGraph.getNodeID(i)))
        roomData = dict(roomList)
        if not (NORTH in roomData):
            roomData.update({NORTH:None})
        if not (SOUTH in roomData):
            roomData.update({SOUTH:None})
        if not (EAST in roomData):
            roomData.update({EAST:None})
        if not (WEST in roomData):
            roomData.update({WEST:None})
        if not (UP in roomData):
            roomData.update({UP:None})
        if not (DOWN in roomData):
            roomData.update({DOWN:None})
        dungeonList.append((roomKey,roomData))
    dungeonMap = dict(dungeonList)
    return dungeonMap
