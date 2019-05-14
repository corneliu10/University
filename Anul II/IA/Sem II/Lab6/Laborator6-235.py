
# coding: utf-8

# # Laborator 6

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import csv
import re
from sklearn import preprocessing
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error, mean_absolute_error


# In[2]:


def read_data(file_path):
    data = []
    scores = []

    with open(file_path, mode='r',encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(re.sub("[-.,;:!?\"\'\/()_*=`]", "", row["essay"].lower()).split())
            scores.append(int(row["score"]))
    return data, scores


# In[3]:


dirPath = "/Users/bogdan/Downloads/laborator6/"

train_data, train_scores = read_data(dirPath + "Data/train_data.csv")
test_data, test_scores = read_data(dirPath + "Data/test_data.csv")

print("Train data length: texts: %d, scores: %d" % (len(train_data), len(train_scores)))
print("Test data length: texts: %d, scores: %d" % (len(test_data), len(test_scores)))


# In[4]:


#toy example for KRR
x = np.linspace(0,10,20)
print(x)
y = 2*x + 5*np.random.randn(len(x))

modelKRR = KernelRidge(kernel = "linear",alpha = 0.0001)
modelKRR.fit(x.reshape(-1,1),y.reshape(-1,1))
y_predicted = modelKRR.predict(x.reshape(-1,1))
plt.plot(x,y,'or')
plt.plot(x,y_predicted,'xb')
plt.show()

