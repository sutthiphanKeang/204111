import math
def float_to_bin(x):
    number = 0
   
    y = x
    x = abs(x)
    
    bird = x // 1
    i = 0
    while bird > 0:
        n = bird % 2
        number += (n*(10**i))
        bird = bird // 2
        i += 1
    

    bird2 = x - (x // 1)
    for i in range(1,7):
        r = math.floor(bird2 * 2)
        number += (r*(10**((-1) * i)))
        if (bird2*2) >= 1:
            bird2 = (bird2*2) - 1
        else: 
            bird2 = (bird2*2)
    if y < 0 :
        number *= -1
    
    return number


def main():
    x = float(input())
    print(float_to_bin(x))
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab06_2
