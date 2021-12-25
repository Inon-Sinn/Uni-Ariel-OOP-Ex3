from unittest import TestCase

from src.DiGraph import DiGraph


class TestDWGraph(TestCase):

    def setUp(self) -> None:
        self.Graph = DiGraph()

    def test_v_size(self):
        self.assertEqual(self.Graph.v_size(), 0)

    def test_e_size(self):
        self.assertEqual(self.Graph.e_size(), 0)
        self.setUp2()
        self.assertEqual(self.Graph.e_size(), 4)
        self.Graph.remove_edge(4, 5)
        self.assertEqual(self.Graph.e_size(), 4)

        self.Graph.remove_edge(1, 2)
        self.assertEqual(self.Graph.e_size(), 3)

        self.Graph.remove_node(0)
        self.assertEqual(self.Graph.e_size(), 1)

    def setUp2(self):
        """ Used for making it easier to test some od the test"""
        self.assertTrue(self.Graph.add_node(0))
        self.assertTrue(self.Graph.add_node(1))
        self.assertTrue(self.Graph.add_node(2, (1, 2, 3)))
        self.assertTrue(self.Graph.add_node(4))

        self.assertTrue(self.Graph.add_edge(1, 2, 10))
        self.assertTrue(self.Graph.add_edge(2, 0, -10))
        self.assertTrue(self.Graph.add_edge(0, 2, -1))
        self.assertTrue(self.Graph.add_edge(2, 1, 0))

        print(self.Graph.nodes.get(2))

    def test_get_all_v(self):
        self.setUp2()
        self.assertEqual(self.Graph.v_size(), 4)
        for v in self.Graph.get_all_v().values():
            print(v)

    def test_all_in_edges_of_node(self):
        self.setUp2()

        self.assertEqual(len(self.Graph.all_in_edges_of_node(0)), 1)
        self.assertEqual(len(self.Graph.all_in_edges_of_node(2)), 2)
        self.assertEqual(len(self.Graph.all_in_edges_of_node(4)), 0)

        print(self.Graph.all_in_edges_of_node(2))

    def test_all_out_edges_of_node(self):
        self.setUp2()

        self.assertEqual(len(self.Graph.all_out_edges_of_node(0)), 1)
        self.assertEqual(len(self.Graph.all_out_edges_of_node(2)), 2)
        self.assertEqual(len(self.Graph.all_out_edges_of_node(4)), 0)

        print(self.Graph.all_out_edges_of_node(2))

    def test_get_mc(self):
        self.assertEqual(self.Graph.get_mc(), 0)
        self.Graph.add_node(1)
        self.assertEqual(self.Graph.get_mc(), 1)
        self.Graph.add_node(2)
        self.assertEqual(self.Graph.get_mc(), 2)
        self.Graph.add_edge(1, 2, 0)
        self.assertEqual(self.Graph.get_mc(), 3)
        self.Graph.add_edge(2, 2, 0)
        self.assertEqual(self.Graph.get_mc(), 3)
        self.Graph.add_edge(2, 1, 0)
        self.assertEqual(self.Graph.get_mc(), 4)
        self.Graph.add_node(3)
        self.Graph.add_edge(3, 2, 0)
        self.assertEqual(self.Graph.get_mc(), 6)
        self.Graph.remove_edge(3, 2)
        self.assertEqual(self.Graph.get_mc(), 7)
        self.Graph.remove_node(2)
        self.assertEqual(self.Graph.get_mc(), 8)

    def test_add_edge(self):
        self.assertTrue(self.Graph.add_node(0))
        self.assertTrue(self.Graph.add_node(1))
        self.assertTrue(self.Graph.add_node(2, (1, 2, 3)))
        # print(self.Graph.nodes.get(2))

        self.assertFalse(self.Graph.add_edge(3, 4, 1))
        self.assertTrue(self.Graph.add_edge(1, 2, 10))
        self.assertEqual(len(self.Graph.getNode(1).get_All_out_edges()), 1)
        self.assertEqual(len(self.Graph.getNode(2).get_All_in_edges()), 1)
        # print(self.Graph.nodes.get(1))
        # print(self.Graph.nodes.get(2))

        self.assertFalse(self.Graph.add_edge(1, 2, 10))

        self.assertTrue(self.Graph.add_edge(2, 0, -10))
        print(self.Graph.nodes.get(2))

        self.assertTrue(self.Graph.add_edge(0, 2, -1))
        self.assertFalse(self.Graph.add_edge(2, 2, 0))
        self.assertTrue(self.Graph.add_edge(2, 1, 0))
        print(self.Graph.nodes.get(2))

    def test_add_node(self):
        self.Graph.add_node(0)
        self.assertEqual(self.Graph.v_size(), 1)
        print(self.Graph.nodes.get(0))

        self.assertTrue(self.Graph.add_node(1))
        self.assertFalse(self.Graph.add_node(1))
        self.assertEqual(self.Graph.v_size(), 2)

        self.assertTrue(self.Graph.add_node(2, (1, 2, 3)))
        self.assertEqual(self.Graph.getNode(2).pos, (1, 2, 3))
        self.assertEqual(self.Graph.v_size(), 3)
        self.assertEqual(self.Graph.e_size(), 0)
        print(self.Graph.nodes.get(2))

    def test_remove_node(self):
        self.setUp2()
        # Test if we will get false for the wrong Inputs
        self.assertFalse(self.Graph.remove_node(5))

        #Test it the node was removed Correctly
        self.assertTrue(self.Graph.remove_node(4))
        self.assertEqual(self.Graph.v_size(), 3)

        self.assertTrue(self.Graph.remove_node(2))
        self.assertEqual(self.Graph.e_size(), 0)
        self.assertEqual(self.Graph.v_size(), 2)
        for v in self.Graph.get_all_v().values():
            print(v)

    def test_remove_edge(self):
        self.setUp2()
        # Test if we will get false for the wrong Inputs
        self.assertFalse(self.Graph.remove_edge(0, 5))
        self.assertFalse(self.Graph.remove_edge(5, 0))
        self.assertFalse(self.Graph.remove_edge(5, 6))
        self.assertFalse(self.Graph.remove_edge(5, 5))
        self.assertFalse(self.Graph.remove_edge(4, 2))
        self.assertFalse(self.Graph.remove_edge(2, 4))

        # Test if it was Removed Correctly
        print(self.Graph.getNode(0))
        print(self.Graph.getNode(2))
        self.assertTrue(self.Graph.remove_edge(0, 2))
        self.assertEqual(len(self.Graph.getNode(0).get_All_out_edges()), 0)
        self.assertEqual(len(self.Graph.getNode(2).get_All_in_edges()), 1)
        # print(self.Graph.getNode(0))
        # print(self.Graph.getNode(2))
        self.assertTrue(self.Graph.remove_edge(2, 0))
        self.assertEqual(len(self.Graph.getNode(0).get_All_in_edges()), 0)
        self.assertEqual(len(self.Graph.getNode(2).get_All_out_edges()), 1)
        print(self.Graph.getNode(0))
        print(self.Graph.getNode(2))
