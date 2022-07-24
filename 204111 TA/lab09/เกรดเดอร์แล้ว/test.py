a = ["apple","papaya","banana","orange","watermelon"]
char = input("")
count = 0
list_all = list(a[0]) + list(a[1]) + list(a[2]) + list(a[3]) + list(a[4])
count += list_all.count(char) 

print("{0} occurs {1} times in List a".format(char,count))