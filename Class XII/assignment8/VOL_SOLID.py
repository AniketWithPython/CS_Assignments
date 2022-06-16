#assignment8

import math as m

def vol_cuboid(length,breadth,height):
    vol=length*breadth*height
    return vol
    
def vol_cylinder(radius,height):
    vol=height*m.pi*radius**2
    return vol

def vol_cone(radius,height):
    vol=(1/3)*height*m.pi*radius**2
    return vol
