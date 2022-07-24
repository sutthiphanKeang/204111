def octagon_area(x):
    result = (x*x)-((0.5*((x/3)**2))*4)
    return result

def main():
    x = float(input())
    result = octagon_area(x)
    print("%.6f" % result, type(result))

if __name__ == '__main__':
    main()

#630510647
    
#สุทธิพันธ์ ประนันแปง
#002
#Lab03_3


