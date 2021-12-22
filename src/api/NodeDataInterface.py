import math


class NodeData:
    global id  # int
    pos = {}  # geoLoc
    edgesConnected = {}  # dicionary/map
    pointingToMe = []  # list

    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        self.edgesConnected = {}

    def getKey(self):
        return self.id

    def getLocation(self):
        return self.pos

    def setLocation(self, x, y, z):
        self.pos = {x, y, z}

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getTag(self):
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def getEdge(self, dest):
        return self.edgesConnected.get(dest)

    def getDistance(self, g):
        return math.sqrt\
            (math.pow(g.x - self.pos[0], 2) +
             math.pow(g.y - self.pos[1], 2) + math.pow(g.z - self.pos[2], 2))

    def getNodeX(self):
        return self.pos[0]

    def getNodeY(self):
        return self.pos[1]

    def getNodeZ(self):
        return self.pos[2]

    def removeEdge(self, dest):
        self.edgesConnected.pop(dest)

    def addEdge(self, e): #edgeData
        self.edgesConnected[e.getDest] = e

    def getPointers(self):
        return self.pointingToMe

    def addPointers(self, src):
        if src not in self.pointingToMe:
            self.pointingToMe.append(src)

    def removePointers(self, src):
        self.pointingToMe.pop(src)

    def __str__(self):
        ans1 = "id:{id}\nweight:{weight}\npos:{pos}\nedges:{edges}" \
               "\npointers:{pointers}\nid:{id}".format \
            (id=self.id, weight=self.weight, pos=self.pos,
             edges = self.edgesConnected, pointers = self.pointingToMe)
        return ans1

    def compareTo(self, node):
        if node == None:
            return -1
        if self.weight < node.weight:
            return -1
        if self.weight > node.weight:
            return 1
        return 0
