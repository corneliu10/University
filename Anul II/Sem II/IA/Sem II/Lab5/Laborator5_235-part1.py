
# coding: utf-8

# # Laborator 5

# # Linear SVM

# In[2]:


import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np 

#training points and labels
train_points = np.array([[1,3],[3,1],[2,-2],[4,4],[5,6]])
train_labels = np.array([-1,-1,-1,1,1])

#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')
plt.show()


# In[3]:


#define the svm classifier
C = 1;
svm_classifier = svm.SVC(C,"linear")

#train the model
svm_classifier.fit(train_points,train_labels)

#plot the decision boundary = a hyperplane in R^2 = a line given by ax + by + c = 0
#take the coefficients a,b,c from the model
a = svm_classifier.coef_[0,0]
b = svm_classifier.coef_[0,1]
c = svm_classifier.intercept_[0]
#build the line ax + by + c = 0
x = np.linspace(0,5,100)
y = -a/b*x -c/b

#plot the points and the decision boundary
#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')
#plot the decision boundary
plt.title("Linear Kernel, C = 1")
plt.plot(x,y,"k")


# In[4]:


get_ipython().run_line_magic('pinfo', 'svm_classifier')
print(svm_classifier.support_)
print(svm_classifier.support_vectors_)
print(svm_classifier.coef_)
print(svm_classifier.intercept_)


# In[5]:


#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')

# plot the decision boundary and the margins
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm_classifier.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
ax.scatter(svm_classifier.support_vectors_[:, 0], svm_classifier.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
plt.title("Linear kernel, C = 1")
plt.show()


# In[6]:


#add the point [2,2.1] with label 1 to the initial training set and see what happens to the margin when you vary C

#training points and labels
train_points = np.array([[1,3],[3,1],[2,-2],[4,4],[5,6],[2,2.1]])
train_labels = np.array([-1,-1,-1,1,1,1])

#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')

#take a small C
C = 1;
svm_classifier = svm.SVC(C,"linear")

#train the model
svm_classifier.fit(train_points,train_labels)

# plot the decision boundary and the margins
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm_classifier.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
ax.scatter(svm_classifier.support_vectors_[:, 0], svm_classifier.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
plt.title("Linear kernel, C = 1")
plt.show()


#take a large C
C = 1000;
svm_classifier = svm.SVC(C,"linear")

#train the model
svm_classifier.fit(train_points,train_labels)

#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')

# plot the decision boundary and the margins
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm_classifier.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
ax.scatter(svm_classifier.support_vectors_[:, 0], svm_classifier.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
plt.title("Linear kernel, C = 1000")
plt.show()


# # Linear vs RBF kernel

# In[8]:


#add the point [0,0] with label 1 to the initial training set and see if you can classify the points. Try the RBF kernel
#training points and labels
train_points = np.array([[1,3],[3,1],[2,-2],[4,4],[5,6],[0,0]])
train_labels = np.array([-1,-1,-1,1,1,1])

#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')


#take a large C
C = 1000;
svm_classifier = svm.SVC(C,"linear")

#train the model
svm_classifier.fit(train_points,train_labels)

#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')

# plot the decision boundary and the margins
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm_classifier.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
ax.scatter(svm_classifier.support_vectors_[:, 0], svm_classifier.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
plt.title("Linear kernel, C = 1000")
plt.show()


#try a RBF kernel
C = 1;
svm_classifier = svm.SVC(C,"rbf")

#train the model
svm_classifier.fit(train_points,train_labels)

#plot the points
pos_train_labels = train_labels == 1
neg_train_labels = train_labels == -1
plt.plot(train_points[pos_train_labels,0],train_points[pos_train_labels,1],'og')
plt.plot(train_points[neg_train_labels,0],train_points[neg_train_labels,1],'xr')

# plot the decision boundary and the margins
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm_classifier.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
ax.scatter(svm_classifier.support_vectors_[:, 0], svm_classifier.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
plt.title("RBF kernel, C = 1")
plt.show()


# # Normalizarea datelor

# ## Standardizarea datelor

# In[9]:


from sklearn import preprocessing
import numpy as np

x_train = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]], dtype=np.float64)
x_test = np.array([[-1, 1, 0]], dtype=np.float64)

scaler = preprocessing.StandardScaler()
scaler.fit(x_train)


# In[10]:


# afisam media
print("Vectorul medie calculat pe baza mediilor pe fiecare componenta este ", scaler.mean_) # => [1. 0. 0.33333333]
print(np.mean(x_train,axis = 0))
print(np.mean(x_train,axis = 1))
print(np.mean(x_train))


# In[11]:


# afisam deviatia standard
print("Vectorul cu deviatiile standard calculat pe fiecare componenta este ", scaler.scale_) # => [0.81649658 0.81649658 1.24721913]
print(np.std(x_train[:,0]))
print(np.std(x_train[:,1]))
print(np.std(x_train[:,2]))
print(np.std(x_train,axis=0))


# In[12]:


# scalam datele de antrenare
scaled_x_train = scaler.transform(x_train)
print("Datele de antrenare scalate sunt:\n", scaled_x_train) # => [[0. -1.22474487 1.33630621]
                      #     [1.22474487 0. -0.26726124]
                      #     [-1.22474487 1.22474487 -1.06904497]]
print(np.mean(scaled_x_train,axis=0))
print(np.std(scaled_x_train,axis=0))
# scalam datele de test
scaled_x_test = scaler.transform(x_test)
print("Datele de testare scalate sunt:\n",scaled_x_test) # => [[-2.44948974 1.22474487 -0.26726124]]


# ## Scalare in 0-1

# In[13]:


x_train = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]], dtype=np.float64)
x_test = np.array([[-1, 1, 0]], dtype=np.float64)


min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)) # (0, 1) default
min_max_scaler.fit(x_train)


# In[14]:


# scalam datele de antrenare
scaled_x_train = min_max_scaler.transform(x_train)
print(scaled_x_train)        # => [[0.5  0.    1.        ]
                             #     [1.   0.5   0.33333333]
                             #     [0.   1.    0.        ]]


# In[15]:


# scalam datele de test
scaled_x_test = min_max_scaler.transform(x_test)
print(scaled_x_test)         # => [[-0.5  1.  0.33333333]]


# ## Normalizarea L1, L2

# In[16]:


x_train = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]], dtype=np.float64)
x_test = np.array([[-1, 1, 0]], dtype=np.float64)


# In[17]:


#l2 - norm
x_train_norm_l2 = preprocessing.normalize(x_train,norm="l2",axis=1)
print(x_train_norm_l2)
print((x_train_norm_l2**2).sum(axis=1))
x_test_norm_l2 = preprocessing.normalize(x_test,norm="l2",axis=1)
print(x_test_norm_l2)


# In[18]:


#l1 - norm
x_train_norm_l1 = preprocessing.normalize(x_train,norm="l1",axis=1)
print(x_train_norm_l1)
print(abs(x_train_norm_l1).sum(axis=1))
x_test_norm_l1 = preprocessing.normalize(x_test,norm="l1",axis=1)
print(x_test_norm_l1)


# In[23]:


dataPath = "/Users/bogdan/Downloads/data/"
#load train images
train_images = np.loadtxt(dataPath + "train_images.txt")
train_labels = np.loadtxt(dataPath + "train_labels.txt",'int8')
test_images = np.loadtxt(dataPath + "test_images.txt")
test_labels = np.loadtxt(dataPath + "test_labels.txt",'int8')

print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)

