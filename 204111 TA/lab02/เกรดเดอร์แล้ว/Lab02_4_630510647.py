x = int(input('Input number of milliseconds: '))
d = 0
h = 0
m = 0
s = 0
while x >= 86400000 :
    x -= 86400000
    d += 1
else :
    while x >= 3600000 :
        x -= 3600000
        h += 1
    else :
        while x >= 60000 :
            x -= 60000
            m += 1
        else :
            while x >= 1000 :
                x -= 1000
                s += 1
print('Results =',d,'day(s),',h,'hour(s),',m,'minute(s),',s,'second(s), and',x,'millisec(s)')
#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab02_4
