################################################################################
#	
#	launcher.py
#
#	Generates output data files from input file containing raw data
#	Usage:
#		python launcher.py [input filename] [output filename]
#
#	The target input data are from: Wizards Taverns
#	Source: https://www.wizards.com/dnd/tavern/Welcome.asp
#
################################################################################

import os, sys, subprocess

# Globals
titleStrip_output = 'titleStrip_out.txt'

def main():
	checkArgs()			# Check the number of arguments to make sure we have an input file
	
	# Strip the title from the raw data (not required)
	exec_titleStrip ()
	
# checkArgs
#	Verifies that the number of arguments is acceptable
def checkArgs ():
	# Verify the number of input arguments
	if len(sys.argv) != 3:
		print ("Usage Error:\t\tThe program needs an input filename to run.")
		print ("Correct Usage:\t\tpython genData.py [input filename] [output filename]")
		sys.exit(1)
		
# exec_titleStrip
#	Change the raw data file into a title stripped version
def exec_titleStrip ():
	cmd = "python titleStrip.py " + sys.argv[1] + " " + titleStrip_output
	subprocess.call (cmd)
	os.remove (sys.argv[1])
	os.rename (titleStrip_output, sys.argv[1])
	
main()