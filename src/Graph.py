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
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).get_All_in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).get_All_out_edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes.get(id1) is None or self.nodes.get(id2) is None:
            return False
        src = self.nodes.get(id1)
        dest = self.nodes.get(id2)
        if src.all_out_edges[id2] is None and dest.all_in_edges[id1] is None:
            src.add_Out_edge(id2, weight)
            dest.add_In_edge(id1, weight)
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """Return False in the Case the node already exists"""
        # TODO check if its right and other options for sending False
        if self.nodes.get(node_id) is None:
            newNode = Node(node_id, pos)
            self.nodes[node_id] = newNode
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        removedNode = self.nodes.pop(node_id)
        if removedNode is None:
            return False  # TODO check if i should return False if the id does not exist
        for dest in removedNode.remove_Out_edge():
            self.remove_edge(node_id, dest)
        for src in removedNode.get_All_in_edges():
            self.remove_edge(src, node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.nodes.get(node_id1) is None or self.nodes.get(node_id2) is None:
            return False
        src = self.nodes.get(node_id1)
        if src.remove_Out_edge(node_id2) is None:
            return False
        dest = self.nodes.get(node_id2)
        if dest.remove_In_edge(node_id1) is None:
            return False
        return True
    def getNode(self, id):
        return self.nodes.get(id)
    def popNode(self, id):
        return self.nodes.pop(id)
    def addNode(self, key, value):
        self.nodes[key] = value

class Node:

    def __init__(self, Id, pos):
        self.Id = Id
        self.tag = -1
        self.pos = pos  # Need to get Tuple of the pos, build it when we get the json
        # The edges which destination is this node, key: source node id, value: weight of the edge
        self.all_in_edges = {}
        # The edges which source is this node, key: destination node id, value: weight of the edge
        self.all_out_edges = {}

    def get_All_in_edges(self):
        return self.all_in_edges

    def get_All_out_edges(self):
        return self.all_out_edges

    def add_In_edge(self, otherId, weight):
        self.all_in_edges[otherId] = weight

    def add_Out_edge(self, otherId, weight):
        self.all_out_edges[otherId] = weight

    def remove_In_edge(self, otherId):
        return self.all_in_edges.pop(otherId)

    def remove_Out_edge(self, otherId):
        return self.all_out_edges.pop(otherId)
    def __copy__(self):
        node = Node()
        for node1 in node.all_out_edges:
            node.add_Out_edge(node1)
        for node1 in node.all_in_edges:
            node.add_in_edge(node1)
        return node

def main():
    newGraph = DWGraph()
    print(newGraph.EdgeSize)


if __name__ == '__main__':
    main()
