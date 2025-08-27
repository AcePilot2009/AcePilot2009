while True:
    print("1.Area of Circle")
    print("2.Area of Rectangle")
    print("3.Area of Triangle")
    print("4.Exit")
    ch = int(input("Choose what you want to find"))
    if ch == 1:
        pi= 3.14 
        r= int(input("Enter the radius of the circle"))
        Area1= pi*r*r
        print("The are of the circle is",Area1)
    elif ch == 2:    
        l= int(input("Enter the length of rectangle"))
        b= int(input("Enter the breadth of rectangle"))
        Area2= l*b 
        print("The are of rectangle is",Area2)
    elif ch == 3:
        b= int(input("Enter the length of base of Triangle"))
        h= int(input("Enter the length of height of Triangle"))
        Area3= 0.5*b*h
        print("The are of triangle is",Area3)
    elif ch == 4:
        print("Exiting the program")
        print("Bye bye")
        break
    else:
        print("Invalid choice. Please select a valid option.")
