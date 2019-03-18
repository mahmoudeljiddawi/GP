import imutils
import numpy as np
import os
from skimage.io import imsave
from keras.preprocessing.image import img_to_array, load_img

path_to_load = '/Users/mac/Desktop/Downloaded/'
path_to_save = '/Users/mac/Desktop/newDataset/'
dir = os.listdir(path_to_load)
fixed_size = 256

for filename in dir:
    if filename[0]!='.':
        img = load_img(path_to_load + filename)
        img = img_to_array(img)
        if(img.shape[0]>img.shape[1]):
            resized = imutils.resize(img , height=fixed_size)
            iterations = fixed_size - resized.shape[1]
            fill = np.zeros((fixed_size,iterations,3))
            newImage = np.concatenate((fill,resized),1)
            imsave(path_to_save + filename,newImage/256)
            print(filename,'height')
        elif(img.shape[0]<img.shape[1]):
            resized = imutils.resize(img, width=fixed_size)
            iterations = fixed_size - resized.shape[0]
            fill = np.zeros((iterations, fixed_size, 3))
            newImage = np.concatenate((resized,fill), 0)
            imsave(path_to_save + filename,newImage/256)
            print(filename,'width')
        else:
            resized = imutils.resize(img, width=fixed_size)
            imsave(path_to_save + filename,resized/256)
            print(filename,'equal')
