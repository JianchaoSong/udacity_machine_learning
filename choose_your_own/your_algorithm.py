#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from hashlib import algorithms, algorithms_available

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.metrics import accuracy_score

##   Adaboost  ######################################## 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
#  
clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1), 
                         algorithm="SAMME.R",                     
                         n_estimators=100)
clf.fit(features_train, labels_train)

labels_pred = clf.predict(features_test)

accuracy_Adaboost = accuracy_score(labels_test, labels_pred, normalize=True)
print 'Accuracy of Adaboost : %.5f' % accuracy_Adaboost

##   Random Forest  ######################################## 
from sklearn.ensemble import RandomForestClassifier
 
clf = RandomForestClassifier(n_estimators=200, criterion='entropy', max_depth=5)
 
clf.fit(features_train, labels_train)
labels_pred = clf.predict(features_test) 
accuracy_RandomForest = accuracy_score(labels_test, labels_pred, normalize=True)
 
print 'Accuracy of Random Forest : %.5f' % accuracy_RandomForest

##   KNN  ######################################## 
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=22)
clf.fit(features_train, labels_train)
labels_pred = clf.predict(features_test)
accuracy_KNN = accuracy_score(labels_test, labels_pred, normalize=True)
print 'Accuracy of KNN : %.5f' % accuracy_KNN

try:
#     prettyPicture(clf, features_test, labels_test)
    prettyPicture(clf, features_test, labels_test)
    print 'Succeess'
except NameError:
    print 'Error'
    pass
