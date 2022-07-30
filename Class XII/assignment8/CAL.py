#assignment8

import CIRCLE 
import RECTANGLE
import VOL_SOLID

def main():
    yn='y'
    while yn in 'Yy':
        choice=input('''Enter function to use:
1. ar_circle
2. circum_circle
3. area_rec
4. peri_rec
5. vol_cuboid
6. vol_cylinder
7. vol_cone
''')
        if choice=="1":
            r=float(input("Enter radius: "))
            ans=CIRCLE.ar_circle(r)           
        elif choice=="2":
            r=float(input("Enter radius: "))
            ans=CIRCLE.circum_circle(r)          
        elif choice=="3":
            l=float(input("Enter length: "))
            b=float(input("Enter breadth: "))
            ans=RECTANGLE.area_rec(l,b)          
        elif choice=="4":
            l=float(input("Enter length: "))
            b=float(input("Enter breadth: "))
            ans=RECTANGLE.peri_rec(l,b)           
        elif choice=="5":
            l=float(input("Enter length: "))
            b=float(input("Enter breadth: "))
            h=float(input("Enter height: "))
            ans=VOL_SOLID.vol_cuboid(l,b,h)           
        elif choice=="6":
            r=float(input("Enter radius: "))
            h=float(input("Enter height: "))
            ans=VOL_SOLID.vol_cylinder(r,h)           
        elif choice=="7":
            r=float(input("Enter radius: "))
            h=float(input("Enter height: "))
            ans=VOL_SOLID.vol_cone(r,h)           
        else:
            print("Invalid input. Try again")
            continue
        print("value is:",ans)
        yn=input("Do you want to continue?(y/n): ")

if __name__=="__main__":
    main()
