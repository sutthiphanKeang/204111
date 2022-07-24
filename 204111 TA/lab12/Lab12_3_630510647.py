def prime_factor(n):
    i = 2
    all_ = []
    while i <= (n ** 0.5): #หาfactor ที่เป็นเลข prime
        if  n % i == 0:
            all_.append(i) #เพิ่มเข้า list
            n //= i
        else:
            if i % 2 == 0: #จำกัด i ที่เอามาหาร
                i += 1
            else:
                i += 2
    if n == 1:
        all_ = []
    else:
        all_.append(int(n)) #เพิ่มเข้า list
    return all_

def coprime_factor(a, b):
    list_a = prime_factor(a) #เรียกฟังก์ชั่นหาตัวประกอบเฉพาะ
    list_b = prime_factor(b) #เรียกฟังก์ชั่นหาตัวประกอบเฉพาะ
    all_ = []
    for i in list_a: #ใช้ list_a เป็นหลักในการหาเลขซ้ำ
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