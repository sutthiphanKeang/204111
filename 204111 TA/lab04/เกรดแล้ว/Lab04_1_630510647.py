def love6(first, second):
    if first == 6 or second == 6: 
        return True
    elif first + second == 6 or abs(first - second) == 6:
        return True
    else:
        return False   
    
def main():
    first = int(input( ))
    second = int(input( ))
    x = love6(first, second)
    print(x)

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab04_1
