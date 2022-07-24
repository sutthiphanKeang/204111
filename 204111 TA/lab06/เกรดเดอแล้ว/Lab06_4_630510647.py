def f(n):
    max_ = 0
    ave_ = 0
    num_ = 0
    run_ = 0
    print('Enter score: ')
    while num_ < n:
        score = int(input())
        try_ = max_
        if score > try_:
            max_ = score
            run_ = try_
            
        elif score < try_:
            max_ = max_
            if score > run_:
                run_ = score


        ave_ += score
        num_ += 1

    print("---")
    print('Max score is: %.2f '%max_)
    if run_ == 0:
        print('Runner up is: None')
    else:
        print('Runner up is: %.2f '%run_)
    print('Average is: %.2f '%(ave_/n))

    
def main():
    n = int(input('Total students: '))
    (f(n))
    
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab06_4
