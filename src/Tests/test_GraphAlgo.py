import math
from unittest import TestCase

from src.DiGraph import DiGraph
from src.Graph_Algo import GraphAlgo, BFS, Dijkstra
from src.Algorithms.Minheap import MinHeap

"""Contains the Test Files of GraphAlgo, BFS and Dijkstra"""


class TestGraphAlgo(TestCase):
    """Test File of Graph Algo"""

    def setUp(self) -> None:
        self.Graph = DiGraph()
        self.Graph.add_node(0)
        self.Graph.add_node(1)
        self.Graph.add_node(2, (1, 2, 3))
        self.Graph.add_edge(1, 2, 10)
        self.Graph.add_edge(2, 0, -10)
        self.Graph.add_edge(0, 2, -1)
        self.Graph.add_edge(2, 1, 0)

        self.GraphAlgo = GraphAlgo()
        self.GraphAlgo.graph = self.Graph
        self.graph1 = DiGraph()
        self.graph1.add_node(0)
        self.graph1.add_node(1)
        self.graph1.add_node(2)
        self.graph1.add_node(3)
        self.graph1.add_node(4)
        self.graph1.add_edge(0, 3, 2)
        self.graph1.add_edge(0, 1, 10)
        self.graph1.add_edge(0, 2, 5)
        self.graph1.add_edge(1, 4, 5)
        self.graph1.add_edge(2, 4, 7)
        self.graph1.add_edge(3, 4, 8)
        self.graphalgo = GraphAlgo()

    def setUpJson(self) -> None:
        self.Graph = DiGraph()
        self.assertTrue(self.Graph.add_node(0))
        self.assertTrue(self.Graph.add_node(1))
        self.assertTrue(self.Graph.add_node(2, (1, 2, 3)))
        self.assertTrue(self.Graph.add_node(4))

        self.assertTrue(self.Graph.add_edge(1, 2, 10))
        self.assertTrue(self.Graph.add_edge(2, 0, -10))
        self.assertTrue(self.Graph.add_edge(0, 2, -1))
        self.assertTrue(self.Graph.add_edge(2, 1, 0))

        # for v in self.Graph.get_all_v().values():
        #     print(v)
        self.GraphAlgo = GraphAlgo()

    def test_get_graph(self):
        self.assertEqual(self.GraphAlgo.get_graph().v_size(), 3)
        self.assertEqual(self.GraphAlgo.get_graph().e_size(), 4)
        print("------------------")
        # for v in self.GraphAlgo.get_graph().get_all_v().values():
        #     print(v)

    def test_load_from_json(self):
        self.setUpJson()
        self.Graph.add_node(5, (3, 2, 1))
        self.GraphAlgo.graph = self.Graph
        self.GraphAlgo.save_to_json("Test_Graph")
        self.GraphAlgo.load_from_json("Test_Graph")
        self.assertEqual(self.Graph.v_size(), 5)

    def test_save_to_json(self):
        self.setUpJson()
        self.GraphAlgo.graph = self.Graph
        self.GraphAlgo.save_to_json("Test_Graph")

    def test_shortest_path(self):
        case = 1
        if case == 0:
            dijk = Dijkstra(self.graph1)
            dijk.DijkstraAlgo(0)
            shortestPath = dijk.ShortestPath(0, 4)
            shortestPathTest = [0, 3, 4]
            self.graphalgo.graph = self.graph1
            self.assertEqual((10, shortestPathTest), self.graphalgo.shortest_path(0, 4))

    def test_tsp(self):
        case = 2
        if case == 0:
            cities = [0, 3, 4]
            self.graphalgo.graph = self.graph1
            print(self.graphalgo.TSP(cities))
        elif case == 1:
            if not self.graphalgo.load_from_json("../../data/A1.json"):
                print("File not found!")
                return
        elif case == 2:
            if not self.graphalgo.load_from_json("../../data/A3.json"):
                print("File not found!")
                return

        cities1 = [0, 3, 6]
        cities2 = [10, 6, 7]
        cities3 = [16, 8, 4]
        cities4 = [0, 12, 1]
        print(self.graphalgo.TSP(cities1))
        print(self.graphalgo.TSP(cities2))
        print(self.graphalgo.TSP(cities3))
        print(self.graphalgo.TSP(cities4))

    def test_load(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/A1.json")

    def test_center_point(self):
        case = 1
        if case == 0:
            centers = [(7, 6.806805834715163), (8, 9.925289024973141), (0, 7.819910602212574), (2, 8.182236568942237),
                       (6, 8.071366078651435), (40, 9.291743173960954)]
            for i in range(6):
                currstr = "../../data/A"
                self.graphalgo.load_from_json(currstr + str(i) + ".json")
                curId, curDist = self.graphalgo.centerPoint()
                self.assertEqual(centers[i], (curId, curDist))
                # print(f'centerId IS: {curId}, maxDistance is : {curDist} ')
        if case == 1:
            self.graphalgo.load_from_json("../../data/A2.json")
            dijk = Dijkstra(self.graphalgo.graph)
            dijk.DijkstraAlgo(0)
            curId1, curDist1 = self.graphalgo.centerPoint()
            maxweight = -1
            idmax = -1
            for idNode in dijk.distsFromSrc.keys():
                print(f"for id Node {idNode}, weight is :{dijk.distsFromSrc[idNode]}")
                if dijk.distsFromSrc[idNode] > maxweight:
                    maxweight = dijk.distsFromSrc[idNode]
                    idmax = idNode
            print(f"assigned true is : {maxweight}, id is {idmax}")

    def test_is_connected(self):
        # Normal Graph test
        self.GraphAlgo.get_graph().add_node(4)
        self.assertFalse(self.GraphAlgo.isConnected())
        self.GraphAlgo.get_graph().remove_node(4)
        self.assertTrue(self.GraphAlgo.isConnected())
        self.GraphAlgo.get_graph().remove_edge(2, 1)
        self.assertFalse(self.GraphAlgo.isConnected())
        self.GraphAlgo.get_graph().add_edge(2, 1, 0)
        self.assertTrue(self.GraphAlgo.isConnected())
        self.GraphAlgo.get_graph().remove_node(2)
        self.assertFalse(self.GraphAlgo.isConnected())
        # special Cases
        self.GraphAlgo.graph = DiGraph()
        self.assertTrue(self.GraphAlgo.isConnected())

    def test_reversed_graph(self):
        Reversed = self.GraphAlgo.reversedGraph()
        # Test if we lost any Node or Edges
        self.assertEqual(Reversed.v_size(), self.GraphAlgo.get_graph().v_size())
        self.assertEqual(Reversed.e_size(), self.GraphAlgo.get_graph().e_size())
        # Check if the edges were reversed or not

        # The Real Edge
        self.assertEqual(self.GraphAlgo.get_graph().all_out_edges_of_node(0).get(2), -1)
        # The Reversed Edge
        self.assertEqual(Reversed.all_out_edges_of_node(2).get(0), -1)

        # Print the Reversed Graph if you would like to see with your own eyes
        print("-------The Transposed Graph------")
        for v in Reversed.get_all_v().values():
            print(v)


class TestBFS(TestCase):
    """BFS Algorithm Test File"""

    def setUp(self) -> None:
        algo = TestGraphAlgo()
        algo.setUp()
        algo.GraphAlgo.get_graph().add_node(4)
        self.BFS = BFS(algo.GraphAlgo.get_graph())

    def test_connected(self):
        """There is no need for other Tests Because connected includes them already"""

        self.assertFalse(self.BFS.Connected())
        self.BFS.graph.remove_node(4)
        self.BFS.BFSAlgo()
        self.assertTrue(self.BFS.Connected())
        self.BFS.graph.remove_edge(2, 1)
        self.BFS.BFSAlgo()
        self.assertFalse(self.BFS.Connected())

        # Check an empty Graph
        self.BFS = BFS(DiGraph())
        self.assertTrue(self.BFS.Connected())


class TestDijkstra(TestCase):
    """Dijkstra Algorithm Test File"""

    def setUp(self) -> None:
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 5)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 1, 4)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 1, 2)
        self.d = Dijkstra(g)
        g1 = DiGraph()
        g1.add_node(0)
        g1.add_node(1)
        g1.add_node(2)
        g1.add_node(3)
        g1.add_edge(0, 1, 5)
        g1.add_edge(1, 2, 7)
        g1.add_edge(2, 1, 3)
        g1.add_edge(2, 0, 1)
        g1.add_edge(2, 3, 4)
        g1.add_edge(3, 2, 3)
        self.Dijkstra1 = Dijkstra(g1)
        g2 = DiGraph()
        g2.add_node(0)
        g2.add_node(1)
        g2.add_node(2)
        g2.add_node(3)
        g2.add_node(4)
        g2.add_node(5)
        g2.add_edge(0, 1, 7)
        g2.add_edge(1, 0, 2)
        g2.add_edge(0, 5, 3)
        g2.add_edge(5, 4, 2)
        g2.add_edge(5, 3, 3)
        g2.add_edge(3, 4, 5)
        g2.add_edge(3, 1, 3)
        g2.add_edge(1, 2, 10)
        g2.add_edge(2, 3, 2)
        g2.add_edge(5, 1, 1)
        self.Dijkstra2 = Dijkstra(g2)

    def test_dijkstra_algo(self):
        case = 4
        if case == 0:
            paths = self.d.DijkstraAlgo(0)
            self.assertEqual(paths.get(0), 0)
            self.assertEqual(paths.get(1), 8)
            self.assertEqual(paths.get(2), 5)
            self.assertEqual(paths.get(3), 6)
        elif case == 1:
            paths1 = self.Dijkstra1.DijkstraAlgo(0)
            self.assertEqual(0, paths1.get(0))
            self.assertEqual(5, paths1.get(1))
            self.assertEqual(12, paths1.get(2))
            self.assertEqual(16, paths1.get(3))
        elif case == 2:
            path2 = self.Dijkstra2.DijkstraAlgo(0)
            self.assertEqual(4, path2.get(1))
            self.assertEqual(14, path2.get(2))
            self.assertEqual(6, path2.get(3))
            self.assertEqual(5, path2.get(4))
            self.assertEqual(3, path2.get(5))
        elif case == 3:
            graphAlgo = GraphAlgo()
            graphAlgo.load_from_json("../../data/A0.json")
            dijk3 = Dijkstra(graphAlgo.graph)
            dijk3.DijkstraAlgo(0)
            for dis in dijk3.distsFromSrc.values():
                print(dis)
            print("Passed")
        elif case == 4:
            graphAlgo1 = GraphAlgo()
            graphAlgo1.load_from_json("../../data/A2.json")
            dijk2 = Dijkstra(graphAlgo1.graph)
            dijk2.DijkstraAlgo(0)
            for key in dijk2.distsFromSrc.keys():
                print(f"Key is {key} distance is : {dijk2.distsFromSrc[key]} ")

    def test_shortest_path(self):
        self.fail()

    def test_max_weight(self):
        self.fail()


