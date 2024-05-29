print("----------Area Calculator-----------")
print("""Click 1 to get Area of Square
Click 2 to get Area of Circle
Click 3 to get Area of Rectangle
Click 4 to get Area of triangle
Click 5 to get Area of Cube
Click 6 to get Area of Cuboid
""")


choice = float(input("enter a number between 1-6:"))

print("----------------------------------------")
if choice == 1:
    print("Formula of Square = Area * Area")
    Area = float(input("Enter your Area = "))
    print(Area * Area)
    print("___________Thank you, Have a Nice Day___________")

elif choice == 2:
    print("Formula of Circle = 3.14 * Radius * Radius")
    Radius = float(input("Enter Your Radius = "))
    print(3.14 * Radius * Radius)
    print("___________Thank you, Have a Nice Day___________")
elif choice == 3:
    print("Formula of Rectangle = Length * Breath")
    Length = float(input("Enter Your Length = "))
    Breath = float(input("Enter Your Breath = "))
    print(Length * Breath)
    print("___________Thank you, Have a Nice Day___________")
elif choice == 4:
    print("Formula of Triangle = 1/2(Base * Height)")
    Base = float(input("Enter Your Base = "))
    Height = float(input("Enter Your Height = "))
    print(1/2*Base*Height)
    print("___________Thank you, Have a Nice Day___________")
elif choice == 5:
    print("Formula of Cube = 4 * Area")
    Area = float(input("Enter Your Area = "))
    print(4* Area)
    print("___________Thank you, Have a Nice Day___________")

elif choice == 6:
    print("Formula of Cuboid = 2*h(Length + Breath")
    Heig = float(input("Enter Your Height = "))
    Len = float(input("Enter Your Length = "))
    Breath = float(input("Enter Your Breath = "))
    print(2 * Heig *Len + Breath)
    print("___________Thank you, Have a Nice Day___________")


else:
    print("")
    print("Please Enter Number Between 1 to 6")
    print("___________Thank you, Have a Nice Day___________")
