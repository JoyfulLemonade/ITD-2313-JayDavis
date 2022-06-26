file_name = input('Enter input filename: ')
try:
    file = open(file_name, 'r')
except:
    print('Error opening file ' , file_name)#print message
exit()
print('{:<12s} {:>10s} {:>10s}'.format('Name', 'Hours', 'Total Pay'))
for l in file.readlines():
    name, hour, wages = l.split()

hour = int(hour)
wages = float(wages)
total = hour * wages

print('{:<12s} {:>10d} {:>10.2f}'.format(name, hour, total))

file.close()#close file
