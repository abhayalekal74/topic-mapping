from preprocess import preprocess_sentence
import json
import sys
from collections import defaultdict


word_subject_map = dict()


def load_map(map_file):
	global word_subject_map
	with open(map_file, 'r') as f:
		word_subject_map = json.loads(f.read())


def detect_topic(inp):
	sentence = preprocess_sentence(inp)
	subject_freq = defaultdict(int)
	words = sentence.split()
	subjects_found = False
	for w in words:
		try:
			print (w, word_subject_map[w])
			for k, v in word_subject_map[w].items():
				subject_freq[k] += v
			if not subjects_found:
				subjects_found = True
		except KeyError:
			pass
	if subjects_found:
		subject_scores = list()

		for k, v in subject_freq.items():
			subject_scores.append([k, v])

		subject_scores.sort(key=lambda x: x[1], reverse=True)
		return subject_scores[:5] 
	else:
		return ("Could not detect subject")


if __name__=='__main__':
	load_map(sys.argv[1])
	while True:
		inp = input("\nType sentence, q to quit..\n")
		if inp == 'q':
			sys.exit(0)
		print (detect_topic(inp))
