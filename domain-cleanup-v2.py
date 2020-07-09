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

#temporary list to story values
temp_List = []
#domains only
domain_only = []
#used to clean up final check 
finalCheck = []

#regex to match the end of the following char: "/"
regex = r"[\/]$"

#use ase replacer = null
subst = ""

#open file through sys.args
with open(sys.argv[1],'r') as myfile:
		for line in myfile:
			temp_List.append(line.strip('*.'))

		#remove * char
		for line in temp_List:
			domain_only.append(line.replace('*', ''))

		#remove dups
		domain_only = list(dict.fromkeys(domain_only))

		#last check to remove "/" char from the end of the lines
		for x in domain_only:
			#result = re.sub(regex, subst, x, 0, re.MULTILINE)
			finalCheck.append(re.sub(regex, subst, x, 0, re.MULTILINE))

		#remove any last dups
		finalCheck = list(dict.fromkeys(finalCheck))

		# write out to a file + create new if file exists
		i = 0
		while os.path.exists("domain-output-v2-%s.txt" % i):
			i += 1
		f = open("domain-output-v2-%s.txt" % i, "w")
		for line in finalCheck:
			f.write(line)
		f.close()
myfile.close()

