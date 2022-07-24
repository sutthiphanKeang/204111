import string
def word_count(text):
    new_text = text.split()
    all_ = []
    wait = []
    re_count = []
    for n in new_text: #นำ\n ออกจากข้อความ
        if '\n' in n:
            if len(n) == 1:
                continue
            else:
                x = n.replace('\n', '')
                re_count.append(x)
        elif '\t' in n:
            if len(n) == 1:
                continue
            else:
                x = n.replace('\t', 't')
                re_count.append(x)
        elif n in string.whitespace: #นำช่องว่างออก
            continue
        else:
            re_count.append(n)

    for i in re_count: #loop เพิ่อตัด punctuation ที่ล้อมรอบ string 
        if i[0] in string.punctuation and i[len(i) - 1] in string.punctuation: #มี punctuation ทั้งหน้าทั้งหลัง
            try_ = ''
            for j in range(len(i)): #ตัดส่วนข้างหน้าก่อน
                if i[j] in string.punctuation:
                    x = (i[j + 1 : ])
                    try_ = x
                    continue  
                else:  
                    break
            for j in range(len(try_)): #ตัดส่วนหลังต่อ
                if try_[len(try_) - (j + 1)] in string.punctuation: 
                    y = (try_[ : len(try_) - (j + 1)])
                    continue
                else:
                    all_.append(y)
                    break
                all_.append(try_)
        elif i[0] in string.punctuation and i[len(i) - 1] not in string.punctuation: #มี punctuation ข้างหน้า
            for j in range(1, len(i)):
                if i[j] in string.punctuation:
                    x = (i[j + 1 : ])
                    continue
                else:
                    all_.append(i[j : ])
                    break
                all_.append(x)
        elif i[0] not in string.punctuation and i[len(i) - 1] in string.punctuation: #มี punctuation ข้างหลัง
            for j in range(1, len(i)):
                if i[len(i) - (j + 1)] in string.punctuation:
                    x = (i[ : len(i) - (j + 1)])
                    continue
                else:
                    all_.append(i[ : len(i) - j])
                    break
                all_.append(x)
        else: #ไม่มี punctuation ทั้งหน้าทั้งหลัง
            all_.append(i)

    for word in all_: #ทำให้ string ทุกตัวเป็นตัวเล็กทั้งหมด
        if word.islower():
            wait.append(word)
        elif word.isdigit():
            wait.append(word)
        else:
            x = word.lower()
            wait.append(x)


    count = 0
    d = dict()
    for i in wait: #นำจำนวนใน dict
        if i in d:
            count = 1 + d[i]
            d[i] = count 
        else:
            d[i] = 1
         
    return d


def main():
    text = """\gh"""
    out = word_count(text)
    print(out)


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab13_3
