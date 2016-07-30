################################################################################
#
#	DnDGenerator.py
#
#	This takes in inputs from the user and launches the proper utilities.
#
#	Version: 0.22
#	
#	Program by Shunman Tse
#
################################################################################

import sys, os, subprocess

# Configurable Globals

# Settings for the initial print of the program
system_title = 'DnDGenerator'	# Title of the program
system_version = '0.22'			# Version
system_title_buffer = 20		# The amount of buffer space when printing the title of the program

# Settings for the function of the program
supported_functions = ['exp_pool', 'roll', 'genrumor', 'rumor']
built_in_functions = ['help', 'exit']

def main():
	# Print basic program info and change program title
	initialize ()

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
		if user_input[0] == 'genrumor' or user_input[0] == 'rumor':
			handle_rumor(user_input)
		if user_input[0] == 'exp_pool':
			handle_exp_pool (user_input)
	# If we have a supported built-in function, handle it
	elif user_input[0] in built_in_functions:
		handle_built_in (user_input)
	# Do nothing for a NULL input
	elif user_input[0] == '':
		return
	else:
		print ("Function: '" + user_input[0] + "' is not supported.")

# handle_exp_pool
#	Procedure for handling the exp_pool command
def handle_exp_pool (user_input):
	if len (user_input) < 3:
		print ("The " + user_input[0] + "function does not support this number of inputs.")
		print ("Proper usage example: exp_pool level=4 party_size=2")
	else:
		os.chdir ('./Utilities/Exp-Pool')
		if len(user_input) == 3: 
			subprocess.call (['python', 'exp_pool.py', user_input[1], user_input[2]])
		else:
			subprocess.call (['python', 'exp_pool.py', user_input[1], user_input[2], user_input[3]])
		for x in range (2):	os.chdir ('..')
		
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
	elif user_input[0] == 'help':
		print_valid_functions()
		
# print_valid_functions
def print_valid_functions():
	print ("The following functions are supported in this version.")
	print ("   {0:17} |    {1:10}".format('Function', 'Usage'))
	print ("{0:20} | Calculates the exp-pool for a party setup".format('exp_pool'))
	print ("{0:8} or {1:8} | Generates random rumors".format('genRumor', 'rumor'))
	print ("{0:20} | Generates a specified roll of dice.".format('roll'))

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

# initialize
#	Outputs the basic program information at the start and changes title of program
def initialize():
	# Set the title for the program
	os.system ("title " + system_title)
	
	# Output the basic information about the program
	print ("=" * (2 * system_title_buffer + len(system_title)) + "\n" + " " * system_title_buffer + system_title + "\n" + "=" * (2 * system_title_buffer + len(system_title)))
	print ("Version: " + system_version + '\n')

main()