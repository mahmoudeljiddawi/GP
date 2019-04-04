#code part 1
from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import PIL.Image
import urllib
import os

page = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04194289")#ship synset
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')#puts the content of the website into the soup variable, each url on a different line
# BeautifulSoup is an HTML parsing library


#code part 2
str_soup=str(soup)#convert soup to string so it can be split
type(str_soup)
split_urls=str_soup.split('\r\n')#split so each url is a different possition on a list
print(len(split_urls))#print the length of the list so you know how many urls you have


#code part 3
#check if all the images where stored on the files system
os.mkdir() #Ekteb el path gowa

# code part 4
img_rows, img_cols = 256, 256  # number of rows and columns to convert the images to
input_shape = (img_rows, img_cols, 3)  # format to store the images (rows, columns,channels) called channels last


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


n_of_training_images = 100  # the number of training images to use
for progress in range(n_of_training_images):  # store all the images on a directory
    # Print out progress whenever progress is a multiple of 20 so we can follow the
    # (relatively slow) progress
    if (progress % 20 == 0):
        print(progress)
    if not split_urls[progress] == None:
        try:
            I = url_to_image(split_urls[progress])
            if (len(I.shape)) == 3:  # check if the image has width, length and channels
                save_path = '/content/train/ships/img' + str(progress) + '.jpg'  # create a name of each image
                cv2.imwrite(save_path, I)

        except:
            None