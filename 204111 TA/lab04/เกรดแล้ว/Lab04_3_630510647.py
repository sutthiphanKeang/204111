def calculate_p2p_evolve_exp(p, c):
    numc = c//12 #ครั้งที่ได้จาก c
    c = c%12 #ลูกอมที่เหลือ
    exp = 0 #exp

    if p > numc : #ลูกอมมากกว่าเท่ากับนก 
        exp += 500*numc
        p -= numc
        c += numc
    else: #p<numc
        exp += 500*p
        c = 0
        p = 0
    
     #ลูกอมน้อยกว่านก
    if p > 0:
        if p+c > 12:
            p -= 12-c+1
            exp += 500
            c += 1
            
    nump = p//12
    exp += (500*nump)
    return exp
      


def main():
    p = int(input())
    c = int(input())
    number_exp = calculate_p2p_evolve_exp(p, c)
    print(number_exp)
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab04_3

