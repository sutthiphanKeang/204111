def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
    if l2 > (l1 + w1):
        return False
    elif (l2+w2) < l1:
        return False
    elif t2 > (t1 + h1):
        return False
    elif (t2 + h2) < t1:
        return False
    else:
        return True



def main():
    l1,t1,w1,h1,l2,t2,w2,h2 = input( ).split( )
    l1 = float(l1)
    t1 = float(t1)
    w1 = float(w1)
    h1 = float(h1)
    l2 = float(l2)
    t2 = float(t2)
    w2 = float(w2)
    h2 = float(h2)
    number = is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2)
    print(number)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab05_4
    
