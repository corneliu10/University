import numpy as np
import matplotlib.pyplot as plt
import scipy
import skimage

# introduction to np
a = np.array([1, 2, 3])
print(a)
print(a.shape)

b = np.reshape(a, (3, 1))
print(b)
print(b.T)
print(a + b.T)

c = np.arange(0, 9)
print(c)

c = np.reshape(c, (3, 3))
print(c)

print(c[1:3, 1:3])
print(c[1, :])

g = np.zeros((4, 4))
print(g)

h = np.ravel(c)
print(h)

a = np.dot(a, 5)
print(a)

a = np.array([[[1, 2, 3],[4, 5, 6]], 
              [[1, 2, 3],[4, 5, 6]],
              [[1, 2, 3],[4, 5, 6]]])
m1 = np.mean(a, axis=(0, 1, 2))
print(m1)

# Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([7, 8, 9])
b = 5

print(a + b)
print(a + c)

# Matplotlib
def plot1():
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.plot(x)
    plt.show()

def plot2():
    x = np.arange(0, 3 * np.pi, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(y1, y2, '1')
    plt.plot(x)
    plt.show()

def plot3():
    plt.subplot(2, 2, 1)
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

    plt.subplot(2, 2, 2)
    plt.plot(x)
    plt.show()

# plot3()

# Ex
import os
from skimage import io

FilePath = ".\\Data\\images"

# a
img_array = []
for img_name in os.listdir(FilePath):
    image = np.load(os.path.join(FilePath, img_name))
    #io.imshow(image)
    #io.show()
    img_array.append(image)

img_array = np.array(img_array)

# b 
print(np.sum(img_array))

# c
sum_list = np.sum(img_array, axis=(1, 2))
print(sum_list)

# d
print(np.argmax(sum_list))

# e
img_medie = np.mean(img_array , axis = 0)
#io.imshow(img_medie.astype(np.uint8))
#io.show()

# f
img_std = np.std(img_array, axis=0)
#io.imshow(img_std.astype(np.uint8))
#io.show()

# g
for img in img_array:
    image = (img - img_medie) / img_std
    #io.imshow(image.astype(np.uint8))
    #io.show()

# img_norm = (img_array - img_medie) / img_std

# h

for img in img_array: 
    pass
    #io.imshow(img[200:300, 280:400].astype(np.uint8))
    #io.show()