unit_list = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
ty_list = ["","","twenty","thirty", "forty", "fifty" ,"sixty", "seventy","eighty", "ninety"] 
#list ค่าตัวเลข

def three_digits_to_word(n): #ฟังก์ชั่นที่จะทำที่ละ 3 ตำแหน่ง
        if n <= 19:
            return unit_list[n]
        elif n > 19:
            if n < 100:
                x, y = divmod(n, 10)
                if y == 0:
                    return ty_list[x] + ' ' + unit_list[y]
                elif y != 0:
                    return ty_list[x] + '-' + unit_list[y]
            else:
                x, y = divmod(n, 100)
                a, b = divmod(y, 10)
                if y == 0: #ถ้าเป็นเลขที่ไม่มีหลักอื่น นอกจะหลักร้อย
                    return unit_list[x] + ' hundred'
                elif y <= 19:
                    return unit_list[x] + ' hundred ' + unit_list[y]
                else:
                    if b == 0:
                        return unit_list[x] + ' hundred ' + ty_list[a]
                    else:
                        return unit_list[x] + ' hundred ' + ty_list[a] + '-' + unit_list[b]



def num_to_word(num): #main ฟังก์ชั่น จะเรียก three_digits_to_word(n) มาทำงาน
    #เพื่อนำไปเรียกฟังก์ชั่น three_digits_to_word(n) และ list ด้านบน
    x, y = divmod(num, 1000) #หาหลักมาสามตัวหลักพัน
    a, b = divmod(x, 10) #หาหลักมาสามตัวหมื่น
    c, d = divmod(x, 1000) #หาหลักมาสามตัวล้าน และมาสามตัวแสน
    e, f = divmod(c, 10) #หาหลักมาสามตัวสิบล้าน
    g, h = divmod(x, 1000) #หาหลักมาสามตัวร้อยล้าน
    i, j = divmod(c, 1000) #หาหลักมาสามตัวหมื่นล้าน
    k, l = divmod(i, 10) #หาหลักหน่วยตรงหมื่นล้าน
    
    if num == 0:
        return 'zero'

    elif num <= 999: #ตรวจสอบว่า num เป็นเลขหลักร้อย
        return three_digits_to_word(num)

    elif num <= 99999: #ตรวจสอบว่า num เป็นเลขหลักหมื่น
        if y == 0:
            return unit_list[x] + ' thousand'
        elif x <= 19:
            return unit_list[x] + ' thousand ' + three_digits_to_word(y)
        else:
            if b == 0:
                return ty_list[a] + ' thousand ' + three_digits_to_word(y)
            elif b != 0:
                return ty_list[a] + '-' + unit_list[b] + ' thousand ' + three_digits_to_word(y)

    elif num <= 999999: #ตรวจสอบว่า num เป็นเลขหลักแสน
        if y == 0:
            return three_digits_to_word(x) + ' thousand'
        else:
            return three_digits_to_word(x) + ' thousand ' + three_digits_to_word(y)

    elif num <= 99999999: #ตรวจสอบว่า num เป็นเลขหลักสิบล้าน
        if y == 0:
            return unit_list[c] + ' million'
        elif c <= 19:
            return unit_list[c] + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)
        else:
            if f == 0:
                return ty_list[e] + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)
            elif f != 0:
                return ty_list[e] + '-' + unit_list[f] + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)

    elif num <= 999999999: #ตรวจสอบว่า num เป็นเลขหลักร้อยล้าน
        if y == 0:
            return three_digits_to_word(g) + ' million'
        else:
            return three_digits_to_word(g) + ' million ' + three_digits_to_word(h) + ' thousand ' + three_digits_to_word(y)
    
    elif num <= 99999999999: #ตรวจสอบว่า num เป็นเลขหลักหมื่นล้าน
        if y == 0:
            if i <= 19:
                return unit_list[i] + ' billion'
            else:
                if l == 0:
                    return ty_list[k] + ' billion'
                else:
                    return ty_list[k] + '-' + unit_list[l] + ' billion'
        if i <= 19:
            return unit_list[i] + ' billion ' + three_digits_to_word(j) + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)
        else:
            if l == 0:
                return ty_list[k] + ' billion ' + three_digits_to_word(j) + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)
            elif l != 0:
                return ty_list[k] + '-' + unit_list[l] + ' billion ' + three_digits_to_word(j) + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)
    
    elif num <= 999999999999: #ตรวจสอบว่า num เป็นเลขหลักล้านล้าน
        if y == 0:
            return three_digits_to_word(i) + ' billion'
        else:
            return three_digits_to_word(i) + ' billion ' + three_digits_to_word(j) + ' million ' + three_digits_to_word(d) + ' thousand ' + three_digits_to_word(y)


    

def main():
    n = int(input())
    print(num_to_word(n))
    
    


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab10_5
