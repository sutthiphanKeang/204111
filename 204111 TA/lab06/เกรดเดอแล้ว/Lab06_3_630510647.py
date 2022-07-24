def prime_number(x):
    i = 2
    while i <=(x**0.5):
        if x % i == 0:
            return False
        i += 1
    return True


def factorize(x):
    if x == 0:
        print ('0 is 0')
    elif x == 1:
        print ('1 is 1')
    elif x == 2:
        print ('2 is prime', end="")
    elif prime_number(x) == True:
        print (x,'is prime', end="")
    else:
        i = 2
        print(x,"is", end=" ")
        while i <= (x**0.5):
            if  x % i == 0 and prime_number(i) == True:
                x /= i
                print(i, end=" * ")
            else:
                i += 1

        print(int(x), end="")

    print()


def main():
    x = int(input())
    (factorize(x))
    #print(prime_number(x))
    print()

    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab06_3            
    

