def n_base_to_10(n, num):
    if num == 0: #basecase จนกว่าnumจะเท่ากับ 0 ให้คืนค่า 0 ไปบวก
        return 0
    else:
        first = int(str(num)[:1])#ตัดเลขตัวแรกออกมา
        num_word = len(str(num)) - 1 #หาจำนวนที่จะยกกำลัง
        x = ((first* (n ** num_word))) #นำเลขแรกมาคูณฐานยกกำลัง
        y = ((n_base_to_10(n, num % 10 ** num_word))) #เปลี่ยนค่าฟังก์ชั่น
        return x + y #คืนค่าเลขฐาน 10

def num_i(num):
    i = 0
    num_word = len(str(num))
    fo


def main():
    n = int(input())
    num = int(input())
    print(n_base_to_10(n,num))
    

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab09_2