# In[37]:

# CS379 - Machine Learning
# Christopher Lakey
# Colorado Technical University
# Unit 1 Invididual Project
# Titanic Clustering and Prediction Models

# This section is the unsupervised machine learning model using k-means to describe the titanic dataset


# In[38]:


import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd


# In[39]:


'''
This refers to the passenger class level in our data -> Pclass (1 = 1st; 2 = 2nd; 3 = 3rd)
This refers to the data showing survival in our dataset -> survival (0 = No; 1 = Yes)
This refers to the name data in our dataset -> name 
This refers to the sex of the passenger in our dataset -> sex  
This refers to the age of the passenger in our dataset -> age 
This refers to if the passenger had siblings aboard the titanic in our dataset -> sibsp 
This refers to if the passenger had parents/children aboard the titanic in our dataset ->parch 
This refers to the ticket number of the passenger in our dataset -> ticket
This refers to the ticket price of the passenger in our dataset -> ticket fare
This refers to the cabin of the passenger in our dataset -> cabin
This refers to the location the passenger left from of the passenger in our dataset -> embarked  (C = Cherbourg; Q = Queenstown; S = Southampton)
This refers to the which lifeboat the passenger was in, in our dataset -> boat 
This refers to the passenger's body identification number in our dataset -> body
This refers to the passenger's end destination in our dataset -> home.dest
'''


# In[42]:


#Reading the excel data and setting it to the variable df
file_path = "C:/Users/Chris Lakey/Desktop/CS479_Machine_Learning_U1_IP1_Christopher Lakey/titanic.xls"
df = pd.read_excel(file_path)
# Removing unnecessary columns body and name from the dataset
df.drop(['body','name'], 1, inplace=True)
# Remove the data that is blank or missing from the dataset
df.fillna(0, inplace=True)


# In[44]:


# This function is encoding the non numeric data like we did in the supervised alogirthms above
def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))


    return df


# In[45]:


# Running the function on the cleaned data
df = handle_non_numerical_data(df)


# In[46]:


# Drop the unneeded columns in the dataset
df.drop(['sex','boat'], 1, inplace=True)
X = np.array(df.drop(['survived'], 1).astype(float))
# Standardize the X variable along the axis
X = preprocessing.scale(X)
#Create an array of the Y variables based on the survived coulmn
y = np.array(df['survived'])


# In[47]:


# Set the clf variable to the K-Means algorithm and set the n-clusters to 2
clf = KMeans(n_clusters=2)


# In[48]:


# Fit the model to our dataset
clf.fit(X)


# In[49]:


#Set the correct variable to 0
correct = 0


# In[50]:


# loop thorough our dataset and run the K-means algorthm to predict the points to cluster our dataset
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = clf.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1


# In[51]:


# Print the the amount of correct points based on predictions.        
print(correct/len(X))


# In[ ]:




