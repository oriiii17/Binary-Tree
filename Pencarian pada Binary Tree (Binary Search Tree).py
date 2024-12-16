#mencari data
def search(self, value):
    return self.binarySearch(self._root, value) is not None
#algoritma binary search
def binarySearch(self, node, value):
    if node is None or node.operator() == value:
        return node
    elif value < node.operator():
        return self.binarySearch(node.left(), value)
    else:
        return self.binarySearch(node.right(), value)
    
print(tree.search(25))
print(tree.search(8))