from src.GraphInterface import GraphInterface


class DWGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.EdgeSize = 0
        self.nodes = {}  # dictionary with all the Nodes

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.EdgeSize

    def get_all_v(self) -> dict:
        return self.nodes  # check how to use dict.items()

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).getEdges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).edgesConnected

    def get_mc(self) -> int:
        raise NotImplementedError

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        raise NotImplementedError

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        raise NotImplementedError

    def remove_node(self, node_id: int) -> bool:
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        raise NotImplementedError
