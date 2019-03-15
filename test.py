from skimage.color import rgb2lab, lab2rgb, rgb2gray, gray2rgb
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from skimage.transform import resize
from skimage.io import imsave
from keras.applications.inception_resnet_v2 import preprocess_input
from keras.models import load_model
import numpy as np
import os
import tensorflow as tf
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from sklearn.metrics import mean_squared_error

inception = InceptionResNetV2(weights=None, include_top=True)
inception.load_weights('inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5')
inception.graph = tf.get_default_graph()

print('done')
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def create_inception_embedding(grayscaled_rgb):
    grayscaled_rgb_resized = []
    for i in grayscaled_rgb:
        i = resize(i, (299, 299, 3), mode='constant')
        grayscaled_rgb_resized.append(i)
    grayscaled_rgb_resized = np.array(grayscaled_rgb_resized)
    grayscaled_rgb_resized = preprocess_input(grayscaled_rgb_resized)
    with inception.graph.as_default():
        embed = inception.predict(grayscaled_rgb_resized)
    return embed

color_me = []

photos = os.listdir('photo')

Y = []

for photo in photos:
    if(photo[0]!='.'):
        print(photo)
        ph = load_img('photo/'+photo)
        ph = img_to_array(ph)
        ph = resize(ph, (256, 256, 3), mode='constant')

        Y.append(ph)
        color_me.append(ph)

color_me = np.array(color_me, dtype=float)
gray_me = gray2rgb(rgb2gray(1.0/255*color_me))
color_me_embed = create_inception_embedding(gray_me)
color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]
color_me = color_me.reshape(color_me.shape+(1,))

model = load_model('10imgmodel.h5')
output = model.predict([color_me, color_me_embed])
output = output * 128

MSE = []
for i in range(len(output)):
    cur = np.zeros((256, 256, 3))
    cur[:,:,0] = color_me[i][:,:,0]
    cur[:,:,1:] = output[i]
    Y_hat = lab2rgb(cur)
    MSE.append(mse(Y[i], Y_hat))
    imsave("result"+str(i)+".png", Y_hat)


print(MSE)
