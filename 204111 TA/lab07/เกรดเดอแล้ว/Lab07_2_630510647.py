def digit_count(x, base=10):
    num = 0
    i = 0
    while x != 0:
        num = abs(x) // base
        x = num
        i += 1
    return (i)


def test_digit_count():
    print("Testing ones_digit...",end="")
    assert(digit_count(258) == 3)
#กรณีนี้มีการกรอกค่า x มีค่าเท่ากับ 258 แต่ไม่ได้กรอกค่า y ดังนั้น ฐานจึงเท่ากับ base ซึ่งมีค่าเท่ากับ 10 นำ x มาหารปัดเศษด้วย 10 เรื่อยๆ จนกว่า x จะมีค่าเป็น 0 แล้วนับจำนวนครั้ง
    assert(digit_count(258, 2) == 9)
#กรณีนี้มีการกรอกค่า x มีค่าเท่ากับ 258 และ y มีค่าเท่ากับ 2 นำ x มาหารปัดเศษด้วย 2 เรื่อยๆ จนกว่า x จะมีค่าเป็น 0 แล้วนับจำนวนครั้ง    
    print("Passed all tests!")

def main():
    x = int(input())
    y = int(input())
    print(digit_count(x, y))
    test_digit_count()


if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab07_2
