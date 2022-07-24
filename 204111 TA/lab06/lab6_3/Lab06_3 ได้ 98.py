#import math
def prime_number(x):
    x = abs(x)
    i = 2
    while i <= (x**0.5)+1:
        if x % i == 0:
            return False
        i += 1
    return True


def factorize(x):
    prime = prime_number(x)
    if x == 0:
        print ('0 is 0')
        #print('พัก1')
    if x == 1:
        print ('1 is 1')
        #print('พัก2')
    if x == 2:
        print ('2 is prime', end="")
        #print('พัก3')
    if prime == True and x != 1 and x != 2:
        print (x,'is prime', end="")
        #print('พัก4')
    else:
        if x != 1 and x != 2:
            print(x,"is", end=" ")
            #print('พัก5')
            while x % 2 == 0 and x != 2 and x != 0 and x != 1: 
                print ("2", end = " * ")
                #print('พัก6')
                x = x / 2 
            for i in range(3, int((x**0.5)+1), 2):
                if prime_number(i) == False:
                    continue
                while x % i == 0: 
                    x = x // i
                    if x == 1:
                        print(i, end="")
                        #print('พัก7')
                        break
                    else:
                        print(i, end=" * ")
                        #print('พัก8')
                
            if x >= 2: 
                print(int(x), end="")
                #print('พัก9')
    print()




def main():
    x = int(input())
    (factorize(x))
    #print(prime_number(x))
    print()
    main()
    

    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab06_3
