def gcd(x, y):
    if y == 0: #basecase ถ้า % y จนมีค่าเท่ากับ0 ให้คืนค่า x
        return x
    
    else:
        return gcd(y, x % y) #เปลี่ยนค่าฟังก์ชั่น เปลี่ยนให้ x % y เป็น y และ ั เป็น x จบกว่าจะเข้า basecase


def main():
    x = int(input())
    y = int(input())
    print(gcd(x, y))
        
     

if __name__ == "__main__":
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab09_1
