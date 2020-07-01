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

#this is the pattern to match
pattern = re.compile(r'^[| *.a-z0-9-]+\.[a-z0-9-.]+')

#temporary list to story values
temp_List = []
#domains only list
domain_only = []
#remove dups
remove_dups = []

#open file through sys.args
with open(sys.argv[1],'r') as myfile:
		for line in myfile:
			matches = pattern.finditer(line)
			for match in matches:
				#only match the object no extra fluff 
				temp_List.append(match.group(0))
		for x in temp_List:
			#strip the extra charachters
			domain_only.append(x.strip('| '))

		domain_only = list(dict.fromkeys(domain_only))
		
		# write out to a file + create new if file exists
		i = 0
		while os.path.exists("dos-output%s.txt" % i):
			i += 1
		f = open("dos-output%s.txt" % i, "w")
		for line in domain_only:
			f.write(line)
			f.write('\n')
		f.close()
myfile.close()
