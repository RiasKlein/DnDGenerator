################################################################################
#	
#	extract.py
#
#	Generates output data files from input file containing raw data
#	Usage:
#		python extract.py [input filename] [optional salt]
#
#	The target input data are from: Wizards Taverns
#	Source: https://www.wizards.com/dnd/tavern/Welcome.asp
#
################################################################################

import os, sys, subprocess

# Globals
titleStrip_output = 'out_titleStrip.txt'
rumors_output = 'out_rumors.txt'			# Output file with rumors
names_output = 'out_names.txt'				# Output file with names

def main():
	checkArgs()			# Check the number of arguments to make sure we have an input file
	
	# Update output file names with optional salt (if it exists)
	if len (sys.argv) == 3:
		global rumors_output
		rumors_output = rumors_output[:-4] + '_' + str ( sys.argv [2] ) + '.txt'
		
		global names_output
		names_output = names_output[:-4] + '_' + str ( sys.argv [2] ) + '.txt'
	
	# Strip the title from the raw data (not required)
	exec_titleStrip ()
	
	# Extract names 
	extractNames ( sys.argv[1] )
	
	# Extract rumors 
	extractRumors( sys.argv[1] )
	
# extractNames
#	Pulls names from the wizards raw data file	
def extractNames ( input ):
	rfile = open ( input, 'r' )
	wfile = open ( names_output, 'w' )
	
	while True:
		line = rfile.readline()		# read a line from input file
		if not line: 				# when at end of the file, clean up
			rfile.close()			
			wfile.close()
			return
		
		# If we find a name, clean it up and write to rumor output file
		if 'Tavern Name' in line:
			line = line[len('Tavern Name: '):]			# Remove the unncessary header
			wfile.write (line)
	
# extractRumors
#	Pulls rumors from the wizards raw data file
def extractRumors( input ):
	rfile = open ( input, 'r' )
	wfile = open ( rumors_output, 'w' )
	
	while True:
		line = rfile.readline()		# read a line from input file
		if not line: 				# when at end of the file, clean up
			rfile.close()			
			wfile.close()
			return
		
		# If we find a rumor, clean it up and write to rumor output file
		if 'Rumors Overheard' in line:
			line = line[len('Rumors Overheard: '):]			# Remove the unncessary header
			line = line.split ('.')
			
			for x in line:
				if x != '\n':
					x = x.strip (' ')
					wfile.write ( x + '.\n')
	
# checkArgs
#	Verifies that the number of arguments is acceptable
def checkArgs ():
	# Verify the number of input arguments
	if len(sys.argv) < 2:
		print ("Usage Error:\t\tThe program needs an input filename to run.")
		print ("Correct Usage:\t\tpython extract.py [input filename] [salt]")
		sys.exit(1)
		
# exec_titleStrip
#	Change the raw data file into a title stripped version
def exec_titleStrip ():
	cmd = "python titleStrip.py " + sys.argv[1] + " " + titleStrip_output
	subprocess.call (cmd)
	os.remove (sys.argv[1])
	os.rename (titleStrip_output, sys.argv[1])
	
main()