from src.DiGraph import Node


class MinHeap:

    def __init__(self):
        # heap containing node
        self.heap = []
        # the first value in the heap at index 0 is None
        self.heap.append(None)
        # dictionary maps id(a.k.a key) to index (a.k.a value) inside the heap
        self.keyToIndex = {}

    def size(self) -> int:
        return self.heap.__len__()

    def swim(self, indexOfNode):
        if indexOfNode == 1:
            return
        parentIndex = int(indexOfNode / 2)
        if self.heap[parentIndex] > self.heap[indexOfNode]:
            self.swap(indexOfNode, parentIndex)
            self.swim(parentIndex)

    def sink(self, parent):
        if parent >= self.size():
            return
        leftChild = parent * 2
        rightChild = parent * 2 + 1
        if leftChild >= self.size():
            return
        # parent bigger than left child and right not exist, swap and call sink
        elif rightChild >= self.size():
            if self.heap[leftChild] < self.heap[parent]:
                self.swap(leftChild, parent)
                self.sink(leftChild)
        # parent bigger than the minimal of right and left, swap them and call recursivly
        else:
            minimumChild = leftChild if self.heap[leftChild] < self.heap[rightChild] else rightChild
            if self.heap[minimumChild] < self.heap[parent]:
                self.swap(minimumChild, parent)
                self.sink(minimumChild)

    def insert(self, node):
        if node is None:
            raise RuntimeWarning("Cant add null to heap")
        self.heap.append(node)
        self.keyToIndex[node.id] = self.size() - 1
        self.swim(self.size() - 1)

    def removeMin(self) -> Node:
        self.swap(1, self.size() - 1)
        minimalNode = self.heap.pop(self.size() - 1)
        self.sink(1)
        return minimalNode

    def remove(self, index) -> Node:
        self.swap(index, self.size() - 1)
        resNode = self.heap.pop(self.size() - 1)
        self.sink(index)
        return resNode

    def isEmpty(self):
        return self.size() == 1

    def DecreaseKey(self, NodeId, weight):
        nodeIndex = self.keyToIndex.get(NodeId)
        if weight < self.heap[nodeIndex]:
            self.heap[nodeIndex] = weight
            self.swim(nodeIndex)

    def swap(self, iIndex, jIndex):
        # swaps the indexes respectively to their location
        self.heap[iIndex], self.heap[jIndex] = self.heap[jIndex], self.heap[iIndex]
        # O(n) lol
        keyValList = list(self.keyToIndex)
        keyValList[iIndex], keyValList[jIndex] = keyValList[jIndex], keyValList[iIndex]
        self.keyToIndex = dict(keyValList)
