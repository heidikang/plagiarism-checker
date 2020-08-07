import sys
import os

# file to be checked
fname = sys.argv[1]

# directory of corpus to be checked against - unformatted text
corpus_dir = sys.argv[2]

# read sample file into string
sample_fobj = open(fname,'r')
sample_string = sample_fobj.read()
sample_fobj = sample_fobj.close()
# list of documents in corpus stored as strings
l_corpus = []

# load corpus into list
for cfname in os.listdir(corpus_dir):
    corp_fobj = open(corpus_dir + "/" + cfname,'r')
    corp_string = corp_fobj.read()
    l_corpus.append(corp_string)
    corp_fobj = corp_fobj.close()

# print sample
print("Sample:\n")
print(sample_string + "\n")

# print corpus file by file
for i,doc in enumerate(l_corpus):
    print("doc" + str(i) + ":\n")
    print(doc + "\n")
