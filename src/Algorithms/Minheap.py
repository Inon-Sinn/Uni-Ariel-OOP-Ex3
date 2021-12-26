import DiGraph

class MinHeap:

    def __init__(self):
        # heap containing nodes
        self.heap = []
        # the first value in the heap at index 0 is None
        self.heap.append(None)
        # dictionary maps id(a.k.a key) to index (a.k.a value) inside the heap
        self.keyToIndex = {}

    def size(self) -> int:
        return self.heap.__len__()
    def swim(self, indexOfNode):
        if(indexOfNode == 1):
            return
        parent = (int) (indexOfNode/2)

    def sink(self):
        pass
    def insert(self, node):
        if(node == None):
            raise RuntimeWarning("Cant add null to heap")
        this.heap.append(node)
        self.keyToIndex[node.id] = self.size()-1
        self.swim(self.size()-1)
    def removeMin(self) -> Node:
        pass
    def remove(self) -> Node:
        pass
    def isEmpty(self):
        return (self.size() is 1)
    def DecreaseKey(self):
        pass
    def swap(self, iIndex, jIndex):
        # swaps the indexes respectively to their location
        self.heap[iIndex], self.heap[jIndex] = self.heap[jIndex], self.heap[iIndex]