class TestMinHeap(TestCase):
    def setUp(self) -> None:
        self.g2 = DiGraph()
        self.g2.add_node(0)
        self.g2.add_node(1)
        self.g2.add_node(2)
        self.g2.add_node(3)
        self.g2.add_node(4)
        self.g2.add_node(5)
        self.g2.add_edge(0, 1, 7)
        self.g2.add_edge(1, 0, 2)
        self.g2.add_edge(0, 5, 3)
        self.g2.add_edge(5, 4, 2)
        self.g2.add_edge(5, 3, 3)
        self.g2.add_edge(3, 4, 5)
        self.g2.add_edge(3, 1, 3)
        self.g2.add_edge(1, 2, 10)
        self.g2.add_edge(2, 3, 2)
        self.g2.add_edge(5, 1, 1)
        self.minHeap = MinHeap()
        for i in self.g2.get_all_v().keys():
            self.minHeap.insert(10 - i, self.g2.getNode(i).Id)

    def testInsert(self):
        for node in self.minHeap.heap:
            print(node)

    def testRemoveMin(self):
        for i in range(6):
            print(self.minHeap.removeMin())

    def testDecreaseKey(self):
        self.minHeap.DecreaseKey(3, 1)
        self.minHeap.DecreaseKey(2, 2)
        self.minHeap.DecreaseKey(4, 3)
        self.minHeap.DecreaseKey(1, 4)
        for nodeId in range(6):
            print(self.minHeap.removeMin())

    def testA0(self):
        algo = GraphAlgo()
        algo.load_from_json("../../data/A0.json")
        minHeap1 = MinHeap()
        for node in algo.graph.get_all_v().values():
            if node.Id == 0:
                minHeap1.insert(0, node.Id)
            else:
                minHeap1.insert(math.inf, node.Id)
        minHeap1.removeMin()
        minHeap1.DecreaseKey(1, 1.4)
        minHeap1.DecreaseKey(10, 1.462)
        minHeap1.removeMin()
        minHeap1.DecreaseKey(2, 1.4 + 1.715)
        minHeap1.removeMin()
