################################################################################
#
#	exp_pool.py
#	Experience Pool Calculator
#	
#	This tool returns the exp pool for a particular challenge.
#
#	Usage: python exp_pool.py [level=X] [party_size=Y] [enemy_count=Z]
#	The level and party_size are required to run this program.
#	By default, the number of enemies is assumed to be 1.
#	
#	Shorter versions for the arguments are:
#		level -> l
#		party_size -> p
#		enemies_size -> e
#	Example: python exp_pool.py l=4 p=6 e=2
#		This returns the exp pool for a team of 6 level 4 players who are 
#		fighting against 2 enemies.
#
#	Program by Shunman Tse
#
################################################################################

import sys

xp_tables_filename = 'xp_thresholds.txt'
xp_tables = []

# Multipliers
mult_1 = 1
mult_2 = 1.5
mult_3 = 2
mult_7 = 2.5
mult_11 = 3
mult_15 = 4

# Parameters
level = -1
party_size = -1
enemy_count = 1

def main():
	checkArgs()				# verify that we have the necessary arguments to run
	initialize()			# set up the program by loading in the xp tables
	output_exp_pool ()		# calculate and print the exp pool for the encounter
	
# output_exp_pool
#	Calculates and outputs (via std.out) the exp pool for the encounter
def output_exp_pool ():
	multiplier = calculate_multiplier (enemy_count)

	# Find the entry in xp_tables for the desired level
	# Then output to screen
	for entry in xp_tables:
		if entry[0] == level:
			print ("Party Size: " + str(party_size) + "\tLevel: " + str(level))
			print ("| {0:7} |  {1:7} |  {2:7} |  {3:7} |".format('Easy', 'Medium', 'Hard', 'Deadly'))
			
			for i in range (len (entry)):
				entry[i] = int(float(entry[i]) * float(party_size) / float(multiplier))
				
			print ("| {0:7} |  {1:7} |  {2:7} |  {3:7} |".format(str(entry[1]), str(entry[2]), str(entry[3]), str(entry[4])))
			
# calculate_multiplier
# 	Returns the proper multiplier to use for the current setup
def calculate_multiplier ( enemy_count ):
	if enemy_count == 1:
		return mult_1
	elif enemy_count == 2:
		return mult_2
	elif enemy_count >= 3 and enemy_count <= 6:
		return mult_3
	elif enemy_count >= 7 and enemy_count <= 10:
		return mult_7
	elif enemy_count >= 11 and enemy_count <= 14:
		return mult_11
	elif enemy_count >= 15:
		return mult_15

# checkArgs
#	Checks whether we have enough arguments to run the program
def checkArgs():
	# Check if we have the minimum number of terms
	# At the very least, we need the party size and the level
	if len (sys.argv) < 3:
		error_missing_arguments ()		

def error_missing_arguments ():
	print ("Error: Insufficient number of parameters. Include the party size and level.")
	print ("Usage Example: python exp_pool.py level=4 party_size=1")
	sys.exit()

# initialize
#	Loads the necessary data
def initialize():
	# Read the file for the xp table
	read_xp_tables ( xp_tables_filename )

	# Read the input parameters
	for argv in sys.argv:
		if '=' in argv:
			argv = argv.split('=')
			if argv[0] == 'p' or argv[0] == 'party_size':
				global party_size
				party_size = int(argv[1])
			elif argv[0] == 'l' or argv[0] == 'level':
				global level
				level = int (argv[1])
			elif argv[0] == 'e' or argv[0] == 'enemy_count':
				global enemy_count
				enemy_count = int (argv[1])

	# Check that we have all the required variables
	if level == -1 or party_size == -1:
		error_missing_arguments ()

# read_xp_tables
#	Reads in the content of filename and store in xp_tables
def read_xp_tables( filename ):
	rfile = open (filename)

	while True:
		line = rfile.readline()
		if not line:
			rfile.close()
			return

		if '#' not in line:
			line = line.rstrip ('\n')
			line = line.split (' ')
			for x in range(len (line)): 
				line[x] = int(line[x])
			xp_tables.append(line)

main()