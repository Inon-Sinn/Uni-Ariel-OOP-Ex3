import datetime
import time
from src.Graph_Algo import GraphAlgo
from src import DiGraph
from unittest import TestCase


def printTimes(curtime, lastTime, i):
    if 6 > i >= 0:
        print(f"Time for json A{i} is : {lastTime - curtime}")
    elif i == 6:
        print(f"Time for json 1000Nodes is : {lastTime - curtime}")
    elif i == 7:
        print(f"Time for json 10000Nodes is : {lastTime - curtime}")
    elif i == 8:
        print(f"Time for json 100000Nodes is : {lastTime - curtime}")


class TestAlgorithms(TestCase):
    def setUp(self) -> None:
        self.algo = GraphAlgo()
    def switch_json(self, case):
        # run tsp
        if case == 0:
            self.algo.load_from_json("../../data/A0.json")
        elif case == 1:
            self.algo.load_from_json("../../data/A1.json")
        elif case == 2:
            self.algo.load_from_json("../../data/A2.json")
        elif case == 3:
            self.algo.load_from_json("../../data/A3.json")
        elif case == 4:
            self.algo.load_from_json("../../data/A4.json")
        elif case == 5:
            self.algo.load_from_json("../../data/A5.json")
        elif case == 6:
            self.algo.load_from_json("../../data/1000Nodes.json")
        elif case == 7:
            self.algo.load_from_json("../../data/10000Nodes.json")
        elif case == 8:
            self.algo.load_from_json("../../data/100000.json")

    def test_TSP(self):
        print("TSP")
        for i in range(8):
            nodelist = [0, 5, 10, 7, 2]
            self.switch_json(i)
            curtime = int(time.time() * 1000)
            self.algo.TSP(nodelist)
            lastTime = int(time.time() * 1000)
            printTimes(curtime,lastTime,i)

    def test_ShortestPath(self):
        print("Shortest Path")
        for i in range(9):
            self.switch_json(i)
            curtime = int(time.time() * 1000)
            self.algo.shortest_path(0,10)
            lastTime = int(time.time() * 1000)
            printTimes(curtime,lastTime,i)


    def test_centerPoint(self):
        print("Center Point")
        for i in range(8):
            self.switch_json(i)
            curtime = int(time.time() * 1000)
            self.algo.centerPoint()
            lastTime = int(time.time() * 1000)
            printTimes(curtime,lastTime,i)

    def test_isConnected(self):
        print("isConnected:")
        for i in range(6):
            self.switch_json(i)
            curtime = int(time.time() * 1000)
            self.algo.isConnected()
            lastTime = int(time.time() * 1000)
            printTimes(curtime,lastTime,i)

    def test_load(self):
        print("Load Json python")
        for i in range(9):
            curtime = int(time.time() * 1000)
            self.switch_json(i)
            lastTime = int(time.time() * 1000)
            printTimes(curtime,lastTime,i)

    def testSave(self):
        print("Save to json python")
        for i in range(9):
            self.switch_json(i)
            curtime = int(time.time() * 1000)
            self.algo.save_to_json(f'test{i}')
            lastTime = int(time.time() * 1000)
            printTimes(curtime,lastTime,i)
