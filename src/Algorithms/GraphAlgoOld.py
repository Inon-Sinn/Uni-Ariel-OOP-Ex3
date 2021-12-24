import json
from typing import List
from src.GraphInterface import GraphInterface


class GraphAlgo:

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        raise NotImplementedError

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        raise NotImplementedError

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError


class GraphAlgo(GraphAlgo):
    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        file_name = "A0.json"  # ?
        g = self.load_from_json(file_name)

    def load_from_json(self, file_name: str) -> bool:
        graph = GraphInterface.DiGraph()
        try:
            with open(file_name, "r+") as f:
                fromJson = json.load(f)
                # g = graph
                for n in fromJson['nodes']:
                    # nodeFromJson = node.NodeData(id=n["id"], pos=n["pos"])
                    graph.add_node(n["id"], n["pos"])
                for e in fromJson['edges']:
                    # edgeFromJson = edge.EdgeData(src=e["src"], dest=e["dest"], w=e["w"])
                    graph.add_edge(e["src"], e["dest"], e["w"])
                return True
        except IOError as err:
            print(err)
            return False

    def save_to_json(self, file_name: str) -> bool:
        graph = GraphInterface.DWGraph()
        ToJson = {}
        ToJson['edges'] = []

        for e in graph.edges:
            ToJson['edges'].append({
                'src': graph.edges.get(e).getSource,
                'w': graph.edges.get(e).getWeight,
                'dest': graph.edges.get(e).getDestination
            })
        for n in graph.nodes:
            ToJson['nodes'].append({
                'pos': graph.nodes.get(n).pos,
                'id': graph.nodes.get(n).id,
            })

        with open(file_name, 'w') as outfile:
            json.dump(ToJson, outfile)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        #DijkstraAlgo.dijkstra(id1)
        raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        raise NotImplementedError