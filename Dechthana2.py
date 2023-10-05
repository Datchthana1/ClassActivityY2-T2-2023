def appendQueue():
        number = int(input("ตัวเลขจำนวนเต็มที่ต้องการจัดเก็บในคิววงกลม = "))
        return number
def CheckNumber (number1):
    if number1 % 2 == 0:
        return number1
n = 1
condition = 0
list = []
while n < 4:
    n = int(input("Enter size of queue : "))
while condition < 4:
    condition = int(input("โปรดระบุทางเลือกในการดำเนินการกับคิววงกลม\n1. เพิ่มข้อมูลตัวเลขจํานวนเต็มในคิววงกลม\n2. ลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว\n3. แสดงตัวเลขจํานวนเต็มที่เป็นเลขคู่ที่จัดเก็บในคิววงกลมทางจอภาพ\nทางเลือกในการดำเนินการ : "))
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
            for i in list:
                confirm = CheckNumber(i)
                if confirm == None:
                    pass
                else:
                    print(confirm)
        else:
            print("แสดงข้อมูลตัวเลขจำนวนเต็มที่เป็นเลขคู่ที่จัดเก็บในคิววงกลมไม่ได้เพราะคิววงกลมว่าง")
