class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        self.data = data  
        data = int(input(f"โปรดป้อนหมายเลชของโหมด Left child ของ {self.data} (ถ้าไม่มีให้ป้อน : -1234) : "))
        self.leftChild = Node()
        if data != -1234:
            self.leftChild.insert(data)
        data = int(input(f"โปรดป้อนหมายเลชของโหมด Right child ของ {self.data} (ถ้าไม่มีให้ป้อน : -1234) : "))
        self.rightChild = Node()
        if data != -1234:
            self.rightChild.insert(data)

    def PreOrder(self, tree):  
        if tree:
            if (tree.data != None) and (tree.data %3 == 0):
                print(tree.data,end=' ')
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)
                 
    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.leftChild)
            if (tree.data != None) and (tree.data > 20):
                print(tree.data,end=' ')
            self.InOrder(tree.rightChild)
           
    def PostOrder(self, tree):
        if tree:
            self.PostOrder(tree.leftChild)        
            self.PostOrder(tree.rightChild)
            if (tree.data != None) and (tree.data %2 == 1):
                print(tree.data,end=' ')

Dech = Node()
RN = int(input("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ Root node : "))
Dech.insert(RN)
while True:
    conditions = int(input("ทางเลือกในการดำเนินการ\n1 ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจํานวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 3 ลงตัวทางจอภาพ\n2 ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจํานวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าเกิน 20 ทางจอภาพ\n3 ทองไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจํานวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคี่ทางจอภาพ\nโปรดระบุทางเลือกในการดำเนินการ : "))
    if conditions == 1:
        print("Pre-order = ",end = '')
        Dech.PreOrder(Dech)
        print()
    elif conditions == 2:
        print("In-order = ",end = '')
        Dech.InOrder(Dech)
        print()
    elif conditions == 3:
        print("Post-order =  ",end = '')
        Dech.PostOrder(Dech)
        print()
    else:
        break
