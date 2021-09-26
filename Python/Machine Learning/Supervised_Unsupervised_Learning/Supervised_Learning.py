#!/usr/bin/env python
# coding: utf-8

# In[52]:


# CS379 - Machine Learning
# Christopher Lakey
# Colorado Technical University
# Unit 1 Invididual Project
# Titanic Clustering and Prediction Models

# This section is the supervised machine learning model using k-means to describe the titanic dataset

# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.utils import get_dataset_names


# In[2]:


# Load in the dataset
titanic = sns.load_dataset('titanic')


# In[3]:


# print dataset to ensure it is loaded in correctly
print('Headers:')
print(titanic.head(10))


# In[4]:


# Print the number of rows and columns
print('Number of columns and rows:')
print(titanic.shape)


# In[5]:


# Describe the data to learn more information about it (Age count is less than 891 therefore we can tell data is
# missing)
print('Data Description:')
print(titanic.describe())


# In[6]:


# Count the number of survivors
print("Number of survivors:")
print(titanic['survived'].value_counts())


# In[7]:


# Visualize the counts of survivors versus deceased
sns.countplot(titanic['survived'], label="Count")


# In[12]:


# Visualize the counts of survivors based on who, sex, pclass, sibsp, parch, and embark
cols = ['who', 'sex', 'pclass', 'sibsp', 'parch', 'embarked']

n_rows = 2
n_cols = 3

# define the subplot grid and the figure size for the graph
# return the figure and the axes object
fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols*3.2, n_rows*3.2))

for r in range(0, n_rows):
   for c in range(0, n_cols):
        i = r*n_cols+ c #loop through the columns     
        ax = axs[r][c] #Visualize where to position for each subplot
        sns.countplot(titanic[cols[i]], hue=titanic["survived"], ax=ax)
        ax.set_title(cols[i])
        ax.legend(title="survived", loc='upper right') 
        
plt.tight_layout()   #tight_layout


# In[13]:


# Check survival rate by sex
titanic.groupby('sex')[['survived']].mean()


# In[14]:


#Check survival rate by sex and class
titanic.pivot_table('survived', index='sex', columns='class')


# In[15]:


#Visualize survival rate by sex and class
titanic.pivot_table('survived', index='sex', columns='class').plot()


# In[16]:


#Use the bar plot to visualize the survival rate of each class.
sns.barplot(x='class', y='survived', data=titanic)


# In[17]:


#Check survival rate by sex, age and class
age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')


# In[19]:


# Use a scatter plot to plot the Prices Paid Of Each Class
plt.scatter(titanic['fare'], titanic['class'],  color = 'purple', label='Passenger Paid')
plt.ylabel('Class')
plt.xlabel('Price / Fare')
plt.title('Price Of Each Class')
plt.legend()
plt.show()


# In[20]:


#Count the missing or empty values for each column 
titanic.isna().sum()


# In[21]:


# Look for redudant coluns that we do not need
for val in titanic:
   print(titanic[val].value_counts())
   print()


# In[22]:


# Drop Columns that are not needed
titanic = titanic.drop(['deck', 'embark_town', 'alive', 'class', 'alone', 'adult_male', 'who'], axis=1)

#Clean up row data by removing missing values
titanic = titanic.dropna(subset =['embarked', 'age'])


# In[23]:


#Count the new columns and rows in dataset after removing uneccassary data
titanic.shape


# In[24]:


#Check to see what columns need to be encoded as numeric data so they can be used in future functions.
titanic.dtypes


# In[25]:


#Find and print the unique values in the columns
print(titanic['sex'].unique())
print(titanic['embarked'].unique())


# In[26]:


#This function changes the object data types into integers so we can use them for numeric calculations
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

#This function encodes the sex column to change them from objects to numeric data
titanic.iloc[:,2]= labelencoder.fit_transform(titanic.iloc[:,2].values)
print(labelencoder.fit_transform(titanic.iloc[:,2].values))

#This function encodes the embarked column to change them from objects to numeric data
titanic.iloc[:,7]= labelencoder.fit_transform(titanic.iloc[:,7].values)
print(labelencoder.fit_transform(titanic.iloc[:,7].values))

# Show the encoded columns new unique values
print(titanic['sex'].unique())
print(titanic['embarked'].unique())


# In[27]:


#Split the data independent (X) and Dependent (Y) variables for creating predictions later.
X = titanic.iloc[:, 1:8].values 
Y = titanic.iloc[:, 0].values 


