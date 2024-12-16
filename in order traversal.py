class BinaryTree:
    #constructor
    def __init__(self):
        self._root = None
        self._size = 0
 
    #menambah data
    def add(self, data):
        if self._root is None:
            self._root = Node(data, None)
            self._size+=1
        else:
            if self._root.insert(data):
            self._size+=1
 
    #mendapatkan jumlah node dari tree
    def size(self):
        return self._size
 
    #mengecek apakah tree kosong
    def empty(self):
        return self._size == 0
 
    #mencetak seluruh node
    def nodes(self):
        self.inorder(self._root)
 
    #inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.operator(), end = ' ')
            self.inorder(node.right())

tree = BinaryTree()
tree.add(10)
tree.add(5)
tree.add(7)
tree.add(1)
tree.add(15)
tree.add(9)
tree.add(25)
tree.add(90) 
tree.nodes()