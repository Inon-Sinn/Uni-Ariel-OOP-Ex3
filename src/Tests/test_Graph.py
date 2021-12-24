from unittest import TestCase

from src.Graph import DWGraph


class TestDWGraph(TestCase):

    def setUp(self) -> None:
        self.Graph = DWGraph()

    def test_v_size(self):
        self.assertEqual(self.Graph.v_size(), 0)

    def test_e_size(self):
        self.assertEqual(self.Graph.e_size(), 0)

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        self.assertEqual(self.Graph.get_mc(), 0)

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
