#!/usr/bin/env python
# coding: utf-8

# In[83]:


# CS379 - Machine Learning
# Christopher Lakey
# Colorado Technical University
# Unit 3 Invididual Project
# Predicting Credit Card Fraud

# Objective:
# In this project I will be attempting to predict credit card fraud with a provided dataset. Credit card fraud prediction
# is one of the many uses of machine learning. With modern applications of these prediction techniques it is easier for
# banks to predict these instances and respond quickly and accuratly. I have had my card deactivated for an incorrect 
# fraud flag and I like to think that machine learning prevents this type of thing from happening a lot. What you will see
# In this assignment is me trying to use the provided dataset and failing at it so I tried to use another example 
# from Kaggle to come up with some kind of solution to this task. I apologize ahead of time if I dod this completley wrong
# but I did my best.

#Import Libraries 

from scipy.io import arff
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


# Here I am naming my datafile df and loading a library to unpack the arff file type into readable data.
# I then load that data into a dataframe using pandas so I can manipulate the data.
# Printing information about the data so I can assess what I am working with.

filename  = "C:/Users/lakey/Desktop/credit_fraud.arff"
data = arff.loadarff(filename)
df = pd.DataFrame(data[0])
df.info()


# In[3]:


# Checking the data for null or missing values and finding that there is not missing data.
df.isnull().sum()


# In[4]:


df.mean() # Checking the mean of the data


# In[5]:


# looking at more details of the data to find how I am going to predict credit card fraud using it.
df.describe() 


# In[6]:


# Printing the first few columns of data so I can look at it to determine what I have to work with.
df.head()


# In[7]:


#Checking the shape of the data to see how many records and columns I have.
print(df.shape)


# In[8]:


# Checking a histogram of the data to see if I can find any correlations between fields.
df.hist(figsize=(20, 20))
plt.show()


# In[9]:


# Still looking for what data in this file is relevant to finding credit card fraud.
# checking a plot of the data to see if I can see anything there.
plot = sns.pairplot(df)
plot.add_legend()
plt.show()


# In[10]:


# from what I can tell there is nothing to go on here for a time series algorithm. 
# For one the data is not temporal, in other words there is no duration or observations of data over time.
# Unfortunately I don't think I can use this data to detect credit card fraud or I don't have the skill to do it.
# Researching another example to do this project with.....


# In[46]:


# Found a new example on Kaggle to attempt this with.
# Import packages
                   
from sklearn.linear_model import LinearRegression,LogisticRegression,SGDRegressor , Ridge,Lasso
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import LabelEncoder,StandardScaler
from warnings import filterwarnings
filterwarnings('ignore')
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix
from sklearn.metrics import classification_report,roc_curve,roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


# In[47]:


# Load new data files
train = pd.read_csv('C:/Users/lakey/Desktop/fraudTrain.csv')
test = pd.read_csv('C:/Users/lakey/Desktop/fraudTest.csv')
# Print the heads to take a look at the data
train.head()


# In[48]:


test.head()


# In[82]:


# appending the training and test data together.
df = pd.concat([train,test],ignore_index=True)
df.drop('Unnamed: 0',axis=1,inplace=True)


# In[50]:


# Print the head of the new datafile to see what the data looks like.
df.head()


# In[51]:


#Check the shape of the data to see how many rows/columns there are.
df.shape


# In[52]:


# Checking on the data types of the file.
df.info()


# In[53]:


# Seperating the numerical data from the catigorical data so analysis can be done on it.
df_cat = df.select_dtypes(include = 'object')
df_num = df.select_dtypes(exclude = 'object')
le = LabelEncoder()


# In[55]:


# Checking for blank or null values that might throw off the models.
nan_df = pd.DataFrame(data = (df.isnull().sum()/len(df))*100,columns = ['% of missing values'])
nan_df


# In[56]:


# Fitting the gender column to be used in the models.
df['gender_le']  = le.fit_transform(df['gender'])


# In[57]:


# Getting rid of object type data in the data files.
# Removing some of the data so itr does not take forever to process.
df2 = df.select_dtypes(exclude = 'object')
df2 = df2.loc[:149999]


# In[58]:


# Check out the tranformations made to the data.
df2.head()


# In[59]:


# Getting rid of the CCC number field because we don't need it for predictions.
df2 = df2.drop(['cc_num'],axis=1)
# Dropping the is fraud fields to clean the data and setting it to the x independent variable.
x = df2.drop('is_fraud',axis=1)
# Setting the is fraud as the Y dependent variable.
y = df2['is_fraud']


# In[60]:


#Splitting the data into training and test sets using a 70/30 split.
xtrain,xtest,ytrain,ytest = train_test_split(x,y,train_size = 0.7 , random_state = 10)


# In[61]:


# Cleaning the cc_num Column.
df_num = df_num.drop(['cc_num'],axis=1)