# In[28]:


# Split the dataset into two sets. 80% for training and 20% for testing so we can test our prediction accuracy.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# In[29]:


#Building a function that contains all the different machine learning models we may use for our predictions
def models(X_train,Y_train):
     
    # This function uses the logistical Regression algorithm on the training set.
    # Logistical Regression is an algorith used to classify data as 1 or 0 and then use the output to make predictions on the 
    # classified data.
    from sklearn.linear_model import LogisticRegression
    log = LogisticRegression(random_state = 0)
    log.fit(X_train, Y_train)

    # This function allows us to use the k-nearest neigbor algorithm in our program.
    # The K-Nearest Neigbor algorithm is a classification algorithm that does not assume anything about the data and
    # if you were to visualize it, the data set gets plotted onto a graph and the clusters of plotted points indicate
    #higher probabilites of a certain measure depending on the plot.
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    knn.fit(X_train, Y_train)

    # This function allows us to use the support vector machine algorithm.
    # support vector machine algorithm is a classification machine learning model in which the data is plotted onto a graph and 
    # that data is seperated by a descision line on the hyperplane and we classify those points based on the line of decision. 
    from sklearn.svm import SVC
    svc_lin = SVC(kernel = 'linear', random_state = 0)
    svc_lin.fit(X_train, Y_train)

    # This function allows us to use the support vector machine with the kernal trick algorithm. This algorithm is similar to 
    # the regular support vector algorithm but it can be used on non linear datasets.
    from sklearn.svm import SVC
    svc_rbf = SVC(kernel = 'rbf', random_state = 0)
    svc_rbf.fit(X_train, Y_train)

    # This function allows us to use the Naïve Bayes Algorithm
    # The Naïve Bayes Algorithm is a classification algorithm based on the Bayes Theorem and uses statistical probability
    # to make predictions about datasets.
    from sklearn.naive_bayes import GaussianNB
    gauss = GaussianNB()
    gauss.fit(X_train, Y_train)

    # This function allows us to use the decision tree algorithm.
    # The decision tree algorithm is a supervised classification algorithm that creates a training model to predict a value
    # of a specific variable by creating learninfg simple decision rules from prior training data.
    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    tree.fit(X_train, Y_train)

    # This function allows us to use the random forest classifier algorithm
    # The random forest classifier algorithm uses numerous decision trees that work in unison to create predictions and the 
    # specific decison tree that gets the most votes on it's accuracy is the one that is used for the model's predictions.
    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    forest.fit(X_train, Y_train)

    # The code below will print the accuracy of each algorith we plug our titanic datset into.
    print('[0]Logistic Regression Training Accuracy:', log.score(X_train, Y_train))
    print('[1]K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
    print('[2]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train, Y_train))
    print('[3]Support Vector Machine (RBF Classifier) Training Accuracy:', svc_rbf.score(X_train, Y_train))
    print('[4]Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train, Y_train))
    print('[5]Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
    print('[6]Random Forest Classifier Training Accuracy:', forest.score(X_train, Y_train))

    return log, knn, svc_lin, svc_rbf, gauss, tree, forest


# In[30]:


#Gather and train our models
model = models(X_train,Y_train)


# In[32]:


from sklearn.metrics import confusion_matrix 
for i in range(len(model)):
    cm = confusion_matrix(Y_test, model[i].predict(X_test)) 
    #extracting TN, FP, FN, TP
    TN, FP, FN, TP = confusion_matrix(Y_test, model[i].predict(X_test)).ravel()
    print(cm)
    print('Model[{}] Testing Accuracy = "{} !"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
    print()# Print a new line


# In[33]:


#Get the importance of the features
forest = model[6]
importances = pd.DataFrame({'feature':titanic.iloc[:, 1:8].columns,'importance':np.round(forest.feature_importances_,3)})
importances = importances.sort_values('importance',ascending=False).set_index('feature')
importances


# In[34]:


#Visualize the importance
importances.plot.bar()


# In[35]:


#Print Prediction of Random Forest Classifier model
pred = model[6].predict(X_test)
print(pred)

#Print a space
print()

#Print the actual values
print(Y_test)


# In[36]:


my_survival = [[3,1,30,1, 0, 0, 1]]
#Print Prediction of Random Forest Classifier model
pred = model[6].predict(my_survival)
print(pred)

if pred == 0:
  print("You didn't make it")
else:
  print('You survived')


# In[37]:


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




