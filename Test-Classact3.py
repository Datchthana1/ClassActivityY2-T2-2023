class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None
class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def InsAtTheBeginning(self,data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
    def InsAtTheEnd(self,data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode