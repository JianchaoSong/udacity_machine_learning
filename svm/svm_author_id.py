#!/usr/bin/python

""" 
this is the code to accompany the Lesson 2 (SVM) mini-project

use an SVM to identify emails from the Enron corpus by their authors

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

  
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

#########################################################
### your code goes here ###
from sklearn.svm import SVC
svc = SVC(C=10000.0, kernel='rbf')
svc.fit(features_train, labels_train)
labels_pred = svc.predict(features_test)

print labels_pred[10]
print labels_pred[26]
print labels_pred[50]

import numpy as np

print 'Chris(1) is %d' % np.bincount(labels_pred)[1]

from sklearn.metrics import accuracy_score

print accuracy_score(labels_test, labels_pred)


# C Parameter
# 1.0 => 61.6%, 10.0 => 61., 100.0 => 61.6, 1000=>82.1, 10000=>89.2

#########################################################

