def dest_rotate_list(list_a, n):
    num_list = abs(n) % len(list_a) #หาจำนวนที่ต้องสลับ
    if n > 0: #ตรวจสอบว่าเลขเป็นบวก 
        for i in range(num_list): #ลูปตามจำนวนที่ต้องสลับ
            y = list_a.pop(len(list_a) - 1) #เปลี่ยนค่าในlist ตัดตำแหน่งสุดท้าย และเก็บใน y
            list_a.insert(0, y) #แทรกไว้หน้าสุด
    else:
        for i in range(num_list): #ลูปตามจำนวนที่ต้องสลับ
            y = list_a.pop(0) #ตัดตำแหน่งหน้าสุด และเก็บไว้ใน y
            list_a.append(y) #append เข้า list เดิม
            





def main():
    nums = [1, 2, 3, 4]
    n = 1
    print(nums)
    out = dest_rotate_list(nums, n)
    print(out)
    print(nums)

if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab10_4