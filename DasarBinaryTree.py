class Node:
    #constructor
    def __init__(self, data, parent):
        self._data= data
        self._parent= parent
        self._left= None
        self._right= None
 
    #menambahdata
    def insert(self, data):
        if data< self.operator():
            if self.left() is None:
                self._left= Node(data, self)
            else:
                self.left().insert(data)
        elif data> self.operator():
            if self.right() is None:
                self._right= Node(data,self)
            else:
                self.right().insert(data)
        else:
            return False #jika tidak berhasil menambah data
        return True #jika berhasil menambah data
 
    #mendapatkanisi elemen
    def operator(self):
        return self._data
    
    #mendapatkanchild sebelahkiri
    def left(self):
        return self._left
 
    #mendapatkanchild sebelahkanan
    def right(self):
        return self._right
 
    #mendapatkannode parent
    def parent(self):
        return self._parent
 
    #mengecekapakah node merupakan root
    def isRoot(self):
        return self._parent is None
    
    #mengecek apakah node merupakan external/leaf
    def isExternal(self):
        return self._left is None and self._right is None