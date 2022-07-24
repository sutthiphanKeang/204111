def Euclid(x1,y1,x2,y2):
    Euclid = (((x1-x2)**2)+((y1-y2)**2))**0.5
    return Euclid

def intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6):
    circle = Euclid(x1,y1,x2,y2)
    if circle < r1 or circle < r2:
        if r1 < r2:
            r_min = r1
            r_max = r2
        else:
            r_min = r2
            r_max = r1
        if (abs(r_min+circle-r_max)) <= epsilon:
            number = 0
        elif (circle+r_min) > r_max:
            number = 1
        else:
            number = -1       
    else:
        if (abs((r1+r2)-circle)) <= epsilon or (r1+r2) == circle:
            number = 0
        elif circle-(r1+r2) < 0:
            number = 1
        else:
            number = -1
        
    return number


def main():
    x1, y1, r1 = input( ).split( )
    x1= float(x1)
    y1 = float(y1)
    r1 = float(r1)
    x2, y2, r2 = input( ).split( )
    x2 = float(x2)
    y2 = float(y2)
    r2 = float(r2)
    number = intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6)
    print(number)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab05_1
