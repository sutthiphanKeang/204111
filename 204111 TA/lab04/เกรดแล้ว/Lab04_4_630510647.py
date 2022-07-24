def round_to_int(x):
    if x >= 0:
        if (x % 1) > 0:
            if (x % 1) < 0.5:
                x = int((x - (x%1))//1)
                return x
            else: #(x % 1) >= 0.5
                x = int(((x - (x%1))//1)+1)
                return x
        else: #(x % 1) = 0
            x = int(x//1)
            return x
    else: #x < 0
        if ((abs(x)) % 1) > 0:
            if ((abs(x)) % 1) < 0.5:
                x = int((((x - (x%1))//1)+1)- ((x%1)//1)*2)
                return x
            else:
                x = int(((x - (x%1))//1)- ((x%1)//1)*2)
                return x
        else:
            x = int(x)
            return x
def main():
    x = float(input())
    number = round_to_int(x)
    print(number)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab04_4
