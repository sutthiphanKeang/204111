import math
def prime_number(x):
    x = abs(x)
    i = 2
    while i <= math.sqrt(x)+1:
        if x % i == 0:
            return False
        i += 1
    return True


def factorize(x):
    prime = prime_number(x)
    if x == 0:
        print ('0 is 0')
        #print('พัก1')s
        return
    elif x == 1:
        print ('1 is 1')
        #print('พัก2')
        return
    elif x == 2:
        print ('2 is prime', end="")
        #print('พัก3')
        return
    elif prime == True and x != 1 and x != 2:
        print (x,'is prime', end="")
        #print('พัก4')
        return
    else:
        if x != 1 and x != 2:
            print(x,"is", end=" ")
            #print('พัก5')
            while x % 2 == 0: 
                print ("2", end = " * ")
                #print('พัก6')
                x = x / 2 
            for i in range(3, int(math.sqrt(x))+1, 2):
                while x % i == 0:
                    if prime_number(x) == True:
                        print(int(x), end="")
                        #print('พัก10')
                        continue
                    x = x // i
                    if x == 1 and prime_number(x) != True:
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
