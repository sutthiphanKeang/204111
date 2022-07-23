import math
def find_r_from_surface_area(surface_area):
    radius = ((surface_area)/(4*math.pi))**0.5
    return radius

def sphere_volume(radius):
    volume = (4/3)*(math.pi*(radius)**3)
    return volume

def main():
    surface_area = float(input("input surface area: "))
    radius = find_r_from_surface_area(surface_area)
    volume = sphere_volume(radius)
    print("volume = {0:.2f}".format(volume))

if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab03_1


