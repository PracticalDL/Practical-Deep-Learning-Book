# Sam Sterckval
# 2019 Edgise
from edgetpu.classification.engine import ClassificationEngine
from PIL import Image
import time

# Function to read labels from text files.
def ReadLabelFile(file_path):
  with open(file_path, 'r') as f:
    lines = f.readlines()
  ret = {}
  for line in lines:
    pair = line.strip().split(maxsplit=1)
    ret[int(pair[0])] = pair[1].strip()
  return ret

# Prepare labels
labels = ReadLabelFile("models/imagenet_labels.txt")
# Initialize engine
engine = ClassificationEngine("models/mobilenet_v2_1.0_224_quant_edgetpu.tflite")
# Load image
img = Image.open("images/cat.jpg")

# Run once, make sure class is right
# the first time we classify the model is send to the edgeTPU,
# that is why this first prediction is so much slower then the rest
print("warmup prediction")
prediction = engine.ClassifyWithImage(img, top_k=1)
prediction = prediction[0]
print(labels[prediction[0]])
print(prediction[1])
time.sleep(1)

print("starting now (Edge TPU)...")
s = time.time()
for i in range(0,250,1):
  result = engine.ClassifyWithImage(img, top_k=1)
  result = result[0]

e = time.time()
print('Time[ms] : ' + str(e-s))
print('FPS      : ' + str(1.0/((e-s)/250.0)))
