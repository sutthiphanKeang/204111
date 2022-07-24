def is_p_triple(a, b, c):
    if a > b and a > c:
        if ((b**2)+(c**2))**0.5 == a:
            return True
        else:
            return False
    elif b > a and b > c:
        if ((a**2)+(c**2))**0.5 == b:
            return True
        else:
            return False
    elif c > a and c > b:
        if ((a**2)+(b**2))**0.5 == c:
            return True
        else:
            return False
    else:
        return False

def main():
    a, b, c = input( ).split( )
    a = int(a)
    b = int(b)
    c = int(c)
    num = is_p_triple(a, b, c)
    print(num)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab05_1
