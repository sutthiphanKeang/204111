import copy
def matrix_mult(m1, m2):
    roww = []
    coll = []
    all_list = []
    wait_list = []
    sum_ = 0
    list_m1 = copy.deepcopy(m1) #copy list แบบไม่เปลี่ยน list เดิม
    list_m2 = copy.deepcopy(m2) #copy list แบบไม่เปลี่ยน list เดิม

    for col in range(len(list_m2)): #หาจำนวนหลักที่จะนำมาคูณ
        coll += [list_m2[col][0]]
        
    if len(list_m1[0]) == len(coll): #เทียบ ถ้าหลักเท่ากับแถว สามารถคูณได้้
        for i in range(len(list_m1)):
            for j in range(len(list_m2[0])):
                for k in range(len(list_m2)):
                    sum_ += (list_m1[i][k] * list_m2[k][j]) #เรียกตำแหน่ง i j k มาเรียกตำแหน่งใน list มาคูณกัน
                wait_list += [sum_]
                sum_ = 0
            all_list.append(wait_list)  #นำข้อมูลมาใส่ในall_list
            wait_list = [] #ล้างข้อมูล
        return all_list

    else:
        return None
        
         
    

def main():
    m1 = [[39, 40, 22, 48], [31, 36, 20, 27], [48, 41, -4, 36]]
    m2 = [[29, -5], [22, 27], [34, -6], [38, 16]]
    print(matrix_mult(m1, m2))


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab11_1