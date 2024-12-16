#mengeset node left
def setLeft(self, node):
    self._left = node
#mengeset node right
def setRight(self, node):
    self._right = node
#mengeset node parent
def setParent(self, node):
    self._parent = node

#  implementasikan kedua method expandExternal() dan removeAboveExternal() pada
#  class BinaryTree:

 #mencari data
def expandExternal(self, value):
    node = self.binarySearch(self._root, value)
    if node is not None and node.isExternal():
        node.insert(node.operator()-1)
        node.insert(node.operator()+1)
        self._size+=2
 
 #mencari data
def removeAboveExternal(self, value):
    node = self.binarySearch(self._root, value)
    if node is not None:
        sibling = node.parent().left() if node == node.parent().right() else node.parent().
        if node.parent() == self._root:
            self._root = sibling
            sibling.setParent(None)
        else:
            if node.parent() == node.parent().parent().left():
                node.parent().parent().setLeft(sibling)
            else:
                node.parent().parent().setRight(sibling)
        self._size-=2

        
#  Lakukan pengujian pada operasi tersebut:
tree.expandExternal(9)
tree.nodes()
tree.removeAboveExternal(7)
tree.nodes()