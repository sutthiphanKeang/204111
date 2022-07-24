def power_set(set_a):
    list_set = list(set_a)
    all_sup_set = [()] #เริ่มจากเซตว่าง
    ans_set = []
    
    for i in list_set:
        for j in range(len(all_sup_set)): #loop นี้จะทำ set ตามลำดับ จาก 1 ไป ถึง len(all_sup_set) เพราะมีการเปลี่ยนค่าของ all_sup_set j จึงเปลี่ยน
            sub_set = all_sup_set[j] #เรียกตำแหน่งใน all_sup_set
            #print('j',j)
            #print(sub_set)
            sub_set += (i,) #บวก tuple ต้องมี ,
            #print(':::',sub_set)
            all_sup_set.append(sub_set)
            #print('all',all_sup_set) 

        #print(all_sup_set)
    
    for i in all_sup_set: #ทำให้ tuple เป็น set
        x = set(i)
        ans_set.append(x)

    return ans_set

#[set(), {'a'}, {'c'}, {'a', 'c'}, {'b'}, {'a', 'b'}, {'c', 'b'}, {'a', 'c', 'b'}]

def main():
    set_a = {'a', 'b', 'c'}
    print(power_set(set_a))

if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab13_2