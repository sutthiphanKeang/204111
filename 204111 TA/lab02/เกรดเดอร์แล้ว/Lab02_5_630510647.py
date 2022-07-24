import math
x = int(input('Enter n: '))
g = (1+(5**0.5))/2
f = ((g**x)/(5**0.5))+0.5
n_1 = f//1
n_2 = math.ceil(n_1)
print('fib(%d) = %d'%(x,n_2),end='')
#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab02_5
