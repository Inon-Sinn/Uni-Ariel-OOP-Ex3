from src.api import EdgeDataInterface
from src.api import NodeDataInterface


class GraphInterface:
    """This abstract class represents an interface of a graph."""

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        pass

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        pass

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        pass

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        pass

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        pass

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        >>> add_edge(1,1,1)
        True
        """
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        pass

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        pass


class DiGraph(GraphInterface):
    mc = 0  # int
    nodes = {}  # dicionary/map
    edges = {}  # dicionary/map

    def __init__(self):
        self.nextKeyEdge = 0
        self.nodes = {}
        self.edges = {}

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).pointingToMe

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).edgesConnected

    def get_mc(self) -> int:
        raise NotImplementedError

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        e = EdgeDataInterface.EdgeData(id1, id2, weight)
        if e in self.edges:
            return False
        if len(self.edges) == 0:
            self.edges[0] = e
            self.nodes.get(id1).addEdge(e)
            self.nodes.get(id2).addPointers(id1)
        else:
            self.edges[len(self.edges) - 1] = e
            self.nodes.get(id1).addEdge(e)
            if self.nodes.get(id2) != None:
                self.nodes.get(id2).addPointers(id1)
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        n = NodeDataInterface.NodeData(node_id, pos)
        if n in self.nodes:
            return False
        self.nodes[len(self.nodes) - 1] = n
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.get(node_id) not in self.nodes:
            return False
        self.nodes.pop(node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        for i in self.edges:
            if self.edges.get(i).getSource != node_id1 or self.edges.get(i).getDestination != node_id2:
                return False
            else:
                self.edges.pop(i)
        return False


