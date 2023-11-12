def Hash_Function():
    count = 0
    Table = int(input("โปรดป้อนขนาดตารางแฮช : "))
    Hashing = []
    for i in range(Table):
        Hashing.append(None)
    while True:
        index = 1
        Key = int(input("โปรดป้อนค่าคีย์ (Key) ที่มีค่าตั้งแต่ 0 ขึ้นไป : "))
        Value = str(input("โปรดป้อนข้อมูล(data) ที่เป็นข้อความเพื่อจัดเก็บในตารางแฮช : "))
        if Key < 0:
            break
        index = Key % Table
        if Hashing[index] == None :
            Hashing[index] = Value
        else:
            count += 1
            print(f"ตำแหน่งดังกล่าวในตารางแฮชจัดเก็บข้อมูล {Hashing[index]}")
    for j in range(len(Hashing)):
        if Hashing[j] == None:
            print(f"index {j} ว่าง")
        else:
            print(f"index {j} ข้อมูลที่จัดเก็บคือ {Hashing[j]}")
    print(f"จำนวนครั้งที่เกิด Collision = {count}")
            
Hash_Function()


