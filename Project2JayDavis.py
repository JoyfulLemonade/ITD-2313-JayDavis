filename = input('Enter file name: ')
lines = []
with open(filename, 'r') as f:
    for line in f:
        lines.append(line.strip())
while True:
    print("The file has", len(lines), "lines.")
    if len(lines) == 0:
       break
    lineNumber = int(input("\nEnter a line number [0 to quit]: "))
    if lineNumber == 0:
        break
    elif lineNumber > len(lines):
        print("Error: There are not enough lines", len(lines))
else:
    print(lineNumber, ": ", lines[lineNumber - 1])
