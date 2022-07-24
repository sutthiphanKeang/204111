def series(n):
    if n == 0: #basecase เมื่อ n = 0 ให้คืนค่า 0 ไปบวก
        return 0
    else:
        if n % 2 == 0: #หาตำแหน่งที่จะใช้สูตรลำดับเลขคณิต 
            return abs(2*(series(n - 1)) + 1) #เมื่อ n % 2 = 0 จะบวก 1
        else:
            return abs(2*(series(n - 1)) - 1) #เมื่อ n % 2 != 0 จะลบ 1


def main():
    n = int(input())
    for i in range(n + 1):
        try_ = str(series(i))
        
    print(try_)
     

if __name__ == "__main__":
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab09_4