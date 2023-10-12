class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def AtTheBegining(self, data):
    if self.head != None:
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
    else:
        NewNode = Node(data)
        NewNode.next = None
        self.head = NewNode
        self.tail = NewNode

def AtTheEnd(self, data):
    if self.head == None:
        NewNode = Node(data)
        NewNode.next = None
        self.head = NewNode
        self.tail = NewNode
    else:
        NewNode = Node(data)
        NewNode.next = None
        self.tail.next = NewNode
        self.tail = NewNode