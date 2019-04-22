import sys
import re


with open(sys.argv[1], 'r') as f:
	lines = f.read()

order = sys.argv[3]


if order == 'tsc':
	# time, subject, content
	pattern = r'(\d{13}),([^,]+),"([^"]*)"'


op = open(sys.argv[2], 'w')
	
for match in re.finditer(pattern, lines, re.MULTILINE):
	op.write(",".join([match.group(3).replace('\n', ' '), match.group(2), match.group(1)]) + "\n")

op.close()
