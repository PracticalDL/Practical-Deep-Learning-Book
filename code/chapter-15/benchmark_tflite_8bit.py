# Sam Sterckval
# 2019 Edgise
import numpy as np
import tensorflow as tf
from tensorflow import lite
# import keras
# from keras.applications.mobilenetv2 import decode_predictions
# for tensorflow 2.X, use the lines below.
import tensorflow.keras as keras
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
import os
import PIL
import time
execution_path = os.getcwd()

model_input_path = os.path.join(execution_path, 'models/mobilenet_v2_1.0_224_quant.tflite')
input_image_path = os.path.join(execution_path, 'images/cat.jpg')

# Load and preprocess the image
input_image = PIL.Image.open(input_image_path)
input_image = np.asarray(input_image)
# we will not preprocess the image here, because
# MobileNet's preprocessing scales down to a range [-1.0, 1.0],
# while the model now expects [0, 255]
# this does, however, seem to make the cat a cougar instead...
preprocessed = input_image
preprocessed = np.expand_dims(preprocessed, axis=0)
preprocessed = preprocessed.astype(np.uint8)
print('input tensor shape : ' + str(preprocessed.shape))

# Load TFLite model and allocate tensors
interpreter = lite.Interpreter(model_path=model_input_path)
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model once
input_shape = input_details[0]['shape']
print(input_shape)
interpreter.set_tensor(input_details[0]['index'], preprocessed)

# This actually calls the inference
interpreter.invoke()

# The function 'get_tensor' returns a copy(!) of the output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])
print(decode_predictions(output_data[:,:1000], top=1))

time.sleep(1)

# uses only 1 cpu, very slow on x86_64
# using this with the Coral package is a lot more efficient, even on cpu
print("starting now (tflite)...")
s = time.time()
for i in range(0,250,1):
    interpreter.set_tensor(input_details[0]['index'], preprocessed)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])
e = time.time()
print('elapsed : ' + str(e-s))
