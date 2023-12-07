def InputNumber():
    count = 0
    size = int(input("โปรดระบุจำนวนข้อความมที่ต้องการเรียงลำดับ : "))
    List = []*size
    print("โปรดป้อนข้อความที่ต้องการเียงลำดับ")
    while count != size:
        count += 1
        Data = str(input("ข้อความ : "))
        Data = Data.upper()
        List.append(Data)
    return List

def shell_sort1(Array_data):
    print("\nข้อมูลก่อนเรียงลำดับ คือ \n",*Array_data)
    N = len(Array_data)
    Flag = 1
    Gap_Size = N
    while Flag == 1 or Gap_Size > 1:
        Flag = 0
        Gap_Size = (Gap_Size + 1) // 2
        for i in range(Flag,(N-Gap_Size)):
            if Array_data[Gap_Size + i] < Array_data[i]:
                Array_data[i + Gap_Size],Array_data[i] = Array_data[i],Array_data[i + Gap_Size]
                Flag = 0
        print("ผลลัพท์จากการเรียงลำดับ = \n",*Array_data)

shell_sort1(InputNumber())