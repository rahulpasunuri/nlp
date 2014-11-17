"""
This file converts the CSV file format to a format that can be used by SVM-light
This setting is for independent study ONly.
"""
import sys
import os
import cPickle as pickle
import tools

def convert(trainf):
    ### This normalized the features column by column, not by all.
    ### By all would not work that way.
    trainIN = open(trainf,"r")
       ##when everything is done, we need to recover and make training/testing separately.

    csvlines = trainIN.readlines()[1:]
    split = len(csvlines)
    trainIN.close()
    
    header = csvlines[0] ##the first line
    nfeature =  len(header.strip().split(",")) -1  ##the number of features

    matrix = []
    labels = []
    print "\tNow making values out of input"
    for instance in csvlines:
        eles = instance.strip().split(",")
        matrix.append([float(x) for x in eles[:nfeature]])
        labels.append(eles[-1])

    print "\tNow calling the numpy script to normalize"
    normallines = tools.normalize_list(matrix)
    
    svmlines = []
    print "\tNow writing the file in SVM compatable format."
    for p in range(len(normallines)):
        instance = normallines[p]
        label = labels[p]
        this_line = [label]
	for i in range(len(instance)):
            #if instance[i] ==0: continue
            if instance[i] != 0.0: this_line.append("{}:{}".format(i+1,instance[i]))
        sthis_line = " ".join(this_line) + "\n"##the string of this line
        svmlines.append(sthis_line)
    
    svmtrain = svmlines[:split]
    Otrain = open(trainf + ".svm","w")
    Otrain.writelines(svmtrain)
 
    Otrain.close()

    ##Now remove these large inter-files.
    return normallines
    

def convertSVM(filename,Normal):

    maxWeight = 0

    IN = open(filename,"r")
    lines = IN.readlines()[1:]  ##the first line is just a header
    IN.close()

    svmlines = []
    for line in lines:
        fields = line.strip().split(",")

        length = len(fields)
        label = fields[-1]
       
        ##### This part is for SVM multi-class classification.
        tag = label
        print "====== ",tag

        """
        #### This part is for SVM binary classification. 
        if label == POS:
            tag = '+1'
        elif label == NEG:
            tag = '-1'
        else:
            print "Incorrect lable!"
            raise
        """
        pairs = [tag]
        for i in range(1,length):
            if float(fields[i-1]) ==0: continue
            
            pairs.append(  ":".join([str(i),str(float(fields[i-1])/Normal)])  )

            if float(fields[i-1]) > maxWeight:
                maxWeight = float(fields[i-1])

        svmline = " ".join(pairs) + "\n"

        svmlines.append(svmline)

    print "Done!",maxWeight
    #pickle.dump(maxWeight,open("max.pickle","wb"))

    OUT = open(filename+ ".svm","w")
    OUT.writelines(svmlines)
    OUT.close()
    return maxWeight

def testcase1():
    global TRAIN,TEST,MAX
    TRAIN = sys.argv[1]
    TEST = sys.argv[2]
    convert(TRAIN,TEST)    
    #tools.list2file(data,"../TT4classify/test.norm")
if __name__ == "__main__":
    #convertSVM("BNS4500train.csv")
    #convertSVM("BNS4500test.csv")
    
    testcase1()
    """
    global TRAIN,TEST,MAX
    TRAIN = sys.argv[1]
    TEST = sys.argv[2]
    MAX = float(sys.argv[3])
    convertSVM(TRAIN,MAX)
    convertSVM(TEST,MAX)
    """
    ##use the following command for SVM-light classifier. 

    
