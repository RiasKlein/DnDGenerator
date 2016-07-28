################################################################################
#
#	merge.py
#
#	Combines input data files into consolidated output files
#	Usage: 
#		python merge.py [input filenames] ...
#
#	Note: At the very least, 2 inputs are needed
#
################################################################################

import os, sys

# Globals
output_rumors = 'merged_rumors.txt'
output_names = 'merged_names.txt'

rumors_list = []
names_list = []

def main():
	checkArgs()		# Check the number of arguments (exit the program if needed)
	
	for arg in sys.argv:
		if 'rumor' in arg:
			updateRumors (arg)
		if 'name' in arg:
			updateNames (arg)
			
	commitOutput ()

def commitOutput ():
	# Commit Rumors
	wfile = open ( output_rumors, 'w' )
	global rumors_list
	for rumor in rumors_list:
		wfile.write (rumor)
	wfile.close()	
	
	# Commit Names
	wfile = open ( output_names, 'w' )
	global names_list
	for name in names_list:
		wfile.write (name)
	wfile.close()
	
def updateRumors ( filename ):
	rfile = open (filename, 'r')
	
	while True:
		line = rfile.readline()
		if not line: 
			rfile.close()
			return
			
		# Add the line to the global rumors_list (if it's new)
		global rumors_list
		if line not in rumors_list:
			rumors_list.append (line)
			
def updateNames ( filename ):
	rfile = open (filename, 'r')
	
	while True:
		line = rfile.readline()
		if not line: 
			rfile.close()
			return
			
		# Add the line to the global names_list (if it's new)
		global names_list
		if line not in names_list:
			names_list.append (line)
	
# checkArgs
#	Verfiest that the number of arguments is acceptable
def checkArgs():
	# Verify the number of input arguments
	if len(sys.argv) < 3:
		print ("Usage Error:\t\tThe program requires at least 2 input files to run.")
		print ("Correct Usage:\t\tpython merge.py [input 1] [input 2] ...")
		sys.exit(1)
	
main()