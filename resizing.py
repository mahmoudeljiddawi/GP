import imutils
import numpy as np
import os
from skimage.io import imsave
from keras.preprocessing.image import img_to_array, load_img

def resize_img(img):
        fixed_size = 256
        if(img.shape[0]>img.shape[1]):
            resized = imutils.resize(img , height=fixed_size)
            iterations = fixed_size - resized.shape[1]
            fill = np.zeros((fixed_size,iterations,3))
            newImage = np.concatenate((fill,resized),1)
            #imsave(path_to_save + filename,newImage/256)
            #print(filename,'height')
        elif(img.shape[0]<img.shape[1]):
            resized = imutils.resize(img, width=fixed_size)
            iterations = fixed_size - resized.shape[0]
            fill = np.zeros((iterations, fixed_size, 3))
            newImage = np.concatenate((resized,fill), 0)
            #imsave(path_to_save + filename,newImage/256)
            #print(filename,'width')
        else:
            resized = imutils.resize(img, width=fixed_size)
            newImage=resized
            #imsave(path_to_save + filename,resized/256)
            #print(filename,'equal')
        return newImage

def enlargement(img , size):
        print(size)
        if size[0]>size[1]:
            resized = imutils.resize(img, height=size[0])
            iterations = size[0] - size[1]
            newImage = resized[: , iterations : , : ]

        elif size[0]<size[1]:
            resized = imutils.resize(img, width=size[1])
            iterations = size[1] - size[0]
            newImage = resized[: iterations , :  , : ]
        else:
            resized = imutils.resize(img, width=size[1])
            newImage=resized
        print(newImage.shape)
        return newImage

