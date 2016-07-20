################################################################################
#
#	roll.py
#
#	Rolls d20 dice in the format: xdy 
#		where x is the number of y-sided dice to roll
#	The total value is outputted to standard output
#
#	Usage:
#		python roll.py xdy
#
#	Shunman Tse
#
################################################################################

import sys, random

def main():
	checkArgs()

	# Extract the user input
	user_input = sys.argv[1].lower()
	user_input = user_input.split('d')
	verifyInput (user_input)

	# Prepare to simulate the rolls
	num_to_roll = int(user_input[0])
	num_sides = int(user_input[1])

	# Simulate the rolls and get a total value
	total_roll = 0
	random.seed()
	for roll in range(num_to_roll):
		total_roll += random.randint (1, num_sides)

	# Output the total of the rolls
	print (total_roll)

def verifyInput ( user_input ):
	if len (user_input) != 2:
		print ("Error in input argument. Correct input has the form: xdy")
		print ("\twhere x is the number of y-sided dice to roll")
		sys.exit()

def checkArgs():
	if len (sys.argv) < 2:
		print ("Usage Error:\t\tThe program needs an input to run.")
		print ("Correct Usage:\t\tpython roll.py [xdy]")
		sys.exit()

main()