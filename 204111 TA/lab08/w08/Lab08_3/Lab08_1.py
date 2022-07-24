def square_frame(n, sep=' '):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                if j < 10:
                    print("0", end="")
                print(str(j), end="")
                if j != n:
                    print(sep, end="")
            elif i == n:
                num = (3 * n) - 2 - j + 1
                if num < 10:
                    print("0", end="")
                print(str(num), end="")
                if j != n:
                    print(sep, end="")
            elif j == n:
                num = n + 1 + i - 2
                if num < 10:
                    print("0", end="")
                print(str(num), end="")
            elif j == 1:
                num = (4 * n) - 4 - i + 2
                if num < 10:
                    print("0", end="")
                print(str(num), end=sep)
            else:
                print(sep+sep, end=sep)
        print("")


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_1
