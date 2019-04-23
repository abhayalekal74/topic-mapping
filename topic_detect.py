from preprocess import preprocess_sentence
import json
import sys
from collections import defaultdict


word_subject_map = dict()
remove_bottom = 0.25 
ignore_words = ["please", "mark", "best", "answer", "give", "thank", "correct", "right", "understand", "question"]


def load_map(map_file):
	global word_subject_map
	with open(map_file, 'r') as f:
		word_subject_map = json.loads(f.read())


def detect_topic(inp):
	sentence = preprocess_sentence(inp)
	subject_freq = defaultdict(int)
	words = set(sentence.split())
	subjects_found = False
	for w in words:
		ignore = sum([1 if w.startswith(i) else 0 for i in ignore_words])
		if not ignore:
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
		print (subject_scores)
		up_to_index = 1
		threshold_score = remove_bottom * subject_scores[0][1]
		for i in range(1, len(subject_scores)):
			if subject_scores[i][1] >= threshold_score:
				up_to_index += 1
		return subject_scores[:up_to_index] 
	else:
		return ("Could not detect subject")


if __name__=='__main__':
	load_map(sys.argv[1])
	while True:
		inp = input("\nType sentence, q to quit..\n")
		if inp == 'q':
			sys.exit(0)
		print (detect_topic(inp))
