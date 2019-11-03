# Sam Sterckval
# 2019 Edgise
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tensorflow as tf
import keras
from keras.applications.mobilenetv2 import MobileNetV2, preprocess_input, decode_predictions
import os
#import cv2
import PIL
import time
execution_path = os.getcwd()
print("tf version : " + tf.__version__)
print("keras version : " + keras.__version__)


# In[2]:

# load in the neural network
net = MobileNetV2(weights = 'imagenet', include_top = True)


# In[3]:


input_image_path = os.path.join(execution_path, 'images/cat.jpg')
print("input image read from : " + str(input_image_path))


# In[4]:

# Installing OpenCV on raspberry pi can be a burden, so let's switch to PIL
# However, if OpenCV is installed, it does tend to be a little faster
#input_image = cv2.imread(input_image_path)
#input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
input_image = PIL.Image.open(input_image_path)
input_image = np.asarray(input_image)


# In[11]:

# Use the MobileNet preprocessing function,
# and expand dimensions to create a batch of 1 image
preprocessed = preprocess_input(input_image)
preprocessed = np.expand_dims(preprocessed, axis=0)
print('input tensor shape : ' + str(preprocessed.shape))


# In[12]:

# Do 1 warmup prediction, this way we make sure everything is loaded as it should
print("warmup prediction")
prediction = net.predict(preprocessed)
print(decode_predictions(prediction, top=1)[0])
time.sleep(1)


# In[13]:

print("starting now...")
s = time.time()
for i in range(0,250,1):
    prediction = net.predict(preprocessed)

e = time.time()
print('Time[ms] : ' + str(e-s))
print('FPS      : ' + str(1.0/((e-s)/250.0)))


# In[ ]:

# Save the model to an h5 file
net.save('MobileNetV2_ImageNet.h5')
print("Model saved.")




