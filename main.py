import cv2
import numpy as np

path ='/Users/mac/Desktop/test.jpg'

BGR = cv2.imread(path)
LAB = cv2.cvtColor(BGR , cv2.COLOR_BGR2LAB)
origin = cv2.cvtColor(LAB , cv2.COLOR_LAB2BGR)
cv2.imshow('i' , origin)
cv2.waitKey()
List = []