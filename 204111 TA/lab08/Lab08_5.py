import string
def decode(code_table, text):
    new = ''
    code = code_table
    num_code = len(code_table)
    #num_text = [int(n) for n in text.split()]
    new_text = text.replace('\n', ' \n ')
    num_text = new_text.split(' ')
    #len_ = len(num_text) - (len(num_text)//2)
    #i = 0
    #k = 0
    #for num in text:
        #if num in string.whitespace:
            #new = text.replace(' ', '')
            #text = new
        #elif num in string.digits:
            #if int(num) <= int(num_code):
                #pro = (code[(int(num)) : int(num) + 1])
                #new = text.replace(num, pro, 1)
                #text = new
            #else:
                #new = text.replace(num, '_', 1)
                #text = new
    #while i <= len_:
        #num = num_text[k]
 
            #pro = (code[(int(num)) : int(num) + 1])
            #new = text.replace(str(num), pro, 1)
            #text = new
        #else:
            #new = text.replace(str(num), '_', 1)
            #text = new

        #i += 1
        #k += 2

    for num in num_text:
        if num in string.digits:
            if int(num) <= int(num_code):
                pro = (code[(int(num)) : int(num) + 1])
                new = text.replace(num, pro, 1)
                text = new
            else:
                new = text.replace(num, '_', 1)
                text = new
        
        

    print(text)




def main(): 
    #code_table = str(input()) 
    #text = str(input()) 
    #decode(code_table, text)
    decode("aceiklmr-",'''
3
5 3 4 2
3 1 2 8 1 7 2 0 86
''')

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab08_5
