def my_max_mid_min(a, b, c):
    if a > b:
        max_ = a
        min_ = b
        
    else:
        max_ = b
        min_ = a
        
    if c > max_:
        max_ = c

    if c < min_:
        min_ = c
   
    mid_ = ((a + b + c) - max_) - min_

    print('max =',max_,'\nmid =',mid_,'\nmin =',min_)
        
   
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_max_mid_min(a,b,c)
    

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab04_2

