def polynomial_addition(p1, p2):
    result = []
    d1 = dict()
    d2 = dict()
    for i in p1:
        d1[i[0]] = i[1]
    
    for i in p2:
        d2[i[0]] = i[1]

    num_key1 = []
    num_key2 = []
    for i in d1:
        num_key1.append(i)

    for i in d2:
        num_key2.append(i)
 
    for i in num_key1:
        if i in num_key2:
            if d2[i] == (d1[i] * -1):
                del d1[i]
                del d2[i]
            elif d1[i] == (d2[i] * -1):
                del d1[i]
                del d2[i]
            else:
                x = d1[i]
                y = d2[i]
                new = x + y
                del d1[i]
                del d2[i]
                d1[i] = new

    for i in d2:
        x = d2[i]
        d1[i] = x
    
    all_key = []
    for i in d1:
        all_key.append(i)

                
    for i in all_key:
        result += [(i,d1[i])]
    
    awesome = sorted(result, reverse = True)
    return awesome
    
   


def main():
    p1 = [(2, 6), (1, 34), (0, -8)]
    p2 = [(2, -6), (0, 2), (1, 1)]
    print(polynomial_addition(p1, p2))



if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab12_4