
# coding: utf-8

# # Rezolvare laborator 3

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


dataPath = "/Users/bogdan/Downloads/data/"
#load train images
train_images = np.loadtxt(dataPath + "train_images.txt")
print(train_images.shape)
print(train_images.ndim)
print(type(train_images[0,0]))
print(train_images.size)
print(train_images.nbytes)


# In[6]:


#plot the first image
image = train_images[0,:]
image = np.reshape(image,(28,28))
plt.imshow(image,cmap = "gray")
plt.show()


# In[7]:


#load training labels
train_labels = np.loadtxt(dataPath + "train_labels.txt",'int8')
print(train_labels.shape)
print(type(train_labels[0]))
print(train_labels.size)
print(train_labels.nbytes)
#show the label of the first training image
print(train_labels[0])


# In[8]:


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


# In[21]:


class NaiveBayes:
    
    def __init__(self,num_bins,max_value=256):
        self.num_bins = num_bins
        self.bins = np.linspace(0,max_value,num_bins+1)
        
    def fit(self,train_images,train_labels):
        #calculez probab p(X_pos = value_interval|C=c) - probabilitatea ca pixelul de pe pozitia pos
        #sa ia o anumita valoare (intr-un interval) tinanc cont ca vine din clasa c
        #stochez totul in matricea M de dimensiuni 10 x 784 x num_bins (numar clase x nr pixeli x numar intervale)
        M = np.zeros((10,785,self.num_bins))
        for c in range(10):
            for pos in range(784):
                indici = np.ravel(np.where(train_labels == c))
                values = train_images[indici,pos]
                h = np.histogram(values,self.bins)
                M[c,pos,:] = h[0]/sum(h[0]) + 1e-10
                
        self.M = M
        
    def predict(self,test_images):
        number_test_images = test_images.shape[0]
        predictedClasses = np.zeros(number_test_images,'int8')
        
        #calculez probabilitatile a-priori p(C=c)
        pC = np.zeros(10,'int8')
        for label in train_labels:
            pC[label] = pC[label] + 1
            
        for idx_test in range(number_test_images):
            log_PC = np.log(pC)
            for c in range(10):
                for pos in range(784):
                    value = test_images[idx_test,pos];
                    bin = np.digitize(value,self.bins)-1
                    log_PC[c] = log_PC[c] + np.log(self.M[c,pos,bin])
            predictedClasses[idx_test] = log_PC.argmax()
        
        return predictedClasses


# In[23]:


test_images = np.loadtxt(dataPath + "test_images.txt")
test_labels = np.loadtxt(dataPath + "test_labels.txt",'int8')
classifier = NaiveBayes(5,256)
classifier.fit(train_images.copy(),train_labels)
predicted_labels = classifier.predict(test_images.copy())
#plot the first 100 test images with their predicted labels in a 10 x 10 subplot
nbImages = 10
plt.figure(figsize=(5,5))
for i in range(nbImages**2):
    plt.subplot(nbImages,nbImages,i+1)
    plt.axis('off')
    plt.imshow(np.reshape(test_images[i,:],(28,28)),cmap = "gray")
plt.show()
labels_nbImages = predicted_labels[:nbImages**2]
print(np.reshape(labels_nbImages,(nbImages,nbImages)))


# In[24]:


def compute_accuracy(true_labels,predicted_labels):
    return (true_labels == predicted_labels).mean()

print("Acuratetea calsificatorului Naive Bayes este: ", compute_accuracy(test_labels,predicted_labels))


# In[28]:


#calculati matricea de confuzie C  de dimensiuni 10 x 10


# In[29]:


#plotati toate imaginile de testare de cifre 4 clasificate drept 9 si invers, imagini de testare de cifre 9 clasificate 4

