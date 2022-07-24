def reverse_num(num): #main function
    return int(reverse_to_int(str(num)))

def reverse_to_int(num):#help function
    if int(num) >= 0: #เช็คว่า num ไม่ติดลบ
        if int(num) < 10: #ถ้า num น้อยกว่า 10 ให้คืนค่า num
            return str(num)
        else:
            x = len(str(num)) #หาจำนวนเลข
            y = str(num) 
            return str(y[x-1 : x] + str(reverse_to_int(int(num) // 10))) #คืนค่าพร้อมเปลี่ยนค่าฟังก์ชั่น โดยตัดตำแหน่งสุดท้ายออกมาบวกไปเรื่อยๆ


def main():
    num = int(input())
    print(reverse_num(num))
    print(type(reverse_num(num)))
    

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab09_5
