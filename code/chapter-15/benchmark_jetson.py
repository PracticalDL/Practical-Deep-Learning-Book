# Sam Sterckval
# 2019 Edgise
import numpy as np
import tensorflow as tf
from tensorflow import lite
import tensorflow.keras as keras # use this line for tensorflow 2.X
# import keras # use this line for tensorflow 1.X
# from keras.models import load_model # tf1.X
from tensorflow.keras.models import load_model  # tensorflow 2.X
# from keras.applications.mobilenetv2 import preprocess_input, decode_predictions
from tensorflow.keras.mobilenet_v2 import preprocess_input, decode_predictions
import os
import PIL
import time
from tftrt_helper import FrozenGraph, TfEngine, TftrtEngine
execution_path = os.getcwd()

model_input_path = os.path.join(execution_path, 'MobileNetV2_ImageNet.h5')
#model_output_path = os.path.join(execution_path, 'MobileNetV2_ImageNet.tflite')
input_image_path = os.path.join(execution_path, 'images/cat.jpg')

# Lets optimize the model for the Jetson's GPU
input_model = load_model(model_input_path)
frozenmodel = FrozenGraph(input_model, (224, 224, 3))
print('FrozenGraph build.')
model = TftrtEngine(frozenmodel, 1, 'FP16', output_shape=(1000))
print('TF-TRT model ready to rumble!')

# Load and preprocess the image
# If you are going to resize images on-the-fly, use OpenCV instead of PIL
input_image = PIL.Image.open(input_image_path)
input_image = np.asarray(input_image)
preprocessed = preprocess_input(input_image)
preprocessed = np.expand_dims(preprocessed, axis=0)
print('input tensor shape : ' + str(preprocessed.shape))

# This actually calls the inference
# A warmup prediction here should not be needed, but let's do it anyway
print("Warmup prediction")
output = model.infer(preprocessed)
print(decode_predictions(output))
time.sleep(1)

print("starting now (Jetson Nano)...")
s = time.time()
for i in range(0,250,1):
    output = model.infer(preprocessed)
e = time.time()
print('Time[ms] : ' + str(e-s))
print('FPS      : ' + str(1.0/((e-s)/250.0)))
