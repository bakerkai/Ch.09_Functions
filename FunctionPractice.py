import math

def volume_sphere(radius):
    '''this function calculates the volume of the sphere'''
    volume = 4/3 * math.pi *math.pow(radius,3)
    print(f"The volume of the sphere is... {volume:.2f}")

#volume_sphere(int(input(print("What is the radius?"))))

def volume_scyl(r,h):
    volume =math.pi *math.pow(r,2)*h
    return volume

def hyp(leg1,leg2):
    hypot = math.sqrt(leg1**2 + leg2**2)
    print(hypot)

def mean(list):
    total =0
    for item in list:
        total += item
    avg = total/len(list)
    print(avg)

def perimeter(b,h):
    per = 2*b +2*h
    print(per)

def myprogram():
    hyp(1,2)
    numlist=[13,2,54,23,34,71]
    mean(numlist)

print(__name__)
if __name__ == "__main__":
    myprogram()
'''
 volume_sphere(4)
    vol24 = 24 * volume_scyl(2, 3)
    print(vol24)
    '''