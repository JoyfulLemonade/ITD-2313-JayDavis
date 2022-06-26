height = int(input("Enter the height from which the ball is yeeted: "))
bounceIndex = float(input("Enter the bounciness: "))
numberOfBounces = float(input("Enter how many times the ball is allowed to bounce: "))
#start point 0
distance = 0
#while not for for bouncy balls bounce
while numberOfBounces > 0:
    distance = distance + height
    height = height * bounceIndex
    distance = distance + height
    numberOfBounces-= 1
#give me information oh divine program
print("Total distance is:",distance ," bounce units.")
