def polynomial_addition(p1, p2):
    result = []
    d1 = dict()
    d2 = dict()
    for i in p1: #นำสมการที่ 1 เข้าเก็บเป็น dict โดยให้ keys คือ กำลัง 
        d1[i[0]] = i[1]
    
    for i in p2: #นำสมการที่ 2 เข้าเก็บเป็น dict โดยให้ keys คือ กำลัง 
        d2[i[0]] = i[1]

    num_key1 = []
    num_key2 = []
    for i in d1: #เก็บเฉพาะ keys ของ dict สมการที่ 1
        num_key1.append(i)

    for i in d2: #เก็บเฉพาะ keys ของ dict สมการที่ 2
        num_key2.append(i)
 
    for i in num_key1: #ใช้ keys ของสมการที่ 1 เป็นตัวตั้ง
        if i in num_key2:
            if d2[i] == (d1[i] * -1): #ถ้าข้อมูลของสมการที่ 2 เท่ากับข้อมูลของสมการที่ 1 เป็นลบ ตัดออกจากdictทั้งสอง
                del d1[i]
                del d2[i]
            elif d1[i] == (d2[i] * -1):#ถ้าข้อมูลของสมการที่ 1 เท่ากับข้อมูลของสมการที่ 2 เป็นลบ ตัดออกจากdictทั้งสอง
                del d1[i]
                del d2[i]
            else: #เอาทั้งสองบวกกันแล้วเก็บค่าเข้า dict 1 แต่ทำการลบข้อมูลและkeys นั้นก่อน
                x = d1[i]
                y = d2[i]
                new = x + y
                del d1[i]
                del d2[i]
                d1[i] = new
    
    for i in d2: #นำตัวที่เหลือใน d2 เข้า d1
        x = d2[i]
        d1[i] = x
    
    all_key = []
    for i in d1: #นำเข้าเก็บใน list
        all_key.append(i)

                
    for i in all_key: #แยกแสดง keys, ข้อมูล
        result += [(i,d1[i])]
    
    awesome = sorted(result, reverse = True) #เรียงจากกำลังมากไปน้อย
    return awesome
    
   


def main():
    p1 = [(2, 6), (1, 34), (0, -8)]
    p2 = [(2, -6), (0, 2), (1, 1)]
    print(polynomial_addition(p1, p2))



if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab12_4