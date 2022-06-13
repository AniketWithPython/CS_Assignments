#assignment8

from math import pi

def vol_cuboid(length,breadth,height):
    vol=length*breadth*height
    return vol
    
def vol_cylinder(radius,height):
    vol=height*pi*radius**2
    return vol

def vol_cone(radius,height):
    vol=(1/3)*height*pi*radius**2
    return vol
