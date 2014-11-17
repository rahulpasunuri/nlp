"""
Now different from the previous project, we need to make the code general so that one can specify their partition for POS and NEG lists.
INPUT: two files specifying the recipe names, one for POS; one for NEG;
INPUT: the fold name; or how to name these features uniquely.
INPUT: path to the reviews data - represented in pickles.
***** ONE HAS TO NAME ALL REVIEW FILES xxx.pickle *****
"""

import random
import cPickle as pickle
from collections import defaultdict
#from nltk import ngrams as ngtool
import nltkngram
from nltkngram import *
import argparse
CORPATH = "../corpus/"  ##We need to write a shell that creat this folder.

class CorpusMaker:

    def __init__(self,neg_list,pos_list,review_path,ngram_n, fold_name,extension ): ##Ngram-n is the ngram number: up to which.
        self.neg_list = neg_list
        self.pos_list = pos_list
        self.review_path = review_path
        self.unigram_do = True
        self.bigram_do = False
        self.trigram_do = False
        self.fold_name = fold_name
        self.extension = "." + extension
        assert int(ngram_n) <=3 and int(ngram_n) >=1, "Invalid option for ngram_n. <1> up to unigram; <2> up to bigram; <3> up to trigram"
        if int(ngram_n)==2:
            self.bigram_do = True
        elif int(ngram_n) ==3:
            self.trigram_do = True
            self.bigram_do = True
        print "Corpus Maker has been initiated with FOLD NAME : ", fold_name

    def make_corpus(self):
        neg = pickle.load(open(self.neg_list,"rb"))[:]
        pos = pickle.load(open(self.pos_list,"rb"))[:]

        assert len(neg)!=0, "The list of NEG recipes you provided is empty."
        assert len(pos)!=0, "The list of POS recipes you provided is empty."

        pos_corpus = defaultdict(lambda:0)
        neg_corpus = defaultdict(lambda:0)

        for poscase in pos[:]:
            if len(poscase.strip()) ==0: continue
            wrd_comments = pickle.load(open( self.review_path + poscase + self.extension,"rb"))

            for cmt in wrd_comments:
                for sent in cmt:
                    if self.bigram_do: bigrams = ngtool(sent,2)
                    else: bigrams = []
                    if self.trigram_do: trigrams = ngtool(sent,3)
                    else: trigrams = []
                    bigrams = ["{}##{}".format(x,y) for x,y in bigrams]
                    trigrams = ["{}##{}##{}".format(x,y,z) for x,y,z in trigrams]

                    ngrams  = sent + bigrams + trigrams
                    for ele in ngrams:
                        pos_corpus[ele.lower()] +=1

        for negcase in neg[:]:
            if len(negcase.strip() )==0: continue
            wrd_comments = pickle.load(open( self.review_path + negcase + self.extension,"rb"))

            for cmt in wrd_comments:
                for sent in cmt:
                    if self.bigram_do: bigrams = ngtool(sent,2)
                    else: bigrams = []
                    if self.trigram_do : trigrams = ngtool(sent,3)
                    else: trigrams = []
                    bigrams = ["{}##{}".format(x,y) for x,y in bigrams]
                    trigrams = ["{}##{}##{}".format(x,y,z) for x,y,z in trigrams]

                    ngrams  = sent + bigrams + trigrams
                    for ele in ngrams:
                        neg_corpus[ele.lower()] +=1 

        pos_corpus = {key:value for key,value in pos_corpus.items() if value >= 4}
        neg_corpus = {key:value for key,value in neg_corpus.items() if value >= 4}

        print "Done building POS corpus for fold {0}, the length of the corpus is {1}".format(self.fold_name, len(pos_corpus))
        print "Done building NEG corpus for fold {0}, the length of the corpus is {1}".format(self.fold_name, len(neg_corpus))

        pickle.dump(neg_corpus,open(CORPATH + self.fold_name + "_neg_corpus.pickle","wb"))
        pickle.dump(pos_corpus,open(CORPATH + self.fold_name + "_pos_corpus.pickle","wb"))

