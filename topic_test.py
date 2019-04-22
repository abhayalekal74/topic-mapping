from topic_detect import detect_topic, load_map
from preprocess import preprocess_sentence


def detect(line):
	datum = line.rsplit(',', 2)
	detected_topics= detect_topic(preprocess_sentence(datum[0]))
	print (detected_topics, datum[1])
	if datum[1] in detected_topics:
		return 1
	else: 
		return 0


if __name__=='__main__':
	import sys
	load_map(sys.argv[1])
	with open(sys.argv[2], 'r') as f:
		lines = f.readlines()
		score = 0
		for line in lines:
			print ("\n", line)
			score += detect(line)
	print ("Accuracy", score / len(lines))
