import math
HourlyWage = float(input("Enter your hourly pay: $"))
NormalHours = float(input("Enter your normal hours: "))
Overtime = float(input("Enter your overtime hours: "))
#now the number value for the employees payment
weekPAY = HourlyWage * NormalHours + Overtime * HourlyWage * 1.5
print("Your total weekly pay is #" + str(weekPAY))
