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
from numpy import NAN

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0
pois_name = []
for key,val in enron_data.items():
#     print key,'\n\t',val
    if val["poi"] == True:
        pois_name.append(key)
        count = count + 1
    else:
        pass
print 'Number of POIs %d' % count     
print 'POI\'s full names\n', pois_name

print 'total stock of James Prentice is ' , enron_data['PRENTICE JAMES']['total_stock_value']
print 'number of emails from Wesley Colwell to POIs : ', enron_data['COLWELL WESLEY']['from_this_person_to_poi'] 
print 'stock options exercised by Jeffrey Skilling : ', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# names = ['LAY KENNETH L', 'SKILLING JEFFREY K','FASTOW ANDREW S']
# for individual in names:
#     print 'total payments of '+individual + ' : '
#     print '\t\t', enron_data[individual]['total_payments']
    
## Dealing with unfilled features
salary_Nan = 0
email_Nan = 0
total_payments_Nan = 0
total_payments_Nan_dic ={}
for key,val in enron_data.items():
    if val['salary'] != 'NaN':
        salary_Nan += 1
    if val['email_address'] != 'NaN':
        email_Nan += 1
    if val['total_payments'] == 'NaN':
        total_payments_Nan += 1
        total_payments_Nan_dic[key] = val

print 'total number of people in dataset : %d' % len(enron_data)
print 'Number of folks who don\'t have a quantified salary : ',salary_Nan
print 'Number of folks who do not have e-mail addressed : ', email_Nan

print '%d(%.4f%%) people have NaN for thir total payments' %(total_payments_Nan,(float(total_payments_Nan) / len(enron_data.items()) * 100.0 ))

cnt = 0
for key,val in total_payments_Nan_dic.items():
    if val['poi'] == True:
        cnt += 1

print '%.4f%% pois do not have total payments.' % (float(cnt)/len(total_payments_Nan_dic) * 100.0)
        
