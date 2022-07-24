import copy
def remove_row_col(list_a, row, col):
    new_list = copy.deepcopy(list_a) #copy list แบบไม่เปลี่ยน list เดิม
    if row > 0: #ตรวจสอบว่า row เป็นลบ
        if row <= len(new_list) - 1:
            new_list.pop(row) #ตัดแถวนั้นทิ้ง
    else: 
        if abs(row) <= len(new_list):
            new_list.pop(row)
    result = []

    for row in new_list: #แยกlistย่อย
        if col > 0: #ตรวจสอบว่า col เป็นลบ
            if col <= len(row) - 1:
                row.pop(col) #ตัดหลักนั้นทิ้ง
                
        else:
            if abs(col) <= len(row):
                row.pop(col)
        result.append(row) #นำคำตอบมารวมใน result
    return result



def main():
    #list_a = input()
    #row = int(input())
    #col = int(input())
    list_a = [[-90, 792211125, 193211887, 512625, 15946], [2456154, 784544, 3409, -34, 34435650], [86344748, 8595, 10731, 68917423, 790], [-44, 83359668, 5450, 72041837, 8910], [-31, 4732265, 1305918, 86762, 738], [167, 1280174, 9582002, 1613742, 4951079], [807920877, 85, 62, -33, 523030], [2327326, 1699, 477, 12407812, -65], [-26, 34777730, -50, 56968277, 63821884], [114626216, 288719710, -84, 301259, 916114], [52054, 6593, 47865, 6166, -78]]
    row = -13
    col = -7
    print(remove_row_col(list_a, row, col))




if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab11_2