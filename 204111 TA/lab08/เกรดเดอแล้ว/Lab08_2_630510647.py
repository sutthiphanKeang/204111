def is_palindrome(x, b):    
    #ขั้นแรก เปลี่ยนเลขตามฐานที่ input เข้ามาโดยการหารฐานนั้นๆ
    i = 0    
    number = 0    
    while x > 0:        
        n = x % b        
        number +=n*(10**i)        
        x = x // b        
        i += 1    
    #ขั้นต่อมาเปรียบเทียบโดยการกลับเลข แล้วเก็บไว้ในอีกตัวแปร 
    old = str(number)    
    dry = old[ : :-1]    

    #นำมาเทียบค่ากัน
    if old == dry:      
        return True   
    else:      
        return False
    
def main():    
    x = int(input())    
    b = int(input())    
    print(is_palindrome(x, b))

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_2
