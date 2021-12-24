from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Graph import DWGraph
import Lib.queue as queue


class DWGraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = None

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        graph = DWGraph()
        self.graph = graph
        return False

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass

class BFS:
    def __init__(self, graph, s):
        self.graph = DWGraph()
        # make a deep copy
        for node in graph:
            self.graph.add_node(node)
            for node1 in node.all_out_edges
        self.Q = queue()
        self.d = {}
        self.prev = {}
        self.white = 0
        self.grey = 1
        self.black = 2



class Dijkstra:

class MinHeap:
