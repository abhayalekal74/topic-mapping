from topic_detect import detect_topic, load_map


def detect(line):
	datum = line.rsplit(',', 2)
	detected_topics= detect_topic(datum[1])
	if datum[0] == 'Maths':
		datum[0] = 'Mathematics'
	if detected_topics == 'Could not detect subject' or datum[0] in detected_topics:
		return 1
	else: 
		print ("\n", datum[1].strip())
		print (detected_topics, datum[0])
		return 0


if __name__=='__main__':
	import sys
	load_map(sys.argv[1])
	with open(sys.argv[2], 'r') as f:
		lines = f.readlines()
		score = 0
		for line in lines:
			score += detect(line)
	print ("Accuracy", score / len(lines))
