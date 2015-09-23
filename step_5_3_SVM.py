"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import cross_validation
#from sklearn.utils.validation import check_arrays


from numpy import array
from sklearn.svm import LinearSVC

#read the reviews and their polarities
reviews=[]
polarities=[]
f=open('E:\\Stevens_sem2\\Research_work\\reviewer_documents\\mr-cranky.txt')
for line in f:
    review,rating=line.strip().split('\t')    
    reviews.append(review.lower())    
    polarities.append(int(rating))
f.close()

#count the number of times each term appears in a document and transform each doc into a count vector
counter = CountVectorizer()
counts = counter.fit_transform(reviews)

#transform the counts into the tfidfd format. http://en.wikipedia.org/wiki/Tf%E2%80%93idf
transformer = TfidfTransformer().fit(counts)
transformedPoints = transformer.transform(counts)

#print transformer
#print transformedPoints

#perform a multi-fold cross validation and get the accuracy for each fold
SVMresult =  cross_validation.cross_val_score(LinearSVC(), transformedPoints, array(polarities), cv=10)


print SVMresult


total_1 = 0
for values in SVMresult:
    total_1 = total_1 + values

ava_kmean = total_1/10;
print 'kmean',ava_kmean


"""
TFIDF takes into account that:
-longer docs are expected to have higher word counts. Which is more likely to be negative? A 50 word doc
that contains the word 'terrible' 5 times or a 1000 word doc that contains the word 'terrible' 7 times?
-words that appear in many docs are not informative (think of stopwords)
"""