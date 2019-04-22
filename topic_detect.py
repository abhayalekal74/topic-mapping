from preprocess import preprocess_sentence
import json
import sys
from collections import defaultdict


word_subject_map = dict()


def build_map(map_file):
	global word_subject_map
	with open(map_file, 'r') as f:
		word_subject_map = json.loads(f.read())


def detect_topic(inp):
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
		return (max_sub[0], max_sub[1] / len(words))
	else:
		return ("Could not detect subject")


if __name__=='__main__':
	build_map(sys.argv[1])
	while True:
		inp = input("\nType sentence, q to quit..\n")
		if inp == 'q':
			sys.exit(0)
		print (detect_topic(inp))
