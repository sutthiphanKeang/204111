def zodiac_element(year):
    if year % 12 == 0:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Monkey')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Monkey')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Monkey')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Monkey')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Monkey')

def main():
    year = int(input())
    print(zodiac_element(year))
    

if __name__ == '__main__':
    main()
