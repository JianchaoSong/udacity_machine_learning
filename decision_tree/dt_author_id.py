#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




print "Number of Features : %d" % len(features_train[0])
#########################################################
### your code goes here ###

from sklearn import tree
from sklearn import metrics

dtc = tree.DecisionTreeClassifier(criterion='entropy', min_samples_split=40)
dtc.fit(features_train, labels_train)
labels_pred = dtc.predict(features_test)

accuracy = metrics.accuracy_score(labels_test, labels_pred)

print "Accuracy : %lf " % accuracy


#########################################################


