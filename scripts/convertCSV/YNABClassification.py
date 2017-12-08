# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%reset -f

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

#import nltk
#nltk.download()

#english_vocab = set(w.lower() for w in nltk.corpus.words.words())

dataset = pd.read_csv("D:/ML Datasets/YNAB/Register.csv")

del dataset["Flag"]
del dataset["Cleared"]
del dataset["Category Group"]
del dataset["Category"]
dataset["Category"] = dataset["Category Group/Category"]
del dataset["Category Group/Category"]

dataset.Outflow = dataset['Outflow'].replace( '[\$]','', regex=True )
dataset.Inflow = dataset['Inflow'].replace( '[\$]','', regex=True )

dataset.Outflow = dataset['Outflow'].map(float)
dataset.Inflow = dataset['Inflow'].map(float)


#Clean up our category data, we're merging Payee and Category
dataset.Payee = dataset['Payee'].replace( np.nan,'', regex=True )
dataset.Category = dataset['Category'].replace( np.nan,'', regex=True )
dataset.Memo = dataset['Memo'].replace( np.nan,'', regex=True )
#Merge Paye and Category
dataset["Category"] = dataset["Payee"].map(str) + dataset["Category"].map(str)
del dataset["Payee"]

#We don't need date for now
del dataset["Date"]

#Limit to only Stanchart details
dataset = dataset[dataset["Account"] == "Stan Chart"]
del dataset["Account"]


#Long ago, my first app used to add an 8 digit random string at the end of each
#transaction, I'm suffering because of that. 
memos = []
for memo in dataset.Memo.values:
    try:
        s = memo.rsplit(None, 1)[-1]
        if(len(s) == 8 and (s != "TRANSFER" or s != "cashback")):
            memos.append(memo.rsplit(' ', 1)[0])
        else:
            memos.append(memo)
    except:
        memos.append(memo)
        print("Something wong")

#dataset.Memo = memos
del dataset["Memo"]

#Data Sets                

# If you're curious we are removing the collumns from dataset because we have 
# some weird ops below
y = dataset.Category.values
del dataset["Category"]

#Categorical data
# y
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


#Stop words and friends
import re
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for memo in memos:
    s = re.sub('[^a-zA-Z]', ' ', memo)
    s = s.lower()
    s = s.split()
    ps = PorterStemmer()
    s = [ps.stem(word) for word in s if not word in set(stopwords.words('english'))]
    s = ' '.join(s)
    corpus.append(s)
    
#NLP Bag of words for Memo
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X_memos = cv.fit_transform(corpus).toarray()

df = pd.DataFrame(X_memos)
df["Outflow"] = dataset.Outflow.values
df["Inflow"] = dataset.Inflow.values
X = df.values
#X = dataset.values

model_name = "Classification"
#Create trainging and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)


#Feature scaling

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#Fitting Classifier to training set
#Create Classifier here

Y = []

#Gaussian SVM accuracy: 0.712290502793
from sklearn.svm import SVC
classifier = SVC(kernel="rbf", gamma = 0.007)
classifier.fit(X_train,y_train)
Y.append(classifier.predict(X_test))


#Linear SVM: 0.787709497207
from sklearn.svm import SVC
classifier = SVC(kernel="linear")
classifier.fit(X_train,y_train)
Y.append(classifier.predict(X_test))


#Naive Bayes: 0.737430167598
from sklearn.naive_bayes import  GaussianNB
classifier = GaussianNB()
classifier.fit(X_train,y_train)
Y.append(classifier.predict(X_test))


#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver = "sag", max_iter=200)
classifier.fit(X_train,y_train)
Y.append(classifier.predict(X_test))


#Random Forest: 0.824022346369
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(criterion="entropy", n_estimators=100)
classifier.fit(X_train,y_train)

Y.append(classifier.predict(X_test))


#KNN: 0.810055865922
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=6, metric="minkowski", p=1, weights="distance")
classifier.fit(X_train,y_train)
Y.append(classifier.predict(X_test))


df_Y = pd.DataFrame(Y)

y_pred = []
#Get Consenssus 
for i in range(0,len(y_test)):
    v = df_Y.iloc[:, i]
    #Mean doesn't work
    #y_pred.append(int(np.mean(v)))
    #Using Most frequent
    counts = np.bincount(v)
    y_pred.append(np.argmax(counts))

#Predict the test set results
#y_pred = classifier.predict(X_test)

# Making Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test,y_pred)
acs = accuracy_score(y_test,y_pred)
 


