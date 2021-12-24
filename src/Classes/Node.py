class Node:

    def __init__(self, id, pos):
        self.id = id
        self.pos = pos  # Need to get Tuple of the pos, build it when we get the json
        self.all_in_edges = {}
        self.all_out_edges = {}
