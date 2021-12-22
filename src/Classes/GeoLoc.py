import math


class GeoLoc:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getDistance(self, g):
        return math.sqrt(math.pow(g.x - self.x, 2) + math.pow(g.y - self.y, 2) + math.pow(g.z - self.z, 2))

    def __str__(self):
        ans1 = "x:{x}\ny:{y}\nz:{z}".format(x=self.x, y=self.y, z=self.z)
        return ans1
