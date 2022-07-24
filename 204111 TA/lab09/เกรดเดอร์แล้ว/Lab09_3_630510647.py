def is_prime(n): #main function
    return prime(n, x = 2)

def prime(n, x = 2):#help function
    if n == 2: #basecase เมื่อ n = 2 คืนค่า True
        return True
    if (n % x == 0): #basecase เมื่อ n % 2 = 0 คืนค่า False
        return False
    if (x + 1 > int(n**0.5)): #basecase เมื่อ x + 1 มากกว่า รากที่สองของ n คืนค่า True
        return True
    else:
        return prime(n, x + 1) #เปลี่ยนค่าฟังก์ชั่น


def main():
    n = int(input())
    print(is_prime(n))
    

if __name__ == '__main__' :
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab09_3
