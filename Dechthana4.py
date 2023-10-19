class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        self.data = data   
        data = int(input())
        self.leftChild = Node()
        self.leftChild.insert(data)
        data = int(input())
        self.rightChild = Node()
        self.rightChild.insert(data)
    
    def PreOrder(self, tree):
        if tree:
            print(tree.data)
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)
                 
    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.leftChild)
            print(tree.data)
            self.InOrder(tree.rightChild)
           
    def PostOrder(self, tree):
        if tree:
            self.PostOrder(tree.leftChild)        
            self.PostOrder(tree.rightChild)
            print(tree.data)