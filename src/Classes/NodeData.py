import math


class NodeData:
    global id  # int
    global pos  # string
    global geoLoc  # geoLoc
    edgesConnected = {}  # dicionary/map
    pointingToMe = []  # list
    global info  # String
    weight = math.inf
    tag = 0

    def __init__(self, id, geoLoc):
        self.pos = ""
        self.id = id
        self.geoLoc = geoLoc
        self.edgesConnected = {}
        self.info = "unmarked node";

    def getKey(self):
        return self.id

    def getLocation(self):
        return self.geoLoc

    def setLocation(self, Loc):
        self.geoLoc = Loc

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

    def getZ(self):
        return self.z

    def getDistance(self, g):
        return math.sqrt(math.pow(g.x - self.x, 2) + math.pow(g.y - self.y, 2) + math.pow(g.z - self.z, 2))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

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
        ans1 = "id:{id}\nweight:{weight}\ngeoLoc:{geoLoc}\nedges:{edges}" \
               "\npointers:{pointers}\nid:{id}\ninfo:{info}\n" \
               "tag:{tag}".format \
            (id=self.id, weight=self.weight, geoLoc=self.geoLoc,
             edges = self.edgesConnected, pointers = self.pointingToMe,
             info=self.info, tag=self.tag)
        return ans1

    def compareTo(self, node):
        if node == None:
            return -1
        if self.weight < node.weight:
            return -1
        if self.weight > node.weight:
            return 1
        return 0