# In[62]:


# Cleaning the is fraud column.
df_num = df_num.drop('is_fraud',axis=1)


# In[63]:


# Using a scaler to scale the data meaning we are getting the data on the same level of scale because the
# algorithms cannot tell what the data is. This makes the results more accurate.
ss = StandardScaler()
xtrain[df_num.columns] = ss.fit_transform(xtrain[df_num.columns])
xtest[df_num.columns] = ss.fit_transform(xtest[df_num.columns])


# In[64]:


#setting a logistical regression model to a variable andf fitting the data for use later in the program.

lr = LogisticRegression()
model_v1 = lr.fit(xtrain,ytrain)


# In[65]:


# Create a confusion matrix for the logistical regression.

ypred = model_v1.predict(xtest)
cm  = confusion_matrix(ytest,ypred)
sns.heatmap(cm,annot=True)
plt.show()


# In[66]:


# Printing a classification report to see the precision and recall of the model.
# Precision is checking what proportion of positive identifications were actually correct?
# Recall is checking what proportion of actual positives were identified correctly?
print(classification_report(ytest,ypred))


# In[67]:


# Using the K-Nearest Neighbors model to see the accuracy on the data.
knn = KNeighborsClassifier()
model_v2 = knn.fit(xtrain,ytrain)
ypred1 = model_v2.predict(xtest)


# In[68]:


# Showing the confusion matrix based on the K-nearest neighbors model.
cm_knn = confusion_matrix(ytest,ypred1)
sns.heatmap(cm_knn,annot=True)


# In[69]:


# Printing the classification report based on the k-nearst neighbor model.
print(classification_report(ytest,ypred))


# In[70]:


# Using the Naive Bayes model to see the accuracy on the data.
nb =GaussianNB()
model_v3 = nb.fit(xtrain,ytrain)


# In[71]:


# Showing the confusion matrix based on the Naive Bayes model.
ypred = model_v3.predict(xtest)
cm = confusion_matrix(ytest,ypred)
sns.heatmap(cm,annot=True)


# In[72]:


# Printing the classification report based on the Naive Bayes model.
print(classification_report(ytest,ypred))


# In[73]:


# Showing the ROC curve for the logistical regression model.
# ROC curve is hjust a way of viewing the precision of the model visually.
## Logistic Regression Model
prob = model_v1.predict_proba(xtest)[:,1]
fpr,tpr,threshold = roc_curve(ytest,prob)
plt.plot(fpr,tpr)
plt.plot([[0,0],[1,1]],color='red',linestyle = '-')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC Curve')
plt.show()


# In[75]:


# Showing the ROC curve for the K-Nearest Neighbors Model.
prob1 = model_v2.predict_proba(xtest)[:,1]
fpr,tpr,threshold = roc_curve(ytest,prob1)
plt.plot(fpr,tpr)
plt.plot([[0,0],[1,1]],color='red',linestyle = '-')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC Curve')
plt.show()


# In[76]:


# Showing the ROC curve for the Naive Bayes Model
prob2 = model_v3.predict_proba(xtest)[:,1]
fpr,tpr,threshold = roc_curve(ytest,prob2)
plt.plot(fpr,tpr)
plt.plot([[0,0],[1,1]],color='red',linestyle = '-')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC Curve')
plt.show()


# In[77]:


# K-nearest neighbors had the best precision out of all the models. So we will use that for predictions.


# In[78]:


# Setting up the prediction using the KNN model.
ypred = model_v2.predict(xtest)


# In[79]:


# Setting up the table to print our prediction results.
prediction = pd.DataFrame()
prediction['Serial No.'] = xtest.index
prediction['is_fraud_pred'] = ypred


# In[80]:


# Printing the prediction results
prediction[prediction['is_fraud_pred']==1]


# In[84]:


# Conclusion
# For this assignment I tried my best attempt at doing a credit card fraud analysis.
# I obviously used an existing example and explained what happened in it because I don't understand enough about machine learning to write the code from
# Scratch. I totally would if I knew how. Also I did not use the original dataset because I did not understand how the data in
# the dataset related to credit card fraud by just listing demographics of customers at a bank. It may just be my misunderstanding but
# I really tried to go through the example and understand the methods used to create credit card fraud predictions.

# References:

#    Google. (n.d.). Classification: Precision and Recall &nbsp;|&nbsp; Machine Learning Crash Course. Google. 
#        https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall. 
    
#    Roy, B. (2020, April 7). All about Feature Scaling. Medium. https://towardsdatascience.com/all-about-feature-scaling-
#            bcc0ad75cb35. 
    
#   ULB, M. L. G.-. (2018, March 23). Credit Card Fraud Detection. Kaggle. https://www.kaggle.com/mlg-
#        ulb/creditcardfraud. 

