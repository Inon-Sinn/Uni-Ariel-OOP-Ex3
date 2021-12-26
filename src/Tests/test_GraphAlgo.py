from unittest import TestCase
import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def setUp(self) -> None:
        self.graphAlgo = GraphAlgo.GraphAlgo()
        self.datapath = "Uni-Ariel-OOP-Ex3/data"
        # example file is A1.json the first 5 nodes and edges
        self.positions = [(35.18753053591606, 32.10378225882353, 0.0), (35.18958953510896, 32.10785303529412, 0.0),
                          (35.19341035835351, 32.10610841680672, 0.0), (35.197528356739305, 32.1053088, 0.0),
                          (35.2016888087167, 32.10601755126051, 0.0)]
        self.ids = [0, 1, 2, 3, 4]
        self.SRCs = [0, 0, 1, 1, 2]
        self.DESTs = [1, 10, 0, 2, 1]
        self.weights = [1.4004465106761335, 1.4620268165085584, 1.8884659521433524, 1.7646903245689283
            , 1.7155926739282625]

    def testLoadFromJson(self):
        graph = DiGraph.DiGraph()

        for i in range(5):
            graph.add_node(self.ids[i], self.positions[i])
            graph.add_edge(self.SRCs[i], self.DESTs[i], self.weights[i])
        for i in range(1):
            jsonPath = self.datapath + 'Test' + str(i + 1)
            self.graphAlgo.load_from_json(jsonPath)
            for node in self.graphAlgo.graph.get_all_v().values():
                # assume the iterator passes orderwise (just a joke not really depending on that)
                self.assertEqual(node == graph.getNode(node.Id), True)
                # after checking each node its certain that all the edges are identical sense they are objects
                # inside the node, therefore __equal__ takes care of that

    def testSaveToJson(self):
        graph = DiGraph.DiGraph()
        pathname = "testSave.json"
        for i in range(5):
            graph.add_node(self.ids[i], self.positions[i])
            graph.add_edge(self.SRCs[i], self.DESTs[i], self.weights[i])

        case = 0
        # case = 0 check by load and then save
        # case = 1 check visually, if not sure about the load function
        if case == 0:
            try:
                self.graphAlgo.graph = graph
                self.graphAlgo.save_to_json(pathname)
                self.graphAlgo.load_from_json(pathname)
                for node in self.graphAlgo.graph.get_all_v().values():
                    self.assertEqual(node == graph.getNode(node.Id), True)
            except IOError:
                self.fail("File Not Found")
            except KeyError:
                self.fail("Position is not given")
            # nodes or edges objects are not correct in graph for some reason
            except TypeError:
                self.fail("Graph has a problem")
        elif case == 1:
            try:
                self.graphAlgo.graph = graph
                self.graphAlgo.save_to_json(pathname)
            except IOError:
                self.fail("File Not Found")
            except KeyError:
                self.fail("Position is not given")

    # def TestDijkstra(self):
