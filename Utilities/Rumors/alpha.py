################################################################################
#
#	alpha.py
#
#	Program reads in input file and sorts everything inside.
#	Usage:
#			python alpha.py [input filename]
#
################################################################################

import os, sys

def main():
	checkArgs()
	
	list = []
	rfile = open ( sys.argv[1], 'r' )
	
	while True:
		line = rfile.readline()
		if not line: break
		
		line = line.strip('\n ')
		list.append (line.rstrip(' '))
		
	rfile.close()
	
	wfile = open ( sys.argv[1], 'w' )
	
	list.sort()
	for item in list:
		wfile.write(item + '\n')
		
	wfile.close()
	
# checkArgs
#	Verifies that the number of arguments is correct
def checkArgs():
	if len (sys.argv) < 2:
		print ("Usage Error:\t\tThe program needs an input filename to run.")
		print ("Correct Usage:\t\tpython alpha.py [input filename]")
		sys.exit(1)
		
main()