import argparse

from nltk.tag import pos_tag
from nltk.tag import StanfordNERTagger
from nltk.tag.stanford import CoreNLPNERTagger
from nltk.tokenize import word_tokenize

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, help="specify file name with absolute path")

args = parser.parse_args()
file_name=args.file

with open(file_name, "r") as fobj:
	data=fobj.read()

a_ctr=data.count("a")
an_ctr=data.count("an")
the_ctr=data.count("the")

proper_nouns=[]
tagged_sent = pos_tag(data.split())
for word in tagged_sent:
	if word[1] == "NNP":
		proper_nouns.append(word[0])

print "No. of occurances of 'a': " + str(a_ctr)
print "No. of occurances of 'an': " + str(an_ctr)
print "No. of occurances of 'the': " + str(the_ctr)
print "No. of occurances of proper nouns: " + str(len(proper_nouns))

"""
stanfordClassifier = '/Users/sabertooth07/Downloads/stanford-ner-2017-06-09/classifiers/english.muc.7class.distsim.crf.ser.gz'
stanfordNerPath = '/Users/sabertooth07/Downloads/stanford-ner-2017-06-09/stanford-ner.jar'

st = StanfordNERTagger(stanfordClassifier, stanfordNerPath, encoding='utf8')
#result = st.tag("10/24/1989")
result = st.tag(word_tokenize("October 24, 1989"))
print (result)
"""
