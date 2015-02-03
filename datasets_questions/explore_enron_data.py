#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0
pois_name = []
for key,val in enron_data.items():
    print key,'\n\t',val
    if val["poi"] == True:
        pois_name.append(key)
        count = count + 1
    else:
        pass
    
print 'POI\'s full names\n'
for name in pois_name:
    print name
print 'totally %d peoples' % len(pois_name)

print 'total stock of James Prentice is ' , enron_data['PRENTICE JAMES']['total_stock_value']
print 'number of emails from Wesley Colwell to POIs : ', enron_data['COLWELL WESLEY']['from_this_person_to_poi'] 
print 'stock options exercised by Jeffrey Skilling : ', enron_data['SKILLING JEFFREY K']['exercised_stock_options']