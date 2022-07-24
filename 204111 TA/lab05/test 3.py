def Year_for_February(m, y):
    if m > 4:
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
    elif m <= 4:
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



def main():
    d, m, y = input( ).split( )
    d = int(d)
    m = int(m)
    y = int(y)
    number = Year_for_February(m, y)
    print(number)

if __name__ == '__main__':
    main()
