class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.leftChild == None:
                self.leftChild = Node()
                self.leftChild.data = data
            else:
                self.leftChild.insert(data)
        elif data > self.data:
            if self.rightChild == None:
                self.rightChild = Node()
                self.rightChild.data = data
            else:
                self.rightChild.insert(data)

    def findMaximumValue(self):
        if self.rightChild is None:
            return self.data
        return self.rightChild.findMaximumValue()

    def findMinimumValue(self):
        if self.leftChild is None:
            return self.data
        return self.leftChild.findMinimumValue()

    def PreOrder(self, tree):
        if tree:
            print(tree.data,end=" ")
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)


Dech = Node()
Data = input("โปรดป้อนข้อความเพื่อสร้าง Binary Search Tree (ถ้าต้องการหยุดการวนซ้ำให้ป้อนคำว่า Exit) : ")
while Data != "Exit":
    Dech.insert(Data)
    Data = input("โปรดป้อนข้อความเพื่อสร้าง Binary Search Tree (ถ้าต้องการหยุดการวนซ้ำให้ป้อนคำว่า Exit) : ")

print("\nผลลัพท์จากการท่องไปใน Binart Search Tree ด้วยขั้นตอนวิธีแบบ Pre-order")
Dech.PreOrder(Dech)
print(f"\nค่าน้อยที่สุดจัดเก็บใน Binary Search Tree คือ {Dech.findMinimumValue()}")