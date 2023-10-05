import numpy as np
def appendQueue():
    while True:
        number = int(input("ตัวเลขจำนวนเต็มที่ต้องการจัดเก็บในคิววงกลม = "))
        if number % 2 == 0:
            return number
        else:
            True
n = 1
condition = 0
list = []
while n < 4:
    n = int(input("Enter size of queue : "))
while condition < 4:
    condition = int(input("โปรดระบุทางเลือกในการดำเนินการกับคิววงกลม\n1. เพิ่มขอมูลตัวเลขจํานวนเต็มในคิววงกลม\n2. ลบขอมูลที่จัดเก็บในคิววงกลม 1 ตัว\n3. แสดงตัวเลขจํานวนเต็มที่เปนเลขคูที่จัดเก็บในคิววงกลมทางจอภาพ\nทางเลือกในการดำเนินการ : "))
    if condition == 1:
        if len(list) !=  n:
            list.append(appendQueue())
        else:
            print("เพิ่มข้อมูลไม่ได้เนื่องจากคิวเต็ม")
    if condition == 2 :
        if len(list) != 0:
            list.pop(0)
        else:
            print("ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง")
    if condition == 3:
        if len(list) != 0:
            print(list)
        else:
            print("แสดงข้อมูลตัวเลขจำนวนเต็มที่เป็นเลขคู่ที่จัดเก็บในคิววงกลมไม่ได้เพราะคิววงกลมว่าง")















































































'''
class queue :
    def __init__(self,n):
        self.n = n
        self.queue = [None]*n
        self.front = -1
        self.rear = -1

    def add(self,item):
        if self.rear == self.n - 1:
            print("Queue is full")
        else :
            if self.front == -1:
                self.queue[self.rear+1] = item
                self.rear = self.rear + 1
                self.front = self.front +1
            else:
                self.queue[self.rear+1] = item
                self.rear = self.rear+1

    def remove (self):
        if (self.rear-self.front)+1 == 0:
            print("Queue is empty")
        else:
            if self.front == self.rear:
                self.queue[self.rear] = None
                self.rear = -1
                self.front = -1
                print("Queue is empty")
            else:
                self.queue[self.front] = None
                self.front = self.front+1

    def len(self):
        return len(self.queue)

    def display(self):
        if (self.front == -1):
            print("Queue is empty")
        else:
            for i in self.queue:
                print(i)

# Class Circulur Queue
class circulurQueue:
    def __init__(self , n ):
        self.n = n
        self.queue = []*n
        self.front = -1
        self.rear = -1

    def addci(self,data):
        if ((self.rear+1) % self.n == self.front):
            print("Circular queue is full")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue.append(data)
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue.append(data)

    def removeci(self):
        if (self.front == -1):
            print("Circular queue is empty")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else :
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n
            return temp

    def displayci(self):
        if (self.front == -1):
            print("Circular queue is empty")
        elif self.rear >= self.front :
            for i in range(self.front, self.rear +1):
                print(self.queue[i])
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])
            for i in range(0, self.rear + 1):
                print(self.queue[i])
'''