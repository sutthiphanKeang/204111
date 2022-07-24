def sort_date(list_x):
    new_list = []
    result = []
    to_int = []
    to_str = []
    ch = []
    for i in list_x: #นำเครื่อง / ออกจากlist
        new_list.append(i.split('/'))

    for i in range(len(new_list)): #สลับตำแหน่งวันกับปี เพื่อนำมาเรียง
	    for j in new_list[i]:
		    wait = new_list[i][0]
		    new_list[i][0] = new_list[i][2]
		    new_list[i][2] = wait
	    wait = ''

    for i in range(len(new_list)): #เปลี่ยนเลขเป็น int
	    for j in range(len(new_list[i])):
		    ch.append(int(new_list[i][j]))
	    to_int.append(ch)
	    ch = []

    to_int.sort() #เรียงลำดับวันที่

    for i in range(len(to_int)): #สลับตำแหน่งกลับมาให้เหมือนเดิม
	    for j in to_int[i]:
		    wait = to_int[i][0]
		    to_int[i][0] = to_int[i][2]
		    to_int[i][2] = wait
	    wait = ''

    for i in range(len(to_int)): #เปลี่ยน str เป็น int
	    for j in range(len(to_int[i])):
		    ch.append(str(to_int[i][j]))
	    to_str.append(ch)
	    ch = []
    
    for i in to_str: #ใส่เครื่องหมาย / ไปเหมือนเดิม
        try_ = '/'.join(i)
        result.append(try_)

    list_x.clear() 
    for i in result: #ใส่ข้อมูลเข้า list_x
        list_x.append(i)


        



def main():
    list_x =["11/1/2100","5/12/1999","19/1/2003","11/9/2001"]
    sort_date(list_x)
    print("---")
    print(list_x)


if __name__ == '__main__':
    main()


#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab12_1