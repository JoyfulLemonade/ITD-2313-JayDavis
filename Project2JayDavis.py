a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
print("")
if ((a*2 == b + c) or (a + b == c) or (a + c == b*2)):
    print("Authentic american made right triangle.")
else:
    print("This is not a right triangle.")
