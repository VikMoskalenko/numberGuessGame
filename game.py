import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
print("\n\tYou've only ", 
	round(math.log2(upper - lower + 1)),
	" chances to guess the integer!\n")
count = 0

for count in range(round(math.log2(upper - lower + 1))):

	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

else:
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
    
    #test