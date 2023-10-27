import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
def encryption(img):
    #Generating chaotic keys
    height=img.shape[0]
    width=img.shape[1]
    key=kg.keygen(0.01,3.954,height*width)

    #Encryption by substituting with XOR
    z=0
    enimg= np.zeros(shape=[height,width], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            enimg[i,j]=img[i,j]^key[z]
            z+=1
    plt.imshow(enimg,cmap='gray')
    plt.axis('off')
    plt.show()
    plt.imsave('Images/face.jpg', enimg)
    return enimg