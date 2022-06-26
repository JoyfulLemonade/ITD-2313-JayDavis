distanceValue = int(input("Enter distance value: "))
message = input("Enter a message: ")
result = ""
for x in message:
    result += chr(ord(x)+distanceValue)
    print(""+result)
#CEAAAASARRR - Joseph Joestar
