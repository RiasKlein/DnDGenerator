################################################################################
#
#	DnDGenerator.py
#
#	This takes in inputs from the user and launches the proper utilities.
#
#	Version: 0.1
#	
#	Program by Shunman Tse
#
################################################################################

import sys, os, subprocess

# Configurable Globals
system_version = '0.1'
supported_functions = ['roll', 'genRumor', 'rumor']
built_in_functions = ['exit']

def main():
	# Print basic information about the Program
	print_basic_info ()

	# Get user input and handle it
	while True:
		# Ask the user for what they are searching for
		sys.stdout.write('>')
		user_input = raw_input()

		handle_input (user_input)

def handle_input (user_input):
	# First, convert the user input into a form we can process
	user_input = user_input.lower().strip('\n')
	user_input = user_input.split (' ')

	# If we have a supported function, handle it
	if user_input[0] in supported_functions:
		if user_input[0] == 'roll':
			handle_roll(user_input)
		if user_input[0] == 'genRumor' or user_input[0] == 'rumor':
			handle_rumor(user_input)
	# If we have a supported built-in function, handle it
	elif user_input[0] in built_in_functions:
		handle_built_in (user_input)
	else:
		print ("Function: '" + user_input[0] + "' is not supported.")

# handle_rumor
#	Procedure for handling the rumor / genRumor command
def handle_rumor (user_input):
	# user_input is a list of the user's input

	# First we check if we have the supported number of inputs
	# If we do, then we go to the proper directory and run the program genRumor.py
	if len (user_input) != 2:
		print ("The " + user_input[0] + " function does not support this number of inputs.")
		print ("Proper usage examples: rumor 5 or genRumor 3")
	else:
		os.chdir ('./Utilities/Rumors')
		subprocess.call(['python', 'genRumor.py', user_input[1]])
		for x in range (2):	os.chdir ('..')

# handle_built_in
#	Procedures for handling various built-in commands 
def handle_built_in (user_input):
	if user_input[0] == 'exit':
		sys.exit()

# handle_roll
#	Procedure for handling the roll command if the user enters it
def handle_roll (user_input):
	# user_input is a list of the user's input

	# First we check if we have the supported number of inputs
	# If we do, then we go to the proper directory and run the program roll.py
	if len (user_input) != 2:
		print ("The 'roll' function does not support this number of inputs.")
		print ("Proper usage example: roll 2d10")
	else:
		os.chdir ('./Utilities/Roll')
		subprocess.call(['python', 'roll.py', user_input[1]])
		for x in range (2):	os.chdir ('..')

# print_basic_info
#	Outputs the basic program information at the start of DnDGenerator
def print_basic_info():
	print ("========================================\n\tDnDGenerator\n========================================")
	print ("Version: " + system_version + '\n')

main()