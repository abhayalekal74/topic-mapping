import sys
import json


word_subject_map = dict()


def add_to_map(word, subject):
	try:
		subjects = word_subject_map[word]
		if subject in subjects:
			return
	except KeyError:
		subjects = list()
		word_subject_map[word] = subjects
	subjects.append(subject)


def save_map():
	op = open(sys.argv[2], 'w')
	op.write(json.dumps(word_subject_map))
	op.close()


with open(sys.argv[1], 'r') as f:
	for line in f.readlines():
		datum = line.split(",")
		for w in datum[1].split():
			add_to_map(w, datum[0])

	save_map()
