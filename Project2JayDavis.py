cipher = input("Enter your coded text: ")
distance = int(input("Enter distance value: "))
result = ""
for ch in cipher:
    result += chr(ord(ch)-distance)
    print("" + result)
#ZA WORLDO -DIO
