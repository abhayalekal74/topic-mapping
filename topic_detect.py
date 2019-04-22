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

		subject_scores = list()

		for k, v in d.items():
			subject_scores.append([k, v])

		subject_scores.sort(key=lambda x: x[1], reverse=True)
		
		best_matches = [subject_scores[0][0]]
		max_score = subject_scores[0][1]
		for subject in subject_scores[1:]:
			if subject[1] == max_score:
				best_matches.append(subject[0])
			else:
				break
		return best_matches 
	else:
		return ("Could not detect subject")


if __name__=='__main__':
	load_map(sys.argv[1])
	while True:
		inp = input("\nType sentence, q to quit..\n")
		if inp == 'q':
			sys.exit(0)
		print (detect_topic(inp))
