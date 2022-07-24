def count_segment(list_a):
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    for i in range(len(list_a)):
        x = list_a[i][0]
        y = list_a[i][1]
        r = list_a[i][2]
        a = ((x**2)+(y**2))**0.5
        if x > 0 and y > 0:
            Q1 += 1
            if r > a:
                Q2 += 1
                Q3 += 1
                Q4 += 1
            else:
                if r > abs(x):
                    Q2 += 1
                if r > abs(y):
                    Q4 += 1
        elif x < 0 and y > 0:
            Q2 += 1
            if r > a:
                Q1 += 1
                Q3 += 1
                Q4 += 1
            else:
                if r > abs(x):
                    Q1 += 1
                if r > abs(y):
                    Q3 += 1
        elif x < 0 and y < 0:
            Q3 += 1
            if r > a:
                Q2 += 1
                Q1 += 1
                Q4 += 1
            else:
                if r > abs(x):
                    Q4 += 1
                if r > abs(y):
                    Q2 += 1
        elif x > 0 and y < 0:
            Q4 += 1
            if r > a:
                Q2 += 1
                Q3 += 1
                Q1 += 1
            else:
                if r > abs(x):
                    Q3 += 1
                if r > abs(y):
                    Q1 += 1
        elif x == 0 and y > 0:
            if r > abs(y):
                Q1 += 1
                Q2 += 1
                Q3 += 1
                Q4 += 1
            else:
                Q1 += 1
                Q2 += 1
        elif x == 0 and y < 0:
            if r > abs(y):
                Q1 += 1
                Q2 += 1
                Q3 += 1
                Q4 += 1
            else:
                Q3 += 1
                Q4 += 1
        elif y == 0 and x > 0:
            if r > abs(x):
                Q1 += 1
                Q2 += 1
                Q3 += 1
                Q4 += 1
            else:
                Q1 += 1
                Q4 += 1
        elif y == 0 and x < 0:
            if r > abs(x):
                Q1 += 1
                Q2 += 1
                Q3 += 1
                Q4 += 1
            else:
                Q2 += 1
                Q3 += 1
        elif x == 0 and y == 0 and r > 0:
            Q1 += 1
            Q2 += 1
            Q3 += 1
            Q4 += 1
    #สูตร (x - h)**2 + (y - k)**2 == r**2 โจทย์ให้ h k r มา แทน x = 0 y = 0 
        
    return (Q1, Q2, Q3, Q4)


def main():
    list_a = [(0.0, 0.0, 1.0)]
    print(count_segment(list_a))

if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab13_1