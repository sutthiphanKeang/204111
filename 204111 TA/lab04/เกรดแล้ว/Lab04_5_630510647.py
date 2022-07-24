def nearest_odd(x):
    if int(x%2) == 0:
        if (x % 2) == 0:
            x = int(x+1)
            return x
        else: 
            x = int(((x - (x%1))//1)+1)
            return x
    else: 
        if (x % 2) == 1:
            x = int(x)
            return x
        else:
            x = int((x - (x%1))//1)
            return x


def main():
    x = float(input())
    number = nearest_odd(x)
    print(number)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab04_5
