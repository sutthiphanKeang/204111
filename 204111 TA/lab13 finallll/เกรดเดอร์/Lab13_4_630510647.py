def square_matrix(list_x):
    max_row = 0
    for row in list_x: #นับจำนวนของแถวที่มากที่สุด
        num = len(row)
        if num > max_row:
            max_row = num
        num = 0
    
    max_col = 0
    new = []
    all_ = []
    for col in range(len(list_x)): #สลับแถวเป็นหลักเพื่อให้ง่ายในการคำนวณ
        for k in range(len(list_x)):
            try:
                new += [list_x[k][col]]
            except IndexError: #กรณีที่ไม่มีเลขแล้ว ให้ผ่านไป
                continue
        all_.append(new)
        new = []
    
    for col in all_: ##นับจำนวนของหลักที่มากที่สุด
        num = len(col)
        if num > max_col:
            max_col = num
        num = 0
    
    if max_row > max_col: #ถ้าแถวที่มากที่สุด มากกว่า หลักที่มากที่สุด
        for i in list_x:
            if len(i) == max_row:
                continue
            else:
                for j in range(max_row - len(i)):
                    i.append(0)

    else:
        for i in list_x:
            if len(i) == max_col:
                continue
            else:
                for j in range(max_col - len(i)):
                    i.append(0)

    if len(list_x) == len(list_x[0]): #ถ้าแถวและหลักเท่ากันจบการทำงาน
        return
    else: #ถ้าไม่ เติม 0 ลงไปแล้วเรียกทำฟังก์ชั่นอีกครั้ง
        for k in (list_x):
            for l in range(len(list_x[0])):
                if len(list_x) != len(list_x[0]):
                    list_x.append([0])
        return square_matrix(list_x)
    


def main():
    list_x = [[2, 3, 4],[1, 2, 3]]
    square_matrix(list_x)
    print(list_x)



if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab13_4