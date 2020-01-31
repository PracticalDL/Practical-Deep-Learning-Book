import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import get_file
import json

from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tf_explain.core.grad_cam import GradCAM

import PIL
from PIL import Image, ImageDraw, ImageFont

import matplotlib.cm as cm

from argparse import ArgumentParser

import glob
import os

CLASS_INDEX = None
CLASS_INDEX_PATH = '../imagenet_class_index.json'

model = VGG16(weights='imagenet', include_top=True, input_tensor=None, input_shape=None, pooling=None, classes=1000)

# Note: decode_predictions(preds, top) is originally a keras function.
# We have modified it here so that it returns the index of the class label along with the predictions.
# The results are assimilated based on the assumption that there is only one top 1% prediction.

def decode_predictions_modified(preds, top=1):
    global CLASS_INDEX
    if len(preds.shape) != 2 or preds.shape[1] != 1000:
        raise ValueError(
            '`decode_predictions` expects ' 'a batch of predictions ''(i.e. a 2D array of shape (samples, 1000)). ' 'Found array with shape: ' + str(preds.shape))
    if CLASS_INDEX is None:
        fpath = get_file('imagenet_class_index.json',
                         CLASS_INDEX_PATH, cache_subdir='models')
        CLASS_INDEX = json.load(open(fpath))
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        for i in top_indices:
            results = [i, tuple(CLASS_INDEX[str(i)]), (pred[i],)]
    return results

# Function that takes an image and model and produces the predictions

def get_predictions(img, model):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return decode_predictions_modified(preds, top=1)

# NOTE: These two functions are taken from Shao-Chuan Wang <shaochuan.wang AT gmail.com> 
# as per the copyright on http://code.activestate.com/recipes/577591-conversion-of-pil-image-and-numpy-array/

"""
   Copyright 2011 Shao-Chuan Wang <shaochuan.wang AT gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""
# Modified from the original format to take only the array as input and calculate the size on the fly
def array_to_PIL(arr):
    mode = 'RGBA'
    # Use only the height and width for further processing
    size = (arr.shape[0], arr.shape[1])  # (224,224)
    arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
    if len(arr[0]) == 3:
        arr = np.c_[arr, 255*np.ones((len(arr), 1), np.uint8)]
    return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)

# Function that puts text based prediction and class name on top of the image
def overlay_prediction_on_image(img, prediction_class, prediction_probability, width, height):
    img = img.resize((width, height), Image.ANTIALIAS)
    draw = ImageDraw.Draw(img)
    l = len(prediction_class)
    # Place a black rectangle to provide a background for the text
    # The size of the rectangle should change with respect to the image
    draw.rectangle([int(width*0.05), int(width*0.05),
                    int(width*0.5), int(width*0.11)], fill=(0, 0, 0))
    draw.text((int(width*0.06), int(width*0.06)), '{0:.0f}'.format(
        prediction_probability) + "% " + prediction_class, fill=(255, 255, 255))
    return img

# Based on StackOverflow code by user DTing
# https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python


def join_images(img1, img2):
    widths, heights = zip(*(i.size for i in [img1, img2]))
    total_width = sum(widths)
    max_height = max(heights)
    new_img = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for img in [img1, img2]:
        new_img.paste(img, (x_offset, 0))
        x_offset += img.size[0]
    return new_img


def process_image(image_path, output_path):
    explainer = GradCAM()

    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    data = ([img], None)

    original_image = Image.open(image_path)
    width = int(original_image.size[0]/4)
    height = int(original_image.size[1]/4)
    original_image.thumbnail((width, height), Image.ANTIALIAS)

    class_index, class_name, prob_value = get_predictions(img, model)
    heatmap = explainer.explain(data, model, "block5_conv3", class_index)

    # overlay the text prediction on the heatmap overlay
    heatmap_with_prediction_overlayed = overlay_prediction_on_image(
        array_to_PIL(heatmap), class_name[-1], prob_value[0] * 100, width, height)

    # place the images side by side
    joined_image = join_images(
        original_image, heatmap_with_prediction_overlayed)
    joined_image.save(output_path)

def process_video(videoframes_path, output_prefix):
    counter = 0
    output_dir = output_prefix + "_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for input_path in sorted(glob.glob(videoframes_path + "/*.jpg")):
        counter += 1
        output_path = output_dir + "/result_" + str(counter).zfill(4) + '.jpg'
        process_image(input_path, output_path)


def get_command_line_arguments():
    parser = ArgumentParser()
    parser.add_argument("--process", choices=["image", "video"], required=True,
                        dest="process_type", help="Process a single image or video")
    parser.add_argument("--path", required=True, dest="path",
                        help="Path of image or directory containing video frames")
    return parser.parse_args()


args = get_command_line_arguments()

if args.process_type == "image":
    image_path = args.path
    output_prefix = os.path.splitext(os.path.basename(image_path))[0]
    process_image(image_path, output_prefix + "_output.jpg")
elif args.process_type == "video":
    videoframes_path = args.path
    output_prefix = os.path.dirname(videoframes_path)
    process_video(videoframes_path, output_prefix)
