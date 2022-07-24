import string
def patterned_message(message, pattern):
    #ทำลูปในแยก * ออกจาก pattern และเพื่อทำตามครั้งที่มี * ด้วย
    for flower in pattern:
        #ลูปแยกสิ่งที่อยู่ในmessage 
        for work in message:
            #ถ้าใน message มี * ให้เปลี่ยนเป็น / และ flower ต้องไม่ใช่" "
            if work == '*' and flower not in string.whitespace:
                new = pattern.replace('*', '/', 1)
                pattern = new
            #เทียบถ้า work และ flower ไม่ใช่ whitespace ให้แทน work ลงใน pattern
            elif work not in string.whitespace and flower not in string.whitespace:
                new = pattern.replace('*', work, 1)
                pattern = new
                
    #เปลี่ยน / คืนเป็น *            
    pattern = pattern.replace('/', '*')
    print(pattern)

def main():
    message = str(input())
    pattern = str(input())
    patterned_message(message, pattern)
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_3
