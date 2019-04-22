from preprocess import preprocess_sentence
import json
import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
	word_subject_map = json.loads(f.read())


while True:
	inp = input("\nType sentence, q to quit..\n")
	if inp == 'q':
		sys.exit(0)
	sentence = preprocess_sentence(inp)
	subjects = list()
	words = sentence.split()
	for w in words:
		try:
			subjects += word_subject_map[w]
		except KeyError:
			pass
	if subjects:
		d = defaultdict(int)
		for subject in subjects:
			d[subject] += 1

		print (d)

		max_sub = max(d.items(), key=lambda x: x[1])
		print (max_sub[0], max_sub[1] / len(words))
	else:
		print ("Could not detect subject")
