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

    if year % 12 == 1:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Rooster')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Rooster')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Rooster')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Rooster')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Rooster')

    if year % 12 == 2:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Dog')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Dog')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Dog')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Dog')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Dog')

    if year % 12 == 3:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Pig')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Pig')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Pig')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Pig')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Pig')

    if year % 12 == 4:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Rat')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Rat')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Rat')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Rat')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Rat')

    if year % 12 == 5:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Ox')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Ox')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Ox')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Ox')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Ox')

    if year % 12 == 6:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Tiger')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Tiger')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Tiger')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Tiger')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Tiger')

    if year % 12 == 7:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Rabbit')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Rabbit')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Rabbit')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Rabbit')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Rabbit')

    if year % 12 == 8:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Dragon')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Dragon')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Dragon')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Dragon')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Dragon')

    if year % 12 == 9:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Snake')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Snake')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Snake')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Snake')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Snake')

    if year % 12 == 10:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Horse')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Horse')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Horse')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Horse')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Horse')

    if year % 12 == 11:
        if year % 10 == 0 or year % 10 == 1:
            return ('Metal Goat')
        elif year % 10 == 2 or year % 10 == 3:
            return ('water Goat')
        elif year % 10 == 4 or year % 10 == 5:
            return ('Wood Goat')
        elif year % 10 == 6 or year % 10 == 7:
            return ('Fire Goat')
        elif year % 10 == 8 or year % 10 == 9:
            return ('Earth Goat')

def main():
    year = int(input())
    print(zodiac_element(year))
    

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab05_5
