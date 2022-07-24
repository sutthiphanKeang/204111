def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def fac(x):
    i = 2
    while i <= (x**0.5):
        if  x % i == 0: #and is_prime(i):
            x /= i
            print(i, end=" ")
        else:
            i += 1

    print(int(x))

            
    
x = int(input())
fac(x)
    
