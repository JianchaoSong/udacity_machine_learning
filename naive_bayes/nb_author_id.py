#!/usr/bin/python

"""
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project

    use a Naive Bayes Classifier to identify emails by their authors
   
    authors and labels:
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



print len(features_test)
print len(labels_train)
print len(features_test)
print len(labels_test)
#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
gnb =GaussianNB()
t0 = time()
gnb.fit(features_train[0:1758], labels_train[ 0: 1758])
print "training time:" , round(time() - t0, 3), "s"


from sklearn.metrics import accuracy_score
t1 = time()
labels_pred = gnb.predict(features_test[ 0: 1758])    # Why predicting time is greater than fitting time?
print "predicting time:" ,round(time() - t1, 3),"s"

print accuracy_score(labels_test[0 :1758 ], labels_pred[0:1758])

#########################################################

  
