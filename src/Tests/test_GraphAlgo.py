from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.Graph = DiGraph()
        self.assertTrue(self.Graph.add_node(0))
        self.assertTrue(self.Graph.add_node(1))
        self.assertTrue(self.Graph.add_node(2, (1, 2, 3)))
        self.assertTrue(self.Graph.add_node(4))

        self.assertTrue(self.Graph.add_edge(1, 2, 10))
        self.assertTrue(self.Graph.add_edge(2, 0, -10))
        self.assertTrue(self.Graph.add_edge(0, 2, -1))
        self.assertTrue(self.Graph.add_edge(2, 1, 0))

        for v in self.Graph.get_all_v().values():
            print(v)
        self.GraphAlgo = GraphAlgo()
        self.GraphAlgo.graph = self.Graph

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

        for v in self.Graph.get_all_v().values():
            print(v)
        self.GraphAlgo = GraphAlgo()

    def test_get_graph(self):
        self.assertEqual(self.GraphAlgo.get_graph().v_size(), 4)
        self.assertEqual(self.GraphAlgo.get_graph().e_size(), 4)
        print("------------------")
        for v in self.GraphAlgo.get_graph().get_all_v().values():
            print(v)

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
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def test_is_connected(self):
        self.fail()

    def test_reversed_graph(self):
        Reversed = self.GraphAlgo.reversedGraph()
        # Test if we lost any Node or Edges
        self.assertEqual(Reversed.v_size(), self.GraphAlgo.get_graph().v_size())
        self.assertEqual(Reversed.e_size(), self.GraphAlgo.get_graph().e_size())




class TestBFS(TestCase):
    def test_bfsalgo(self):
        self.fail()

    def test_bfs_visit(self):
        self.fail()

    def test_connected(self):
        self.fail()


class TestDijkstra(TestCase):
    def test_djkstra_algo(self):
        self.fail()

    def test_relax(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_max_weight(self):
        self.fail()