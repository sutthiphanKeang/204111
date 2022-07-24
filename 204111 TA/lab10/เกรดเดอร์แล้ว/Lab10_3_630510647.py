def nondest_rotate_list(list_a, n):
    new_list = list_a 
    num_list = abs(n) % len(list_a) #หาจำนวนที่ต้องสลับ
    #print(num_list)
    if n > 0: #ตรวจสอบว่าเลขเป็นบวก 
        for i in range(num_list): #ลูปตามจำนวนที่ต้องสลับ
            x = new_list[len(list_a) - 1 : ] #ตัดตัวหลังสุดออกมา
            y = new_list[ : len(list_a) - 1] #ตัดตัวที่เหลือ
            result = x + y
            new_list = result

    else:
        for i in range(num_list):#ลูปตามจำนวนที่ต้องสลับ
            x = new_list[1 : ] #ตัดตัวในlist ยกเว้นตัวแรก
            y = new_list[ : 1] #ตัดตัวแรก
            result = x + y
            new_list = result


    #print('aa',list_a)
    return result



def main():
    #list_a = input().split()
    #print(list_a)
    #n = int(input())
    #print(nondest_rotate_list(list_a, n))
    print(nondest_rotate_list([1, 2, 3, 4], -1))

if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab10_3