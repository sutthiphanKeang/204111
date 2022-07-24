def longest_digit_run(n):
    sum_ = 1
    num_ = 1 
    while n // 10 != 0:
        num_1 = n % 10
        n = n // 10
        if num_1 == (n % 10):
            sum_ += 1
            
        elif num_1 != (n % 10):
             sum_ = 1

        if sum_ > num_:
            num_ = sum_
        elif sum_ < num_:
            num_ = num_

    
    return num_



def main():
    n = int(input())
    print(longest_digit_run(n))
    
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab06_5
