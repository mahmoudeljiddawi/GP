import imutils
from skimage import data
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imsave
from keras.preprocessing.image import img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray, gray2rgb

fixed_size = 256
img = load_img('ImageToLoad.jpg')
img = img_to_array(img)
print(img.shape)
maximum = max(img.shape[0],img.shape[1])
if(img.shape[0]>img.shape[1]):
    resized = imutils.resize(img , height=fixed_size)
    iterations = fixed_size - resized.shape[1]
    fill = np.zeros((fixed_size,iterations,3))
    newImage = np.concatenate((fill,resized),1)
    imsave('newImage.jpg',newImage/256)
elif(img.shape[0]<img.shape[1]):
    resized = imutils.resize(img, width=fixed_size)
    iterations = fixed_size - resized.shape[0]
    fill = np.zeros((iterations, fixed_size, 3))
    newImage = np.concatenate((resized,fill), 0)
    imsave('newImage.jpg',newImage/256)
else:
    resized = imutils.resize(img, width=fixed_size)
    imsave('newImage.jpg',resized/256)