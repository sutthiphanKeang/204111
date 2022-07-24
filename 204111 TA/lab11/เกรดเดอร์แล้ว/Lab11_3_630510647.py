def is_magic_square(board):
    main_num = sum(board[0])
    result = []
    all_col = []
    coll = []
    sum_x1 = []
    sum_x2 = []
    if find_num(board) is True and find_num_n2(board) is True: #ตรวจสอบว่า list ไม่มีเลขซ้ำกันทั้งหมด และ เลขใน list มีค่าไม่เกิน n^2
        sum_row = list(map(lambda x: sum(x), board)) #หาผมรวมของแถวท้งหมด

        for row in range(len(board)): #loop เพื่อ ต้องการcol มาไว้ใน list เดียวกัน
            for col in range(len(board)):
                coll += [board[col][row]]
            all_col.append(coll)
            coll = []

        sum_col = list(map(lambda x: sum(x), all_col)) #นำlistที่ได้มาหาผมรวมทั้งหมด จะเป็นผมรวมของหลัก


        for i in range(len(board)): #หาผลรวมของตำแหน่ง i == j 
            for j in range(len(board)):
                if i == j:
                    sum_x1 += [board[i][j]]
        sum_x1 = sum(sum_x1) 

        for i in range(len(board)): #หาผลรวมของตำแหน่ง i + j == n - 1
            for j in range(len(board)):
                if i + j == len(board) - 1:
                    sum_x2 += [board[i][j]]
        sum_x2 = sum(sum_x2)

        result = sum_row + sum_col + [sum_x1] + [sum_x2] #นำข้อมูลทัั้งหมด มารวมเป็น list เดียว


        for i in result: #ตัวสอบว่าทุกตัวเท่ากันไหม
            if i == main_num:
                continue
            elif i != main_num:
                return False
        return True

    else:
        return False


def find_num(x): #หาเลขซ้ำ
    row = []
    for i in x: #แยกเพื่อให้อยู่ใน list เดียวกัน
        row += i

    for j in row:
        if j == row[0]: #ตรวจสอบว่าตัวเลขนั้นเท่ากับตัวแรก
            continue
        elif j != row[0]: #ตรวจสอบว่าตัวเลขนั้นไม่เท่ากับตัวแรก
            return True
    return False

def find_num_n2(x): #หาเลขที่เกิน n^2
    row = []
    for i in x: #แยกเพื่อให้อยู่ใน list เดียวกัน
        row += i

    for j in row:
        if j > (len(x[0]) ** 2): #ตรวจสอบว่าตัวเลขนั้นมีค่ามากกว่า n^2
            return False
    return True



def main():
    #board = input()
    board = [[3, 8, 7],[10, 6, 2],[5, 4, 9]]

    print(is_magic_square(board))


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab11_3