#assignment9
import pack_vehicle

def main():
    yn='y'
    while yn in 'Yy':
        choice=input('''Enter function to use:
1. distance
2. speed
3. energy
''')

        if choice=="1":
            #distance
            u=float(input("Enter initial velocity: "))
            a=float(input("Enter acceleration: "))
            t=float(input("Enter time: "))
            ans=pack_vehicle.veh_distance.distance(u,a,t)
        elif choice=="2":
            #speed
            d=float(input("Enter distance: "))
            t=float(input("Enter time: "))
            ans=pack_vehicle.veh_speed.speed(d,t)          
        elif choice=="3":
            #energy
            m=float(input("Enter mass: "))
            v=float(input("Enter velocity: "))
            ans=pack_vehicle.veh_energy.energy(m,v)
        else:
            print("Invalid input. Try again")
            continue
        print("value is:",ans)
        yn=input("Do you want to continue?(y/n): ")

main()
