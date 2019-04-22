import sys
import re
import nltk
from nltk.corpus import stopwords


stopwords = stopwords.words('english')
allowed_subjects = ["Sociology", "Hindi Language", "History", "Geography", "Economics", "English", "Science", "Maths", "Mathematics", "Chemistry", "Physics", "Biology", "Important Question", "Social Science"]


def has_only_alphabets(w):
	return re.search(r'\b[a-z]{4,}\b', w)


def preprocess_sentence(s):
	content = re.sub(r'<.*?>', ' ', s).replace('\n', ' ').lower()
	content = re.sub(r'[^a-z]', ' ', content)
	content = re.sub(r'\s+', ' ', content)
	words = [w for w in content.split() if w not in stopwords]
	alpha_words = [w for w in words if has_only_alphabets(w)]	
	return " ".join(alpha_words)
	


def process_record(record):
	if record[1] == 'Maths':
		record[1] = 'Mathematics'
	return ",".join([record[1], preprocess_sentence(record[0])])


if __name__ == '__main__':
	op = open(sys.argv[2], 'w')

	with open(sys.argv[1], 'r') as f:
		for line in f.readlines():
			datum = line.rsplit(',', 2)
			if len(datum) == 3 and datum[-2] in allowed_subjects:
				op.write(process_record(datum) + "\n")

	op.close()
