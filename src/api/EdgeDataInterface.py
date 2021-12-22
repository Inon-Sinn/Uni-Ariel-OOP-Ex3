import math


class EdgeData:
    global stc  # int
    global dest  # int
    global w  # double
    global id

    def __init__(self, src, dest, w):
        self.src = src
        self.dest = dest
        self.w = w

    def getID(self):
        return self.id

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

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

    def __str__(self):
        ans1 = "src:{src}\ndest:{dest}\nw:{w}\ninfo:{info}\ntag:{tag}\nid:{id}".format \
            (src=self.src, dest=self.dest, w=self.w, info=self.info, tag=self.tag, id=self.id)
        return ans1
