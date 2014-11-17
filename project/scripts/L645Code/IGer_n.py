## Note the naming difference: this script is for Word and POS ngram, up to tri-grams.
##Note that this script extracts POS and Ngram features together.
##So it needs to read in both pickles
import re
import cPickle as pickle
from collections import defaultdict
import math
#import inverseBN
#from inverseBN import *
#from nltk import ngrams as ngtool
import nltkngram
from nltkngram import *
CORPATH = "../corpus/" 

def IG_n(ig_dict,numFeatures,fold_name):
    ig_list = [[v,k] for k,v in ig_dict.items()]
    ig_list.sort()
    cut_off = len(ig_list) - numFeatures
    cut_off = max(0, cut_off)
    pickle.dump(ig_dict,open(CORPATH + fold_name + "_igdict.pickle","wb"))
    pickle.dump(ig_list[cut_off:],open(CORPATH + fold_name +"_IG.features","wb")) ##ma
    print "Done selecting features! The number of features that Information Gain used:", len(ig_list[cut_off:])
    print "The name of this feature file is called {0} : Make sure to use a different FOLD NAME for different data partitions.".format(CORPATH + fold_name +"_IG.features" )
    OUT = open(CORPATH + fold_name +"_IGvalue.dat","w")
    for v,k in ig_list:
        OUT.write("{}\t{}\n".format(v,k))
    OUT.close()

def pre_IG_n(neg_list,pos_list,review_path,ngram_n, fold_name,extension ): ##Ngram-n is the ngram number: up to which.
    ##We should do this in a faster manner.  Keep track of
    ## how many documents a word occured in NEG and POS.
    ## subtract from that we can know how many docs not contain this particular word.
    if int(ngram_n)==2:
        bigram_do = True
        trigram_do = False
    elif int(ngram_n) ==3:
        trigram_do = True
        bigram_do = True
    else:
        bigram_do = False
        trigram_do = False
    extension = "." + extension

    Adict = defaultdict(lambda:0)
    Bdict = defaultdict(lambda:0)

    As = {}
    Bs = {}
    Cs = {}
    Ds = {}
        
    negInstances = pickle.load(open(neg_list,"rb"))[:]
    posInstances = pickle.load(open(pos_list,"rb"))[:]

    ## XXXX this should be the positive corpus filename.
    pd = pickle.load(open(CORPATH + fold_name + "_pos_corpus.pickle","rb"))

    numPOSdoc = len(posInstances)
    numNEGdoc = len(negInstances)
    N = numPOSdoc + numNEGdoc
    print("the number of positive and negative instances {} {} press Enter to continue".format(numPOSdoc,numNEGdoc))
    count =0
    for poscase in posInstances[:]:
        if len( poscase.strip()) ==0: continue
        print "POS instance", count 
        count +=1
        wrd_comments = pickle.load(open( review_path + poscase + extension,"rb"))

        for cmt in wrd_comments:  ##actually there is only one comment
            for sent in cmt:
                if bigram_do: bigrams = ngtool(sent,2)
                else: bigrams = []
                if trigram_do: trigrams = ngtool(sent,3)
                else: trigrams = []
                bigrams = ["{}##{}".format(x.lower(),y.lower()) for x,y in bigrams]
                trigrams = ["{}##{}##{}".format(x.lower(),y.lower(),z.lower()) for x,y,z in trigrams]

                ngrams  = sent + bigrams + trigrams
                for word in ngrams:
                    Adict[word.lower()] +=1 

    count = 0
    print "**** Adict length\t",len(Adict)
    for negcase in negInstances:
        if len( negcase.strip()) ==0: continue
        print "NEG instance", count
        count +=1
        wrd_comments = pickle.load(open( review_path + negcase + extension,"rb"))

        for cmt in wrd_comments:  ##actually there is only one comment
            for sent in cmt:
                if bigram_do: bigrams = ngtool(sent,2)
                else: bigrams = [] 
                if trigram_do :trigrams = ngtool(sent,3)
                else: trigrams = [] 
                bigrams = ["{}##{}".format(x.lower(),y.lower()) for x,y in bigrams]
                trigrams = ["{}##{}##{}".format(x.lower(),y.lower(),z.lower()) for x,y,z in trigrams]

                ngrams  = sent + bigrams + trigrams
                for word in ngrams:
                    Bdict[word.lower()] +=1

    print "**** Bdict length\t",len(Bdict)
    print "converting dictionaries for IG..."
    
    ##there is something we can change baout it: we can use PD + ND
    pc0 = numNEGdoc*1.0 / (numNEGdoc + numPOSdoc)
    pc1 = 1 - pc0
    ig_dict = {}

    #raw_input("Type to continue.... {}{}".format(pc0,pc1))
    print "Calculating IG score for all words in the POS corpus."
    for word in pd:#vocab: ##should be pd for one-way
        ##If the word is appears in a positive document, we can find it.
        ##If not, A=0, and Nc1t0 = numPositive Document. 
        try:
            A = Adict[word]
        except:
            A =0
        try:
            B = Bdict[word]
        except:
            B  =0
            
        C = numPOSdoc - A
        D = N - numPOSdoc - B 
        
        #raw_input("{} in total!!!".fomrat(N))
        pt0 =  max(0.0000001,(C+D) * 1.0/N) ##number of cases that this word is not present.
        pt1 = max(0.0000001,1 - pt0)   ##probability that this word is present

        pc0t0 = max(D*1.0/N,0.0000001)
        pc0t1 = max(B*1.0/N,0.0000001)
        pc1t0 = max(C*1.0/N,0.0000001)
        pc1t1 = max(A*1.0/N,0.0000001)
        
        ig = pc0t0 * math.log(        pc0t0  /(pc0 * pt0     )      ) +\
             pc0t1 * math.log(        pc0t1  /(pc0 * pt1     )      ) +\
             pc1t0 * math.log(        pc1t0  /(pc1 * pt0     )      ) +\
             pc1t1 * math.log(        pc1t1  /(pc1 * pt1     )      )

        #assert ig > =0  ##if cannot be less than zero, entropy is never less than zero, uncertainty is never increased
        ig_dict[word] = ig
        assert ig >=0
    pickle.dump(ig_dict,open(CORPATH +fold_name + "_pre_IG.pickle","wb"))
    return ig_dict
