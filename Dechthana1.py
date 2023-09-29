SOS = 0
Stack = []
while SOS < 5 :
 SOS = int(input("Size of Stack : "))
while len(Stack) != SOS+1:
    Conditions = int(input("โปรดระบุทงเลือกในการดำเนินการ \n 1. เพิ่มข้อมูลใน Stack \n 2. ลบข้อมูลที่จัดเก็บในตําแหน่งบนสุดของ Stack \n 3. แสดงข้อมูลที่จัดเก็บในตําแหน่งบนสุดของ Stack ทางจอภาพ \n 4. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Stack ทางจอภาพ \n 5. แสดงคำมากที่สุดและค่าน้อยที่สุดของข้อมูลที่จัดเก็บใน Stack ทางจอภาพ \n : "))
    print(f"ทางเลือกในการดำเนินการ = {Conditions}")
    if len(Stack) == SOS:
        print("The Stack is Full")
    else:
        if Conditions == 1:
            if len(Stack) != SOS:
                Text1 = int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Stack คือ : "))
                Stack.append(Text1)
            else:
                print("เก็บข้อมูลไม่ได้เพราะ Stack เต็ม")
        elif Conditions == 2:
            if len(Stack) != 0:
                Stack.pop()
            else:
                print("ลบช้อมูลไม่ได้เพราะ Stack ว่าง")
        elif Conditions == 3:
            if len(Stack) == 0:
                print("แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง")
            else:
                print(f"ข้อมูลที่จัดเก็บในตำแหน่งสูงสุดของ Stack คือ {Stack[-1]}")
        elif Conditions == 4:
            print(f"ข้อมูล = {Stack}")
        elif Conditions == 5:
            max = Stack[0]
            min = Stack[0]
            if len(Stack) != 0:
                for i in range(1, len(Stack)):
                    if Stack[i] > max:
                        max = Stack[i]
                    else:
                        Stack[i] < min
                        min = Stack[i]
                print(f"ค่ามากที่สุดของข้อมูลใน Stack คือ {max}\nค่าน้อยที่สุดของข้อมูลใน Stack คือ {min}")
            else:
                print("แสดงค่ามากที่สุดและค่าน้อยที่สุดในข้อมูลใน Stack ไม่ได้ Stack ว่าง")
        else:
            if Conditions > 5:
                break
print("Dechthana Arunchaiya 65112948")