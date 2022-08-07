def mean(list):
    l = len(list)
    i = 0
    sum = 0
    while i<l:
        sum += list[i]
        i+=1
        return sum/l
    def median(list):
     l = len(list)
    list = sorted(list)
    mid = l//2
    if l%2 == 0:
      return(list[mid]+list[mid-1])/2
    else:
        return list[mid]
def mode(list):

    d = dict()
mode = False
modeValue = 0
result = 0
for x in list:
    if(not d.get(x)):
        d[x] = 1
else:
    d[x]+=1
mode = True
if(d[x] > modeValue):
    modeValue = d[x]
    result = x
if(mode):
    return result
    else:
    return "No mode"
def main():
    lst = [3, 1, 7, 1, 4, 10]
print("List:",list)
print("Mode:",mode(list))
print("Median:",median(list))
print("Mean:",mean(list))
main()
