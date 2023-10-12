class Node:
    def __init__(self,info = None):
        self.info = info
        self.next = None

class SLinkList:
    def __init__(self) :
        self.head = None
        self.tail = None
    def AtTheBeginning(self,data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
       
    def AtTheEnd(self,data):
        if self.tail == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode
    
    def OptionalProgramming(self):
        node = Node
        link = SLinkList
        txt = 1
        while txt > 0 and txt < 4:
            txt = int(input("โปรดระบุทางเลือกในการดำเนินการกับ Singly Linked List\n1 เพื่อเพิ่มข้อมูลทีจุดเริ่มต้นของ Singly linked list\n2 เพื่อเพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list\n3 เพื่อแสดงข้อมูลที่จัดเก็บในตําแหน่งที่พ้อยเตอร์ head และ tail ชี้ และข้อมูลใน Singly linked list\nทางเลือกในการดำเนินการ = "))
            if txt == 1:
                data = int(input("ตัวเลขที่ต้องการเพิ่มที่จุดเริ่มต้นของ Singly Linked List = "))
                link.AtTheBeginning(data)
            elif txt == 2:
                data = input("ตัวเลขที่ต้องการเพิ่มต่อจากตัวสุดท้ายของ Singly linked List = ")
                link.AtTheEnd(data)
            elif txt == 3:
                print(f"ข้อมูลที่จัดเก็บในตำแหน่งพ้อยเตอร์ head และ tail ชี้ คือ\nhead = {self.head.info}\ntail = {self.tail.info}")
                print(f"ข้อมุลที่อยู๋ใน Singly Linked List คือ")
                while self.head.info != None:
                    tmpt = self.head
                    while tmpt != data:
                        print(tmpt.info)
                        tmpt = tmpt.next
            else:
                break

SLinkList = SLinkList()
SLinkList.OptionalProgramming()