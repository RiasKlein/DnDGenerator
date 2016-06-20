################################################################################
#
#	titleStrip.py
#
#	Generates an output file with the titles of the input stripped
#	Usage:
#		python titleStrip.py [input filename] [output filename]
#
################################################################################

import os, sys

# Globals / Settings
strip_target = ['Wizards of', 'Random Generator']		# Keys for removal between input and output
output_name = 'titleStrip_out.txt'						# default output filename is out.txt

# There will be a better home for this, mhm...
def clearConsole ():
	os.system ('cls' if os.name == 'nt' else 'clear')
	
def main():
	checkArgs()
	
	# Open up the input / output files (read / write modes respectively)
	rfile = open (sys.argv[1], 'r')
	wfile = open (output_name, 'w')

	parseAndStrip (rfile, wfile) 
	
	# Close the input / output files now that we are done
	rfile.close()
	wfile.close()

# checkArgs
#	1. Verifies that the number of arguments is acceptable
#	2. Reads in optional output filename
def checkArgs ():
	# Verify number of input arguments
	if len (sys.argv) < 2 or len (sys.argv) > 3:
		print ("Usage Error:\t\tThe program needs (at least) an input filename to run.")
		print ("Correct Usage:\t\tpython titleStrip.py [input filename]")
		print ("Alternate Usage:\t\tpython titleStrip.py [input filename] [output filename]")
		sys.exit(1)
	
	# Read in optional output filename if any
	if len (sys.argv) == 3:
		global output_name				# Use the global output_name
		output_name = sys.argv [2]		# Set the name

# parseAndStrip
#	Reads through rfile and copies lines into wfile
#	If we find a line to remove, we do not copy it into wfile		
def parseAndStrip ( rfile, wfile ):
	while True:
		line = rfile.readline()		# read in a line
		if not line: return			# leave this function if we are done
		
		# Check to see if line has a key for removal
		skip = 0
		for key in strip_target:
			if key in line:
				skip = 1
		
		# Only copy from rfile to wfile if skip == 0
		if skip == 0:
			wfile.write (line)

main()
	