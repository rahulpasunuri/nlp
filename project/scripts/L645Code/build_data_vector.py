##Feature Selection.
##First we have to find all the videos that are normalized,
##out of them , use some as training data and extract training data from there...
import argparse
import cPickle as pickle
from collections import defaultdict
import math
import os
import svmlight
from svmlight import *
import IGer_n
#from nltk import ngrams as ngtool
import nltkngram
from nltkngram import *

CORPATH = "../corpus/"
TTPATH = "../svmdata/"
##that was a confusing number, we might or might not need it.

def extract_multiclass(featurefile,train_list,review_path,ngram_n,out_name,extension):
    extension = "." + extension.strip(".")
    print "\t***Began extracting.... Please wait.... "
    if int(ngram_n)==2:
        bigram_do = True
        trigram_do = False
    elif int(ngram_n) ==3:
        trigram_do = True
        bigram_do = True
    else:
        bigram_do = False
        trigram_do = False
    features = pickle.load(open(featurefile,"rb")) ##User has to specify the feature file
    features = [x[1] for x in features]
    numFeature = len(features)	
    train = pickle.load(open(train_list,"rb"))

    header = [str(x) for x in range(1,numFeature +1)]
    headerline = ",".join(header) + ",LABEL" + "\n"
	
    train_vectors = [] 
    count =0  ##just to keep track where we are in the process of making train/test data.
    for video in train:
        if len(video.strip())==0: continue
        label = video.split("_")[0]  ##the naming is something like 3_arhgafgadfa;
        try:
        # If there is an error in loading the pickle
        #    we were actually using pos_comments; wrd_comments 
        #    from the previous video
            wrd_comments = pickle.load(open(review_path + video + extension,"rb"))
        except: 
            print "Something is wrong when loading this video: ", video, "press <enter> to skip it."
            raw_input()

        vector = []
        ngrams = []

        for cmt in wrd_comments:
            for sent in cmt:
                ngrams += [x.lower() for x in sent]
                if bigram_do : bigrams = ngtool(sent,2)
                else: bigrams = []
                if trigram_do:trigrams = ngtool(sent,3)
                else: trigrams = []
                bigrams = ["{}##{}".format(x.lower(),y.lower()) for x,y in bigrams]
                trigrams = ["{}##{}##{}".format(x.lower(),y.lower(),z.lower()) for x,y,z in trigrams]

                ngrams += bigrams
                ngrams += trigrams

        for f in features:
            vector.append(str(ngrams.count(f)))
        vector.append(label)
        train_vectors.append(",".join(vector) + "\n")
        count +=1
        print "\tIntance: ",count
    print "done training !"
    #print features, "--------", len(features) 
    train_vectors.insert(0,headerline)
    #print train_vectors    
    OUT1 = open(TTPATH + out_name,"w")
    OUT1.writelines(train_vectors)
    OUT1.close()
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program generates the selected features based on speficied POS/NEG partition and a n-gram length.')
    parser.add_argument('-s','--s', help='The selected features file', required=True)
    parser.add_argument('-p','--p', help='Path that contains the review data represented in pickles', required=True)
    parser.add_argument('-n','--n', help='n-gram length; <1/2/3> for up to uni/bi/tri -gram', required=True)
    #parser.add_argument('-f','--f', help='Fold name, use to uniquely distinguish the feature file.', required=True)
    parser.add_argument('-e','--e', help='Extension of the pickle files that contain the reviews [DEFAULT IS .pickle] if not specified', required=False)
    parser.add_argument('-rl','--rl', help='The recipe name list, use different ones for training and testing', required=True)
    parser.add_argument('-o','--o', help='Please name your output data vector file', required=True)
    args = vars(parser.parse_args())
    
    extract_multiclass(featurefile = args['s'],train_list = args['rl'],review_path = args['p'], ngram_n = args['n'], out_name = args['o'], extension = args['e'])

    trainName = TTPATH + args['o']

    print "\n****Now we are normalizing feature values by column and convert them into a SVM compatible format****\n"
    convert(trainName)
    
    print "\n****You can now use this file for train or test, make sure you use a difference name for different data splits next time. ****"
    print "{}.svm ".format(trainName)
    #print "./svm_learn ../{}.svm ../{}{}.model".format(TTPATH + trainName,choice,numF)
    #print "./svm_classify ../{}.svm ../{}{}.model ../{}{}.prediction".format(TTPATH + testName,choice,numF,choice,numF)
