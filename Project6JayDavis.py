iteration = int(input("n: "))
presumm = 0
div = 1
sign = True
#true statement test do not use; use : in iteration 
for i in range(iteration):
    presumm = presumm + 1 / div if sign else presumm - 1 / div
    div += 2
    sign = not sign
#now use presum x 4 to make pi
pi = presumm * 4
print(pi)
