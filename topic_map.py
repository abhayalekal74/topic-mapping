import sys
import json
from collections import defaultdict


word_subject_map = dict()


def add_to_map(word, subject):
	global word_subject_map
	try:
		subjects = word_subject_map[word]
	except KeyError:
		subjects = defaultdict(int)
		word_subject_map[word] = subjects
	subjects[subject] += 1


def save_map(sync):
	op = open(sync, 'w')
	op.write(json.dumps(word_subject_map))
	op.close()


def build_map(data_file):
	with open(data_file, 'r') as f:
		for line in f.readlines():
			datum = line.split(",")
			for w in datum[1].split():
				add_to_map(w, datum[0])


if __name__ == '__main__':
	build_map(sys.argv[1])
	save_map(sys.argv[2])
