filename = input("input file name: ")
outfile = input("output file name: ")
try:
    with open(filename, 'r') as f, open(outfile, 'w') as w:
        for line in f:
            w.write(line)
except FileNotFoundError:
    print(filename + " this doesn't exist!")
