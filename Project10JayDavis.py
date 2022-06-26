price = float(input("Total computer cost:"))
remainingPrice = (price * 0.9)
monthlyPayment = remainingPrice * 0.05
interestOwed = remainingPrice * (.12/12.0)
principal = monthlyPayment - interestOwed
month = 0
print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, price, interestOwed, principal, monthlyPayment, remainingPrice))
while remainingPrice > 0:
    month += 1
    remainingPrice -= principal
    interestOwed = remainingPrice * (.12/12.0)
    principal = monthlyPayment - interestOwed

print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, price, interestOwed, principal, monthlyPayment, remainingPrice))
#attempt4
