from package1 import plus_minus
from package1 import mult,div
import math
while True:
    ch = int(input("""
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Square
6.Squareroot
7.Cube
8.Cuberoot
9.Exit
Enter Choice:"""))

    if ch == 1:
        num=int(input("Enter First number:"))
        num1=int(input("Enter Second number:"))
        plus_minus.add_num(num,num1)
    elif ch == 2:
        num = int(input("Enter first number"))
        num1 = int(input("Enteer second number"))
        plus_minus.sub_num(num,num1)
    elif ch == 3:
        num = int(input("Enter first number"))
        num1 = int(input("Enter second number"))
        mult.mult_num(num,num1)
    elif ch == 4:
        num = int(input("Enter First number:"))
        num1 = int(input("Enter second number:"))
        div.div_num(num,num1)
    elif ch == 5:
        num = int(input("Enter number"))
        print(math.pow(num,2))
    elif ch == 6:
        num = int(input("Enter number:"))
        print(math.sqrt(num))
    elif ch == 7:
        num = int(input("Enter number"))
        print(math.pow(num,3))
    elif ch == 8:
        num = int(input("Enter number"))
        print(math.pow(num,1/3))
    elif ch == 9:
        print("VISIT AGAIN!!")
        break
    else:
        print("INVALID INPUT!!")
        break

















    
