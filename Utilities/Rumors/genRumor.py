################################################################################
#
#	genRumor.py
#
#	Generates a rumor of the form Actor + Action using components from 
#	files containing lists of actors and actions.
#	Usage:
#			python genRumor.py [actors filename] [actions filename]
#
#	If no filenames are provided, the default ones will be used.
#
################################################################################

import sys, random

# Default Globals
actors_filename = 'rumor_actors.txt'
actions_filename = 'rumor_actions.txt'

actors_list = []
actions_list = []

def main():
	updateFilenames()		# Use the provided filenames, if they were provided
	
	# Read in the actors and actions files
	readFiletoList ( actors_filename, actors_list )
	readFiletoList ( actions_filename, actions_list )
	
	# Retrieve an actor and an action
	actor = getRandElement ( actors_list ) + ' ' 
	action = getRandElement ( actions_list )
	
	# Output the merged result
	print ( actor + action )

# getRandElement
#	Returns a random element from a provided list	
def getRandElement ( list ):
	index = random.randint (0, len(list) - 1)
	return list[index]
	
# readFiletoList
#	Opens file and imports contents into a list (line by line)	
def readFiletoList ( filename, list ):
	rfile = open (filename, 'r')
	
	while True:
		line = rfile.readline()
		if not line: break
		
		line = line.strip('\n ')
		list.append (line)
	
	rfile.close()
	
# updateFilenames
#	Updates the global filename variables with provided arguments (if there are any)
def updateFilenames():
	# If both filenames were provided, update our globals
	if len (sys.argv) > 2:
		global actions_filename
		global actors_filename
		actors_filename = sys.argv[1]
		actions_filename = sys.argv[2]
		
	# If only one filename was provided, give a warning.
	if len (sys.argv) == 2:
		print ("genRumor.py requires 2 file names, one for actors and one for actions (in that order).")
		print ("Default filenames were used instead.")

main()