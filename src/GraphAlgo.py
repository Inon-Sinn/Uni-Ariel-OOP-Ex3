import json
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from queue import Queue


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
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass


class BFS:
    """This Class implements the BFS Algorithm,"""

    def __init__(self, graph, id):
        """
        Run the BFS Algorithm
        :param graph: a Graph that implements the GraphInterface
        :param id: id of the Node from which the algorithms should start
        """
        self.graph = DiGraph()
        self.Q = Queue(0)  # TODO check that 0 is infinite in help()
        self.d = {}
        self.prev = {}
        # constants
        self.white = 0
        self.gray = 1
        self.black = 2

        self.BFS(id)

    def BFS(self, node_id):
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

    def __init__(self, graph, startID):
        # this dijkstra uses minq as implementation for pq
        self.graph = graph
        self.prioQ = []
        startNode = graph.get_all_v.get(startID)
        # iterating through all the nodes and setting their weights to infinity
