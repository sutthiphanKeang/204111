import string
def decode(code_table, text):
    new = ''
    code = code_table
    num_code = len(code_table) - 1
    new_text = text.replace('\n', ' \n ') 
    num_text = new_text.split(' ')#นำข้อมูลมาใส่ใน list

    #แยกเลขกับ \n ออกมาจาก list
    for num in num_text:
        if num == '\n': #ตรวจสอบว่าเป็น \n 
            new += '\n'
            continue
        
        elif num not in string.whitespace: #ตรวจสอบว่าเป็นเลข
            if int(num) >= 0: #ตรวจสอบกรณีที่เลขไม่ติดลบ
                if int(num) <= int(num_code): #เลขยังอยู่ในจำนวนคำ
                    new += (code[(int(num)) : int(num) + 1])
                    text = new
                elif int(num) > int(num_code): #เลขไม่อยู่ในจำนวนคำ
                    new += '_'
                    text = new
            elif int(num) < 0: #ตรวจสอบกรณีที่เลขติดลบ
                new += '_'
                text = new
                
    print(text)


def main(): 
    code_table = str(input()) 
    text = str(input()) 
    decode(code_table, text)
   
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_5
