def prime_number(x): #หาจำนวนเฉพาะ
    i = 2
    while i <=(x**0.5):
        if x % i == 0:
            return False
        i += 1
    return True

def sum_prime_in_range(x, y):
    sum_ = 0
    for i in range(x, y + 1):
        if prime_number(i) == True: #เช็คว่าตั้งแต่ x ถึง y ตัวไหนบ้างที่เป็นจำนวนเฉพาะ ถ้าเป็นเอาบวกใน sum
            sum_ += i
    return sum_

def main():
    x = int(input())
    y = int(input())
    print(sum_prime_in_range(x, y))
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab07_1
