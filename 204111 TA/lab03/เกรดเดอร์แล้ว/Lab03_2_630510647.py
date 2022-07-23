def reverse_digits(x):
    re_number = 0
    re_number = (re_number *10)+(x%10) 
    x = x//10 
    re_number = (re_number *10)+(x%10) 
    x = x//10 
    re_number = (re_number *10)+(x%10) 
    x = x//10 
    re_number = (re_number *10)+(x%10) 
    x = x//10
    return re_number

def main():
    x = int(input())
    re_number = reverse_digits(x)
    print(format(re_number))

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab03_2
