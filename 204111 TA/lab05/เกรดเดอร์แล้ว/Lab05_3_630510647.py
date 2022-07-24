def Year_for_February(m, y):
    if m >= 4:
        if (y + 1) % 4 == 0: #0 No 1 Yes
            if (y + 1) % 400 == 0:
                year = 1
            elif (y + 1) % 100 == 0:
                year = 0
            else:
                year = 1
        else:
            year = 0

        return year
    elif m < 4:
        if y % 4 == 0: #0 No 1 Yes
            if y % 400 == 0:
                year = 1
            elif y % 100 == 0:
                year = 0
            else:
                year = 1
        else:
            year = 0

        return year

def count_down_to_songkran(d, m, y):
    sum_a = 0
    year = Year_for_February(m, y)
    if year == 0:
        if m == 4:
            if d == 13:
                sum_a = 0
            elif d < 13:
                sum_a = (13 - d)
            elif d > 13:
                sum_a = (30 - d)+31+30+31+31+30+31+30+31+31+28+31+13
        elif m == 1:
            sum_a = (31 - d)+28+31+13
        elif m == 2:
            sum_a = (28 - d)+31+13
        elif m == 3:
            sum_a = (31 - d)+13
        elif m == 5:
            sum_a = (31 - d)+30+31+31+30+31+30+31+31+28+31+13
        elif m == 6:
            sum_a = (30 - d)+31+31+30+31+30+31+31+28+31+13
        elif m == 7:
            sum_a = (31 - d)+31+30+31+30+31+31+28+31+13
        elif m == 8:
            sum_a = (31 - d)+30+31+30+31+31+28+31+13
        elif m == 9:
            sum_a = (30 - d)+31+30+31+31+28+31+13
        elif m == 10:
            sum_a = (31 - d)+30+31+31+28+31+13
        elif m == 11:
            sum_a = (30 - d)+31+31+28+31+13
        elif m == 12:
            sum_a = (31 - d)+31+28+31+13

    elif year == 1:
        if m == 4:
            if d == 13:
                sum_a = 0
            elif d < 13:
                sum_a = (13 - d)
            elif d > 13:
                sum_a = (30 - d)+31+30+31+31+30+31+30+31+31+29+31+13
        elif m == 1:
            sum_a = (31 - d)+29+31+13
        elif m == 2:
            sum_a = (29 - d)+31+13
        elif m == 3:
            sum_a = (31 - d)+13
        elif m == 5:
            sum_a = (31 - d)+30+31+31+30+31+30+31+31+29+31+13
        elif m == 6:
            sum_a = (30 - d)+31+31+30+31+30+31+31+29+31+13
        elif m == 7:
            sum_a = (31 - d)+31+30+31+30+31+31+29+31+13
        elif m == 8:
            sum_a = (31 - d)+30+31+30+31+31+29+31+13
        elif m == 9:
            sum_a = (30 - d)+31+30+31+31+29+31+13
        elif m == 10:
            sum_a = (31 - d)+30+31+31+29+31+13
        elif m == 11:
            sum_a = (30 - d)+31+31+29+31+13
        elif m == 12:
            sum_a = (31 - d)+31+29+31+13
        
    return sum_a




def main():
    d, m, y = input( ).split( )
    d = int(d)
    m = int(m)
    y = int(y)
    number = count_down_to_songkran(d, m, y)
    print(number)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab05_3

