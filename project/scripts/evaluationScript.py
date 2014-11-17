##This is the evaluation script
##Follow the instruction using --help
## L645, Fall 2014
## Note: this script does not do multi-fold evaluation together, but you can pass the 'count_dict' to another function, or parse the screen output from command line. 
import argparse
import pickle
from collections import defaultdict

def read_predictions(predfile):
    print "this is not done!"
    preds = open(predfile,"r").readlines()
    preds = [x.strip() for x in preds if len(x.strip())!=0]
    return preds

def evaluate(predictions, recipe_file):
    recipes = pickle.load(open(recipe_file,"rb"))
    golds = [int(x.strip().split("_")[0]) for x in recipes if len(x.strip())!=0]
    assert len(golds) == len(predictions)
    paired = zip(predictions, golds)
    print paired ,golds,predictions
    ##We will need the actual number of golds, the number of predictions, and then calculate the values
    count_dict = defaultdict( lambda: defaultdict(lambda:0))
    for pred,gold in paired:
        count_dict[int(gold)]["gold"] +=1
        count_dict[int(pred)]["pred"] +=1
        if int(pred) == int(gold):
            count_dict[int(gold)]["right"] +=1

    print "*** Here are the numbers for each fork ***"
    ##In the end, let's print out the statistics that we calculated.
    correct = 0
    for key in [1,2,3,4]:
        precision = count_dict[key]["right"]*1.0/ max(0.01,count_dict[key]["pred"]) 
        recall = count_dict[key]["right"]*1.0/ max(0.01,count_dict[key]["gold"] )

        if count_dict[key]['pred'] ==0: precision = "NAN"
        if count_dict[key]['gold'] ==0: recall = "NAN"
        print "{0}-FORK    Precision {1}  Recall {2}  Number of predictions {3}".format(key,precision,recall,count_dict[key]["pred"])
        correct += count_dict[key]['right']
    ##We also need to calculate the accuracy overall.   
    print "*"*20
    print "Total number of instances: {0} ; Correct instances: {1}; accuracy: {2}".format(len(golds),correct,1.0*correct/len(golds))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is the evaluation program')
    parser.add_argument('-p','--p', help='The file that contains the SVM predictions', required=True)
    #parser.add_argument('-f','--f', help='Fold name, use to uniquely distinguish the feature file.', required=True)
    parser.add_argument('-r','--rl', help='The list of recipe names in PICKLE format, this should be same as the file you used for constructing the data vectors.', required=False)
    args = vars(parser.parse_args())

    preds = read_predictions(args['p'])
    evaluate(preds,args['rl'] )


    
