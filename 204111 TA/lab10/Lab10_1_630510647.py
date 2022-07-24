import string
def is_anagram(str1, str2):
    new_str1 = ''.join(sorted(list(str1.lower()))) #เรียงลำดับข้อความที่ 1 โดยแปลงเป็นตัวเล็ก และเรียงลำดับตามตัวอักษร
    new_str2 = ''.join(sorted(list(str2.lower()))) #เรียงลำดับข้อความที่ 2 โดยแปลงเป็นตัวเล็ก และเรียงลำดับตามตัวอักษร
    new_str1_nowhite = ''
    new_str2_nowhite = ''
    for i in new_str1: #ทำลูปแยก whitespace, punctuation และ digits ออกจากข้อความที่ 1
        if i not in string.whitespace and i not in string.punctuation and i not in string.digits:
            new_str1_nowhite += i

    for i in new_str2: #ทำลูปแยก whitespace, punctuation และ digits ออกจากข้อความที่ 2
        if i not in string.whitespace and i not in string.punctuation and i not in string.digits:
            new_str2_nowhite += i
    
    if new_str1_nowhite == new_str2_nowhite: #เทียบระหว่างข้อความที่ 1 และ 2 ถ้าเท่ากันคืนค่า True ถ้าไม่เท่าคืนค่า False
        return True
    else:
        return False


def main():
    str1 = input()
    str2 = input()
    print(is_anagram(str1, str2))


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab10_1