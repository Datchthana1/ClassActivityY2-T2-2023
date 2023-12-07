class Sorting:
    def __init__(self):
        self.List = []

    def Input(self):
        print("โปรดป้อนข้อมูลตัวเลขจำนวนเต็มที่ต้องการเรียงลำดับ ถ้าต้องการหยุดการวนซ้ำเพื่อรับข้อมูลให้ป้อน -1234")
        while True:
            Number = int(input("ข้อมูลที่ต้องการเรียงลำดับ : "))
            if Number < 0 :
                print("ข้อมูลก่อนเรียงลำดับ คือ ")
                for Number_list in self.List:
                    print(Number_list,end=" ")
                break
            else:
                Number = self.List.append(Number)

    def Sorting_List(self):
        print("\nขั้นตอนการเรียงลำดับจากย้อยไปมากด้วยขั้นตอนวิธีแบบ Bubble Sort")
        for i in range(len(self.List)-1):
            for j in range(0, len(self.List)-i-1):
                if self.List[j] > self.List[j+1]:
                    self.List[j], self.List[j+1] = self.List[j+1], self.List[j]
            print(f"\n Pass = {i+1} : ผลลัพธ์จากการเรียงลำดับ คือ ")
            for Number_list in self.List:
                print(Number_list,end=" ")

    def OutPut(self):
        print("\nข้อมูลที่เรียงจากน้อยไปมาก คือ ")
        for Number_list in self.List:
            print(Number_list,end=" ")

Sorting = Sorting()
Sorting.Input()
Sorting.Sorting_List()
Sorting.OutPut()