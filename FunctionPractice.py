import math

def volume_sphere(radius):
    volume = 4/3 * math.pi *math.pow(radius,3)
    print(f"The volume of the sphere is... {volume:.2f}")

#volume_sphere(int(input(print("What is the radius?"))))

def volume_scyl(r,h):
    volume =math.pi *math.pow(r,2)*h
    return volume

volume_sphere(4)
vol = 24*volume_scyl(2,3)
print(vol)
