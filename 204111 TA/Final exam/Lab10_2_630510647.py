def classify(list_x):
    list_a = [] #list เก็บข้อมูล int
    list_b = [] #list เก็บข้อมูล float
    list_c = [] #list เก็บข้อมูล str
    for i in list_x: #ลูปแยกข้อมูลใน list
        if isinstance(i, int): #ฟังก์ชั่นตรวจสอบข้อมูลว่าเป็น int ไหม ถ้าใช้ append เข้า list_a
            list_a.append(i)
        elif  isinstance(i, float): #ฟังก์ชั่นตรวจสอบข้อมูลว่าเป็น float ไหม ถ้าใช้ append เข้า list_b
            list_b.append(i)
        elif  isinstance(i, str): #ฟังก์ชั่นตรวจสอบข้อมูลว่าเป็น str ไหม ถ้าใช้ append เข้า list_c
            list_c.append(i)

    return list_a, list_b, list_c 

def main():
    #str1 = input().split()
    #a, b, c = classify(list_x):
    a, b, c = classify([10, 'hello', 23.5, 4])
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab10_2