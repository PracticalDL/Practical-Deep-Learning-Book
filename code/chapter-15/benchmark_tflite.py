# Sam Sterckval
# 2019 Edgise
import numpy as np
import tensorflow as tf
from tensorflow import lite
# import keras
# from keras.applications.mobilenetv2 import preprocess_input, decode_predictions
# for tensorflow 2.X, use lines below
import tensorflow.keras as keras
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import os
import PIL
import time
execution_path = os.getcwd()

model_input_path = os.path.join(execution_path, 'MobileNetV2_ImageNet.h5')
model_output_path = os.path.join(execution_path, 'MobileNetV2_ImageNet.tflite')
input_image_path = os.path.join(execution_path, 'images/cat.jpg')

# Load and preprocess the image
input_image = PIL.Image.open(input_image_path)
input_image = np.asarray(input_image)
preprocessed = preprocess_input(input_image)
preprocessed = np.expand_dims(preprocessed, axis=0)
print('input tensor shape : ' + str(preprocessed.shape))

# Convert to tflite from a keras model
model = load_model(model_input_path)
converter = lite.TFLiteConverter.from_keras_model(model)
tfmodel = converter.convert()
open (model_output_path , "wb") .write(tfmodel)

print("conversion to tflite is done")

# Load TFLite model and allocate tensors
interpreter = lite.Interpreter(model_path=model_output_path)
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model once
input_shape = input_details[0]['shape']
input_data = preprocessed
interpreter.set_tensor(input_details[0]['index'], preprocessed)

# This actually calls the inference
interpreter.invoke()

# The function 'get_tensor' returns a copy(!) of the output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])
print(decode_predictions(output_data, top=1))

time.sleep(1)

# keep in mind that tflite is build for inferencing on ARM cpu's, not x86_64
print("starting now (tflite)...")
s = time.time()
for i in range(0,250,1):
    interpreter.set_tensor(input_details[0]['index'], preprocessed)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])
e = time.time()
print('Time[ms] : ' + str(e-s))
print('FPS      : ' + str(1.0/((e-s)/250.0)))
