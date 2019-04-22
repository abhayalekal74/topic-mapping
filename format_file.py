import sys
import re


def format_file(inp, out, order):
	with open(inp, 'r') as f:
		lines = f.read()

	if order == 'tsc':
		# time, subject, content
		pattern = r'(\d{13}),([^,]+),"([^"]*)"'

	op = open(out, 'w')
		
	for match in re.finditer(pattern, lines, re.MULTILINE):
		op.write(",".join([match.group(3).replace('\n', ' '), match.group(2), match.group(1)]) + "\n")

	op.close()


if __name__=='__main__':
	format_file(sys.argv[1], sys.argv[2], sys.argv[3])
