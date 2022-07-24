import string
def uniform(line):
    up = 0
    low = 0
    #แยกระหว่างตัวเล็ก กับตัวใหญ่ว่าตัวไหนมากกว่ากัน
    for i in line:
        if i in string.ascii_uppercase:
            up += 1
        elif i in string.ascii_lowercase:
            low += 1

    #ถ้าตัวพิมพ์ใหญ่มากกว่าให้เปลี่ยนข้อความเป็นตัวพิมพ์ใหญ่
    if up > low:
        work = str.upper(line)
    #ถ้าตัวพิมพ์เล็กมากกว่าให้เปลี่ยนข้อความเป็นตัวพิมพ์เล็ก
    elif low > up:
        work = str.lower(line)
    #ถ้าเท่ากันให้ใช้ตัวหน้าสุดเปลี่ยนตัวกำหนด
    else: #low = up
        if line[0:1] in string.ascii_uppercase:
            work = str.upper(line)
        elif line[0:1] in string.ascii_lowercase:
            work = str.lower(line)

    return work


def main():
    x = input()
    print(uniform(x))
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_4
