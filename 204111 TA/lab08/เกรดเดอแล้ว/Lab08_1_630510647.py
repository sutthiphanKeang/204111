def square_frame(n, sep=' '):
    for i in range(1, n + 1): #ทำพิกัด i
        for j in range(1, n + 1): ##ทำพิกัด j
            if i == 1: #ทำแถวบนสุด
                if j < 10: #ตรวจสอบว่าถ้าน้อยกว่าสุดต้องบวก 0 ไปข้างหน้า
                    print("0", end="")
                print(str(j), end="")
                if j != n: #แกป้องใส่ sep ไปข้างสุด
                    print(sep, end="")
            elif i == n: #ทำแถวล่างสุด
                num = (3 * n) - 2 - j + 1 #สูตรจากลำดับเลขคณิต
                if num < 10: #ตรวจสอบว่าถ้าน้อยกว่าสุดต้องบวก 0 ไปข้างหน้า
                    print("0", end="")
                print(str(num), end="")
                if j != n: 
                    print(sep, end="")
            elif j == n:#ทำแถวขวามือ
                num = n + 1 + i - 2
                if num < 10: #ตรวจสอบว่าถ้าน้อยกว่าสุดต้องบวก 0 ไปข้างหน้า
                    print("0", end="")
                print(str(num), end="")
            elif j == 1: #ทำแถวซ้ายมือ
                num = (4 * n) - 4 - i + 2 #สูตรจากลำดับเลขคณิต
                if num < 10: #ตรวจสอบว่าถ้าน้อยกว่าสุดต้องบวก 0 ไปข้างหน้า
                    print("0", end="")
                print(str(num), end=sep)
            else:
                print(sep+sep, end=sep)
        print("")


def main():
    square_frame(n, x)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_1
