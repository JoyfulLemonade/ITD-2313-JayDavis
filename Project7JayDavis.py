startsal = int(input("Please enter starting pay: "))
percentup = (float(input("Please enter percentage increase: ")) / 100)
years = list(range(1,(int(input("Please enter the scheduled years: ")) + 1)))
#test define
def calculateSalary(startsal, percentup, numberYears):
  for year in years:
#makesure they go up on each iteration 
    upsalary = startsal*percentup
    newSalary = startsal+upsalary
    startsal = newSalary
    print("{} year salary is  {:0.2f}".format(year, newSalary))
calculateSalary(startsal, percentup, years)
