import pandas as pd
import requests, io
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

#Pull data from data.gov website and load into a dataframe/data structure.
#Verify is set to False because my computer cannot verify the SSL certificate.

data_sets = ['Demographic_Statistics_By_Zip_Code.csv']
base_url = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD"

req = requests.get(base_url, verify = False)
url_content = req.content
c = pd.read_csv(io.StringIO(url_content.decode('utf-8')))
print(c.describe())

# Plot data points from file on a graph to see if the relationship between the amount of males in a district
# correlates linearly with the amount of people on public assistance.
# In this case there seems to be a linear relationship based on the graph.

c.plot(kind= 'scatter', x = 'COUNT RECEIVES PUBLIC ASSISTANCE', y = 'COUNT MALE' )
plt.show()


# Replace spaces in the file header with underscore to feed this into matplotlib for splittting the test/training data.
c.columns = c.columns.str.replace(' ', '_')


# Split out the training data from the testing data. We are using the training data to make predictions about the test data.
X_train, X_test, y_train, y_test = train_test_split(c.COUNT_RECEIVES_PUBLIC_ASSISTANCE, c.COUNT_MALE)

plt.scatter(X_train, y_train, label = 'Training Data', color ='b', alpha = .7)
plt.scatter(X_test, y_test, label = 'Testing Data', color ='r', alpha = .7)
plt.legend()
plt.title("test Train Split")
plt.show()

# Create the linear regression model to feed the train data into the model to make predictions about the test data.

LR = LinearRegression()
train_values = LR.fit(X_train.values.reshape(-1,1), y_train.values)

prediction = LR.predict(X_test.values.reshape(-1, 1))
tests = X_test.values

plt.plot(X_test, prediction, label='Linear Regression', color='g')
plt.scatter(X_test,y_test, label = 'Test Data', color = 'b', alpha = .7)
plt.legend()
plt.show()

scores =  LR.score(X_test.values.reshape(-1, 1), y_test.values)

print("Test prediction for 50 men in a district, Number of people on public assistance: ", LR.predict(np.array([[50]]))[0])
print("Predictiction Accuracy: ", scores)

prediction_list = prediction.tolist()
test_list = tests.tolist()

final_df = pd.DataFrame(data={"NUMBER_OF_MALES_IN_DISTRICT": test_list, "NUMBER_OF_PEOPLE_ON_PUBLIC_ASSISTANCE": prediction_list})

print(final_df)

final_df.to_csv("Predictions.csv", sep=',',index=False)
