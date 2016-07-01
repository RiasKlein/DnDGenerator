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
grammar_filename = 'rumor_grammar.txt'

actors_list = []
actions_list = []

# Dictionaries
singular_dict = {}	# singular_dict has keys that are plural and values that are singular
plural_dict = {} 	# plural_dict has keys that are singular and values that are plural

# Singular keys
singular_keys = ['a', 'an']

def main():
	# Initialize the data needed for generating rumors
	initialize()
	
	# Output a rumor 
	print (generateRumor())

# generateRumor
#	Generates a rumor by merging a random actor with an action
def generateRumor():
	actor = getRandElement ( actors_list ) 
	action = getRandElement ( actions_list )
		
	action = fixGrammar( actor, action )

	# Output the merged result
	return ( actor + ' ' + action + '\n')

# initialize
#	Loads proper files / data for program to function
def initialize ():
	updateFilenames()		# Use the provided filenames, if they were provided
	
	# Read in the actors and actions files
	readFiletoList ( actors_filename, actors_list )
	readFiletoList ( actions_filename, actions_list )

	# Read in the grammar dictionaries
	readDictionaries ( grammar_filename, singular_dict, plural_dict )

# readDictionaries
#	Generates dictionaries for singular-plural pairs using content of file
def readDictionaries ( filename, singular, plural ):
	# Open for the dict. file for reading
	rfile = open ( filename, 'r' )

	# Generate our dictionaries
	while True:
		line = rfile.readline()
		if not line: 
			rfile.close()
			return

		line = line.strip(' \n')
		line = line.split(' ')

		# '#' is used to mark a line as a comment - don't process those
		if (line[:1]) != '#' and line != '':
			# The two elements of line are in the format: singular, plural
			# singular_dict has keys that are plural and values that are singular
			singular_dict[line[1]] = line[0]

			# plural_dict has keys that are singular and values that are plural
			plural_dict[line[0]] = line[1]

# fixGrammar
#	Fix the grammar so the actor and action is a better sentence
def fixGrammar ( actor, action ):
	# Check whether the actor is plural
	actor_is_plural = False			# Assume that the actor is singular
	actor_e = actor.split (' ')		# Get individual words of actor
	for element in actor_e:
		if element[len(element)-1:].lower() == 's':
			actor_is_plural = True
			break

	if actor_e[0].lower() in singular_keys:
		actor_is_plural = False

	# Now make the action match a singular actor
	if not actor_is_plural:
		#print ('not plural')	# DEBUG
		action = makeSingular ( action )

	# Make the action match a plural actor
	if actor_is_plural:
		#print ('plural')	# DEBUG 
		action = makePlural ( action )

	return action

def makeSingular ( action ):
	# First we split the action string into individual words
	action_e = action.split (' ')

	if singular_dict.has_key (action_e[0]):
		action_e[0] = singular_dict.get(action_e[0])
	action_e = listToString (action_e)

	return action_e

def makePlural ( action ):
	# First we split the action string into individual words
	action_e = action.split (' ')

	if plural_dict.has_key (action_e[0]):
		action_e[0] = plural_dict.get (action_e[0])
	action_e = listToString (action_e)

	return action_e

# listToString
#	Returns a string composed by the concatenation of the elements of an input list
def listToString ( list ):
	result = ''
	for element in list:
		result += str(element)
		result += ' '
	return result

# getRandElement
#	Returns a random element from a provided list	
def getRandElement ( list ):
	index = random.randint (0, len(list) - 1)
	return list[index]
	
# readFiletoList
#	Opens file and imports contents into a list (line by line)	
#	Statements starting with '#' are considered comments
def readFiletoList ( filename, list ):
	rfile = open (filename, 'r')
	
	while True:
		line = rfile.readline()
		if not line: break
		
		line = line.strip('\n ')

		# '#' is used to mark a line as a comment - don't process those
		if (line[:1]) != '#' and line != '':
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