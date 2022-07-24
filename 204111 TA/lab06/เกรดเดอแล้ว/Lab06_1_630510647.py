def int_power(x, y):
    n = x
    if x % 1 == 0: #จำนวนเต็ม
        if y > 0: #กำลังบวก
            for i in range(y-1):
                x = x*n
                
            return x

        elif y < 0: #กำลังลบ
            for i in range((abs(y)-1)):
                x = (x)*(n)

            x = 1/x      
            return x

        else:
            x = 1
            
            return x

    else:
        if y > 0: #กำลังบวก
            for i in range(y-1):
                x = x*n
                
            return x
        elif y < 0: #กำลังลบ
            for i in range((abs(y)-1)):
                x = x*n
                
            x = 1/x  
            return x
        else:
            x = 1

            return x

            
    

def main():
    x = float(input())
    y = int(input())
    print(int_power(x, y))
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab06_1
