def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def prime_factor(n):
    i = 2
    all_ = []
    while i <= (n ** 0.5):
        if  n % i == 0: #and is_prime(i):
            n /= i
            all_.append(i)
        else:
            i += 1
    if n == 1:
        all_ = []
    else:
        all_.append(int(n))

    return all_

def coprime_factor(a, b):
    list_a = prime_factor(a)
    list_b = prime_factor(b)
    all_ = []
    for i in list_a:
        if i in list_b:
            all_.append(i)
            list_b.remove(i)
            
    all_.sort()
    return all_

def main():
    print(prime_factor(0))
    print(coprime_factor(180, 48))



if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab12_