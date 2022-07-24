import copy
def matrix_mult(m1, m2):
    roww = []
    coll = []
    all_list = []
    i = 0
    sum_ = 0
    list_m1 = copy.deepcopy(m1)
    list_m2 = copy.deepcopy(m2)

    for row in list_m1:
         roww += row

    for i in range(len(list_m2) - 1): 
        for col in range(len(list_m2)):
            coll += [list_m2[col][i]]
        i += 1
        
    if len(roww) == len(coll):
        for i in range(len(list_m1)):
            for j in range(len(list_m2[0])):
                for k in range(len(list_m2)):
                    sum_ += (list_m1[i][k] * list_m2[k][j])
                all_list.append(sum_)
                sum_ = 0
        return all_list

    else:
        return None
         
    #print(m1[0][0], m1[0][1], m1[0][2])
    #print(m2[0][0], m2[1][0], m2[2][0])
    #print("->" , m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0] + m1[0][2]*m2[2][0])
    #print(" ")
    #print(m1[0][0], m1[0][1], m1[0][2])
    #print(m2[0][1], m2[1][1], m2[2][1])
    #print("->" , m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1] + m1[0][2]*m2[2][1])
    #print(" ")
    #print(m1[1][0], m1[1][1], m1[1][2])
    #print(m2[0][0], m2[1][0], m2[2][0])
    #print("->" , m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0] + m1[1][2]*m2[2][0])
    #print(" ")
    #print(m1[1][0], m1[1][1], m1[1][2])
    #print(m2[0][1], m2[1][1], m2[2][1])
    #print("->" , m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1] + m1[1][2]*m2[2][1])

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[7, 8], [9, 10], [11, 12]]
    print(matrix_mult(m1, m2))


if __name__ == '__main__':
    main()