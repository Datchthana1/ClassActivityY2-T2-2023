count = 0
Table = int(input("โปรดป้อนขนาดตารางแฮช : "))
Hashing = [None] * Table
while True:
    index = 1
    Key = int(input("โปรดป้อนค่าคีย์ (Key) ที่มีค่าตั้งแต่ 0 ขึ้นไป : "))
    Value = str(input("โปรดป้อนข้อมูลชื่อพนักงานเพื่อจัดเก็บในตารางแฮช : "))
    if Key < 0:
        break
    index = Key % Table
    while True:
        if Hashing[index] == None :
            Hashing[index] = Value
            print(f"Address : {Hashing.index(Value)}")
            break
        else:
            index += 1
print("ข้อมูลในตารางแฮช")
for j in range(len(Hashing)):
    if Hashing[j] == None:
        print(f"Address : {j} ไม่มีข้อมูลจัดเก็บ")
    else:
        print(f"Address : {j} ข้อมูลที่จัดเก็บคือ {Hashing[j]}")         