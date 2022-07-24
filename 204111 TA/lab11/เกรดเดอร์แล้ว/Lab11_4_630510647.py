import copy
def sum_nested_list(list_a):
    new_list = copy.deepcopy(list_a) #copy list แบบไม่เปลี่ยน list เดิม
    if find_int(new_list) is True: #ตรวจสอบแล้วว่าข้างใน list ไม่มี list ซ้อนอยู่
        return sum(new_list) 
    else:
        return sum_nested_list(new_list) #กลับไปทำฟังก์ชั่นเดิมอีกครั้ง โดยเปลี่ยนค่า list แล้ว (แต่ยังมี list ซ้อน)


def find_point(x): #ฟังก์ชั่นลบlist ที่ซ้อนใน list รวม
    for i in x:
        if isinstance(i, list): #ตรวจสอบว่าตัวที่แยกคือ list
            x.remove(i) #ลบออก
            x.extend(i) #เพิ่มค่าเข้าไป
    return x

def find_int(x): #ฟังก์ชั่นตรวจสอบ ว่า list ไม่มี list ซ้อน
    for i in find_point(x):
        if isinstance(i, int): ##ตรวจสอบว่าตัวที่แยกคือ list
            continue
        elif isinstance(i, list): ##ตรวจสอบว่าตัวที่แยกคือ list
            return False
    return True



def main():
    list_a = [61, [[2, [75]], 8000, [39]], [58, [46]]]
    print(sum_nested_list(list_a))


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab11_4