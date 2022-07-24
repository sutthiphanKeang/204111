def life_path(n):
    x = (next_life(n))
    while x > 9:
       x = next_life(x)
    return x
       

def next_life(life):
    sum_ = 0
    while life != 0:
       num = life % 10
       life = life // 10
       sum_ += num
    return sum_

def main():
    n = int(input())
    x = (life_path(n))
    print(x)
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab07_4
