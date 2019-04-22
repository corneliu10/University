
# coding: utf-8

# # Laborator 4

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


dataPath = "/Users/bogdan/Downloads/data/"
#load train images
train_images = np.loadtxt(dataPath + "train_images.txt")
train_labels = np.loadtxt(dataPath + "train_labels.txt",'int8')
print(train_images.shape)
print(train_images.ndim)
print(type(train_images[0,0]))
print(train_images.size)
print(train_images.nbytes)


# In[3]:


#plot the first 100 training images with their labels in a 10 x 10 subplot
nbImages = 10
plt.figure(figsize=(5,5))
for i in range(nbImages**2):
    plt.subplot(nbImages,nbImages,i+1)
    plt.axis('off')
    plt.imshow(np.reshape(train_images[i,:],(28,28)),cmap = "gray")
plt.show()
labels_nbImages = train_labels[:nbImages**2]
print(np.reshape(labels_nbImages,(nbImages,nbImages)))


# In[4]:


#load test images
test_images = np.loadtxt(dataPath + "test_images.txt")
test_labels = np.loadtxt(dataPath + "test_labels.txt",'int8')
#plot the first 100 testing images with their labels in a 10 x 10 subplot
nbImages = 10
plt.figure(figsize=(5,5))
for i in range(nbImages**2):
    plt.subplot(nbImages,nbImages,i+1)
    plt.axis('off')
    plt.imshow(np.reshape(test_images[i,:],(28,28)),cmap = "gray")
plt.show()
labels_nbImages = test_labels[:nbImages**2]
print(np.reshape(labels_nbImages,(nbImages,nbImages)))


# In[ ]:


#do 1-NN, 3-NN, 5-NN, 7 -NN for the first test image
#plot the neighbors


# In[ ]:


#define class Knn_classifier

