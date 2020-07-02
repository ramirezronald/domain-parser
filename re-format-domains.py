#!/usr/bin/python3
import sys
import re
import os

#file argument check
if len(sys.argv) > 2:
	print('\n You have entered too MANY arguments! \n')
	print('\nusage: \n python3 program.py <filename>\n')
	sys.exit()

#file argument check
if len(sys.argv) < 2:
	print('\n You have entered NO arguments! \n')
	print('\nusage: \n python3 program.py <filename>\n')
	sys.exit()

# first append
firstapp = "*."
# second append
secondapp = "/*"
# new list to store values
newList = []

#open file through sys.args
with open(sys.argv[1],'r') as myfile:
		for line in myfile:
			x = line.rstrip()
			newList.append((firstapp + x + secondapp))
			newList.append((firstapp + x))
			newList.append((x + secondapp))
			newList.append((x))
		
		# write out to a file + create new if file exists
		i = 0
		while os.path.exists("re-format-output%s.txt" % i):
			i += 1
		f = open("re-format-output%s.txt" % i, "w")
		for line in newList:
			f.write(line)
			f.write('\n')
		f.close()
myfile.close()