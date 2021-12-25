import json
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import Lib.queue as queue


class DWGraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = None

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        try:
            with open(file_name, "r+") as f:
                fromJson = json.load(f)
                for n in fromJson['Nodes']:
                    try:
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
        graph = GraphInterface.DWGraph()
        ToJson = {'Edges': [], 'Nodes': []}

        for src in graph.nodes:
            for dest in src.all_out_edges.items:
                ToJson['Edges'].append({
                    'src': src,
                    'w': dest[1],
                    'dest': dest[0]
                })
        for n in graph.nodes:
            ToJson['nodes'].append({
                'pos': n.pos,
                'id': n.id
            })

        with open(file_name, 'w') as outfile:
            json.dump(ToJson, outfile)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass

class BFS:
    def __init__(self, graph, idOfStart):
        self.Q = queue()
        self.d = {}
        self.prev = {}
        # constants
        self.white = 0
        self.grey = 1
        self.black = 2
        ## initialize the graph
        self.graph = DiGraph()
        for node in graph.get_all_v():
            newnode = node.copy()
            newnode.tag = self.white
            self.graph = newnode
        self.d[idOfStart] = 0
        self.Q.put(idOfStart)

#
# Used by the BFS algorithm
# goes over all the sibling of a node and adds them to the Queue if they have the color white
# @param currentVisitNode int - the id of the node for which we used this function
#
    def BFS_VISIT(self, currentVisitNode):
        currNode = self.graph.getNode(currentVisitNode)
        for outNode in currNode.get_All_out_edges().keys():
            if(outNode.tag == self.white):
                outNode.tag = self.gray
                self.d[outNode.id] = self.d.get(currNode.id) +1
                self.prev[outNode.id] = currNode.id
                self.Q.add(outNode.id)
        currNode.tag = self.black
    # An Auxiliary function used to check if the graph is connected
    # @return boolean -True: the graph is connected, False: the graph isn't connected
    #

    def Connected(self):
        for node in self.graph:
            if(node.tag == self.white):
                return False
        return True

class Dijkstra:

    def __init__(self, graph, startID):
        # this dijkstra uses minq as implementation for pq
        self.graph = graph
        self.prioQ = []
        startNode = graph.get_all_v.get(startID)
        # iterating through all the nodes and setting their weights to infinity




