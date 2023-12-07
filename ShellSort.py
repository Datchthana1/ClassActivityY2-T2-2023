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

def shell_sort2(Array_data):
    print("ข้อมูลก่อนเรียงลำดับ คือ \n",*Array_data)
    n = len(Array_data)
    gap = (n + 1) // 2
    while gap > 0:
        for i in range(gap, n):
            temp = Array_data[i]
            j = i
            while j >= gap and Array_data[j - gap] > temp:
                Array_data[j] = Array_data[j - gap]
                j -= gap
            Array_data[j] = temp
        gap //= 2
        print("ผลลัพท์จากการเรียงลำดับ = \n",*Array_data)
    return Array_data

shell_sort2(InputNumber())