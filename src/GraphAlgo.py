import json
import math
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from queue import Queue
import heapq


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = None

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        try:  # Checks if the file even Exists
            with open(file_name, "r+") as f:
                fromJson = json.load(f)
                for n in fromJson['Nodes']:
                    try:  # In case we are not given a position
                        pos = tuple(float(s) for s in n['pos'].split(','))
                        graph.add_node(n['id'], pos)
                    except KeyError:
                        graph.add_node(n['id'])
                for e in fromJson['Edges']:
                    graph.add_edge(e['src'], e['dest'], e['w'])
        except IOError as err:
            print(err)
            return False

        self.graph = graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        # Checks the Input
        if file_name is None:
            return False
        ToJson = {'Edges': [], 'Nodes': []}
        for src in self.graph.get_all_v().values():
            for dest in src.all_out_edges.items():
                ToJson['Edges'].append({
                    'src': src.Id,
                    'w': dest[1],
                    'dest': dest[0]
                })
        for n in self.graph.nodes.values():
            if n.pos is None:
                ToJson['Nodes'].append({
                    'id': n.Id
                })
            else:
                ToJson['Nodes'].append({
                    'pos': ','.join(map(str, n.pos)),
                    'id': n.Id
                })
        try:
            with open(file_name, 'w') as outfile:
                json.dump(ToJson, outfile, indent=4)
                return True
        except TypeError:  # Should not happen but in case the Graph itself has a problem
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dijkstra = Dijkstra()
        paths = dijkstra.DjkstraAlgo(id1)
        if paths.get(id2) is math.inf:
            return float('inf'), []
        return paths.get(id2), dijkstra.ShortestPath(id1, id2)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        if self.isConnected is False:  # TODO check if returning None is correct in case that there is no Center
            return None  # next(iter(self.graph.get_all_v().keys())),math.inf
        super().centerPoint()

    def plot_graph(self) -> None:
        pass

    def isConnected(self) -> bool:
        """An auxiliary function for center Point, Checks if the given Graph is Connected"""
        if len(self.graph.get_all_v()) != 0:
            firstRun = BFS(self.graph)
            if firstRun.Connected() is False:
                return False
            SecondRun = BFS(self.reversedGraph())
            if SecondRun.Connected() is False:
                return False
        return True

    def reversedGraph(self) -> DiGraph:
        """Return the Reverse Graph of the algorithms Graph"""
        Reversed = DiGraph()
        # Add all the node to the Reverse Graph
        for node in self.graph.get_all_v().values():
            Reversed.add_node(node.Id, node.pos)
        # Add all the edges to the Reverse Graph
        for node_id in self.graph.get_all_v().keys():
            for edge in self.graph.all_out_edges_of_node(node_id).items():
                Reversed.add_edge(node_id, edge[0], edge[1])
        return Reversed


class BFS:
    """This Class implements the BFS Algorithm,"""

    def __init__(self, graph):
        """
        Run the BFS Algorithm
        :param graph: a Graph that implements the GraphInterface
        """
        self.graph = DiGraph()
        self.Q = Queue(0)  # TODO check that 0 is infinite in help()
        self.d = {}
        self.prev = {}  # TODO could be deleted if there is no use for it
        # constants
        self.white = 0
        self.gray = 1
        self.black = 2

        Id = next(iter(self.graph.get_all_v().keys()))  # TODO check if it works
        if Id is not None:
            self.BFSAlgo(Id)

    def BFSAlgo(self, node_id):
        """The BFS algorithm, the input is the id of a node from which the Algorithm will start"""
        for node in self.graph.get_all_v().values():
            node.tag = self.white
            self.prev[node.Id] = None
        self.graph.getNode(node_id).tag = self.gray
        self.d[node_id] = 0
        self.Q.put(node_id)
        while self.Q.empty is False:
            self.BFS_VISIT(self.Q.get_nowait())

    def BFS_VISIT(self, node_id):
        """Used By the BFS Algorithm, Goes over all the siblings of the given Node and adds them to the Queue if they
        were not visited before( color white) """
        currNode = self.graph.getNode(node_id)
        for other_Node_id in currNode.get_All_out_edges():
            outNode = self.graph.getNode(other_Node_id)
            if outNode.tag == self.white:
                outNode.tag = self.gray
                self.d[other_Node_id] = self.d.get(node_id) + 1
                self.prev[other_Node_id] = node_id
                self.Q.add(other_Node_id)
        currNode.tag = self.black

    def Connected(self):
        """An Auxiliary Function used to check if the given Graph is connected"""
        for node in self.graph.get_all_v().values():
            if node.tag == self.white:
                return False
        return True


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.MinHeap = []
        self.d = {}
        self.prev = {}

    def DjkstraAlgo(self, start_id) -> dict:
        """
        The Dijkstra algorithm
        :param start_id: the id of the node on which the Dijkstra algorithm will run
        :return: dict - A dict with the weight of the shortest path for every node from the given starting node
        """
        # Iterating through all the nodes and setting their weights to infinity
        for node_id in self.graph.get_all_v():
            self.d[node_id] = math.inf
            self.prev[node_id] = None
        self.d[start_id] = 0
        heapq.heappush(self.MinHeap, start_id)
        while len(self.MinHeap) != 0:
            next_id = heapq.heappop(self.MinHeap)
            for edge in self.graph.all_out_edges_of_node(next_id).items():
                self.relax(next_id, edge[0], edge[1])
        return self.d

    def relax(self, src, dest, weight):
        """
        Relax, used be the Dijkstra algorithm,
        The Input is a Edge
        :param src: the id of the source node
        :param dest: the id of the destination node
        :param weight: the weight of the edge
        """
        if self.d.get(dest) > (self.d.get(src) + weight):
            for node_id in self.MinHeap:  # TODO takes O(n) implement MinHeap to make it log(n)
                if self.MinHeap[node_id] == dest:
                    self.MinHeap[node_id] = self.d.get(src) + weight
                    heapq.heapify(self.MinHeap)
                    self.prev[dest] = src
                    break

    def ShortestPath(self, src, dest) -> list:
        """
        An Auxiliray function that Return the shortest path between 2 given nodes in a form of a list
        :param src: the id of the starting node
        :param dest: the id of the end node
        :return: list - the shotest path between the two nodes (them included)
        """
        Q = Queue(0)
        Q.put(dest)
        cur = dest
        while self.prev.get(cur) is not src:
            Q.put(self.prev.get(cur))
            cur = self.prev.get(cur)
        path = [src]
        while Q.empty() is False:
            path.append(Q.get_nowait())
        return path