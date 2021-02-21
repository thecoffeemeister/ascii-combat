from random import randrange
from random import choice
from dicts import *

#upgrade: enforce realistic-ish geometry, maybe...
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
            self.coords = [None for i in range(nodes)]
        else:
            self.pathMat = []
            self.numNodes = 0
            self.nodeVals = []
            self.coords = []

    #allows len to be used on this class
    def __len__(self):
        return self.numNodes

    #iterates over the nodes [0] and the associated paths with each node [1]
    #as well as the id of each node [2]...also coordinates[3]
    def __iter__(self):
        nodind = []
        for i in range (self.numNodes):
            nodind.append((self.nodeVals[i],self.pathMat[i],self.nodeIDs[i],self.coords[i]))
        return iter(nodind)

    #add a path between two nodes, with a weight of inpath, defaults to 1
    #the coords are just there to help the graph generator
    def addPath(self,i,j,inpath,coord1,coord2):
        if self.pathMat != []:
            if (i >= 0) and (j >= 0):
                if (i < self.numNodes) and (j < self.numNodes):
                    self.pathMat[i][j] = inpath
                    self.coords[i] = coord1
                    self.coords[j] = coord2

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

    #fetches the coordinate value for a node
    def getCoord(self,i):
        if (i >= 0) and (i < self.numNodes):
            return self.coords[i]
        else:
            return None

#applies random.choice to dictionaries
def dchoice(indict):
    thech = choice([dcho for dcho in range(len(indict))])
    dicklist = list (indict)
    dickkey = dicklist[thech]
    dickval = indict[dickkey]
    return (dickkey,dickval)

def inverseCardinal(cardinal):
    if cardinal == NORTH:
        return SOUTH
    elif cardinal == SOUTH:
        return NORTH
    elif cardinal == WEST:
        return EAST
    elif cardinal == EAST:
        return WEST
    elif cardinal == UP:
        return DOWN
    else:
        return UP

#procedurally generates a version of the dungeon map, storing it in a graph.
#Should not be used top level, for use with make_dungeon_map
def make_dungeon_graph(rooms:int,roomTypes):
    dungeonGraph = Graph(rooms)
    currcoord = [0,0,0]
    nextcoord = None
    badcoords = False
    for i in range(len(dungeonGraph)):
        randomroom = dchoice(roomTypes)
        dungeonGraph.addNodeVal(i,randomroom[1],randomroom[0] + str(i))
    for i in range(len(dungeonGraph)):
        if dungeonGraph.coords[i] == None:
            dungeonGraph.coords[i] = currcoord
        #change randrange 6 to a number based on room description
        directioncode = randomroom[0]
        for j in range(int(directioncode[0])):
            randomdir = (choice([0,1,2]),choice([1,-1]))
            if randomdir[0] == 0:
                cardinal = NORTH if randomdir == 1 else SOUTH
            if randomdir[1] == 1:
                cardinal = WEST if randomdir == 1 else EAST
            else:
                cardinal = UP if randomdir == 1 else DOWN
            nextcoord = None
            nexti = None
            for k in range(len(dungeonGraph)):
                nextcoord = dungeonGraph.coords[k]
                nexti = k
                if nextcoord == None:
                    break
            if nextcoord == None:
                nextcoord = [currcoord[0],currcoord[1],currcoord[2]]
                nextcoord[randomdir[0]] += randomdir[1]
            else:
                badcoords = True
                while badcoords:
                    nexti = randrange(len(dungeonGraph))
                    nextcoord = dungeonGraph.coords[nexti]
                    coordist = [currcoord[0]-nextcoord[0],currcoord[1]-nextcoord[1],currcoord[2]-nextcoord[2]]
                    coordist = [abs(coordist[0]),abs(coordist[1]),abs(coordist[2])]
                    coordist = coordist[0] + coordist[1] + coordist[2]
                    badcoords = (currcoord == nextcoord) or (coordist > (len(dungeonGraph) / 3))
            for dirc in directioncode:
                if (dirc == 'n') and cardinal == NORTH:
                    badcoords = True
                if (dirc == 's') and cardinal == SOUTH:
                    badcoords = True
                if (dirc == 'e') and cardinal == EAST:
                    badcoords = True
                if (dirc == 'w') and cardinal == WEST:
                    badcoords = True
                if (dirc == 'u') and cardinal == UP:
                    badcoords = True
                if (dirc == 'd') and cardinal == DOWN:
                    badcoords = True
            if not badcoords:
                dungeonGraph.addPath(i,nexti,cardinal,currcoord,nextcoord)
                dungeonGraph.addPath(nexti,i,inverseCardinal(cardinal),nextcoord,currcoord)
                currcoord = nextcoord
    return dungeonGraph

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
