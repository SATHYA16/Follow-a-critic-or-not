# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:02:08 2015

@author: Subu Ganesh
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import  linear_model
import numpy as np

#-------------------DATA----------------------------------
train_data=['An average meal','Average food and average service',\
'good food in a good location','The pizza is good',\
'amazing place','amazing food and great service, probably the best I have ever had']
train_labels=[0,0,1,1,2,2]

test_docs = ['The food was average', 'This place is great']
test_labels=[1,2]
#------------------------------------------------------------

regr = linear_model.LinearRegression()
count_vect = CountVectorizer(stop_words="english")
print count_vect

#VECTORIZE
train_counts = count_vect.fit_transform(train_data)
test_counts = count_vect.transform(test_docs)
print test_counts

#FIT
regr.fit(train_counts, train_labels)

#PREDICT
predicted = regr.predict(test_counts)
print predicted

#SAVE THESE
coefficients=regr.coef_

#the lower the better
print("Mean Squared Error: %.2f"
      % np.mean((predicted  - test_labels)**2))

#perfect score is 1
print('Variance score: %.2f' % regr.score(test_counts, test_labels))

#PRINT PREDICTIONS
for doc, pred in zip(test_docs, predicted):
    print('%r => %s' % (doc, pred))
