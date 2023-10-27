import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Reading the image

img = mpimg.imread('Images/face.jpg')

plt.imshow(img)
plt.show()

#Generating chaotic keys
height=img.shape[0]
width=img.shape[1]
key=kg.keygen(0.01,3.95,height*width)
print(key)

#Encryption by substituting with XOR
z=0
enimg= np.zeros(shape=[height,width,4], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        enimg[i,j]=img[i,j]^key[z]
        z+=1
plt.imshow(enimg)
plt.show()
plt.imsave('Images/face.jpg', enimg)

#Decrypting the image
z=0
decimg=np.zeros(shape=[height,width,4], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        decimg[i,j]=enimg[i,j]^key[z]
        z+=1
plt.imshow(decimg)
plt.imsave('Images/face.jpg', decimg)

