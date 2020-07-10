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
pattern = re.compile(r'^[| *.a-z0-9-]+\.[a-z0-9-./]+')

#temporary list to story values
temp_List = []
#domains only list
domain_only = []
#will not include unresolved lines from output created by HostResolver
badwords = ['unresolvable']

#open file through sys.args
with open(sys.argv[1],'r') as myfile:
		for line in myfile:
			#first check and DO NOT include unresolved responses
			if not any(badword in line for badword in badwords):
				#then begin to match by patter regex
				matches = pattern.finditer(line)
				#only get the group domain (in other words, only the first enrtry [1])
				for match in matches:
					temp_List.append(match.group(0))

		for x in temp_List:
			#strip the extra charachters
			domain_only.append(x.strip('| '))
		#remove dups
		domain_only = list(dict.fromkeys(domain_only))
		
		# write out to a file + create new if file exists
		i = 0
		while os.path.exists("resolved-output-v2-%s.txt" % i):
			i += 1
		f = open("resolved-output-v2-%s.txt" % i, "w")
		for line in domain_only:
			f.write(line)
			f.write('\n')
		f.close()
myfile.close()