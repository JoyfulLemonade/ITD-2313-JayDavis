import random
import math
smoler = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxguess = math.log2(larger-smoler+1)
count = 0
while count < maxguess:
    count += 1
    print(smoler,larger)
    guess = int((smoler + larger) / 2)#computer takes a guess
    print('number is',guess)
    hint = input('Enter >,<,or =:')
    if hint == '<': 
        larger = guess
    elif hint == '>':
        smoler = guess
    elif hint == '=':
        print('Poggers I outplayed you in %d attempts!'%(count))
        break
else:
    print('I\'m out of guesses... antipog')
