def kth_digit(number,k):
    nnum_1 = (number//10**k)%10
    return nnum_1

def set_kth_digit(number,k,value):
    nnum_2 = (abs(number)+((value)-((abs(number)//10**k)%10))*(10**k))
    return nnum_2

def main():
    number = int(input())
    k = int(input())
    value = int(input())
    nnum_1 = kth_digit(number,k)
    nnum_2 = set_kth_digit(number,k,value)
    print(nnum_1, type(nnum_1), nnum_2, type(nnum_2))

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab03_5
