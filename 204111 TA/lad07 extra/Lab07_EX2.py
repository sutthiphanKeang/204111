def pyramid_stairs(n):
    if n > 0:
        people = (' '*(5*(n-1)) + '  o  ' + '*'*12 + '  o\n')
        people += (' '*(5*(n-1)) + ' /|\ *' + ' '*10 + '* /|\\\n')
        people += (' '*(5*(n-1)) + ' / \ *' + ' '*10 + '* / \\\n')
        #people += (' '*((n * 2)+(2 * (n - 1))-1) + ' '*10 \n')



        for i in range(2,n + 1):
            people += (' '*(5*(n-i)) + '  o  ' + '*'*6 + ' '*(10 * (i - 1)) + '*'*6 + '  o\n')
            people += (' '*(5*(n-i)) + ' /|\ *' + ' '*(10 * i) + '* /|\\\n')
            people += (' '*(5*(n-i)) + ' / \ *' + ' '*(10 * i) + '* / \\\n')
        

        people += ('*'*(12+((n*5)*2)))

        print(people)

  
def main():
    n = int(input())
    pyramid_stairs(n)
    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab07_EX2
