def kth_digit(number, k):
    nnum = (abs(number)//(10**k))%10
    return nnum
    
def main():
    number = int(input())
    k = int(input())
    nnum = kth_digit(number, k)
    print(nnum, type(nnum))

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab03_4
