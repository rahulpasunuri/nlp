"""
This script performs the binary feature selection. One needs to play with the combination in order to reach the multi-class feature selection.
"""
import argparse
import cPickle as pickle
import make_corpus_n
import IGer_n
CORPATH = "../corpus/"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program generates the selected features based on speficied POS/NEG partition and a n-gram length.')
    parser.add_argument('-nl','--nl', help='File that contains recipe names in the NEG partition', required=True)
    parser.add_argument('-pl','--pl', help='File that contains recipe names in the POS partition', required=True)
    parser.add_argument('-p','--p', help='Path that contains the review data represented in pickles', required=True)
    parser.add_argument('-n','--n', help='n-gram length; <1/2/3> for up to uni/bi/tri -gram', required=True)
    parser.add_argument('-f','--f', help='Fold name, use to uniquely distinguish the feature file.', required=True)
    parser.add_argument('-m','--m', help='The number of features to be selected by Information Gain', required=True)
    parser.add_argument('-e','--e', help='Extension of the pickle files that contain the reviews [DEFAULT IS .pickle] if not specified', required=False)
    parser.add_argument('-r','--r', help='Do you want to re-compute the Information Gain values? <y> <n>', required=True)
    args = vars(parser.parse_args())
    if 'e' not in args: args['e'] = "pickle"
    args['p'] = args['p'].strip("/") + "/"

    if args['r'] == "y": cls = make_corpus_n.CorpusMaker(neg_list = args['nl'],pos_list = args['pl'],review_path = args['p'],ngram_n = args['n'], fold_name  = args['f'], extension = args['e']) ##Ngram-n is the ngram number: up to which.
    if args['r'] == "y": cls.make_corpus()
    
    if args['r'] == "y":
        IGer_n.pre_IG_n(neg_list = args['nl'],pos_list = args['pl'],review_path = args['p'],ngram_n = args['n'], fold_name = args['f'],extension = args['e'])##Ngram-n is the ngram number: up to which.
        
    ig_dict = pickle.load(open(CORPATH + args['f']+ "_pre_IG.pickle","rb"))
        ##load the PREIG file from the folder, and we will always call this IG functions.
    num_f = int( args['m'])
    IGer_n.IG_n(ig_dict,num_f,args['f'])
