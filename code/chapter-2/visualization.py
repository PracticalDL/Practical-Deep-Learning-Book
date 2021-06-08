import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import get_file

from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tf_explain.core.grad_cam import GradCAM

import PIL
from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.image as mpimg

from argparse import ArgumentParser

import glob
import os

#Select a model to use, in this case VGG16
model = VGG16(weights='imagenet', include_top=True, input_tensor=None, input_shape=None, pooling=None, classes=1000)
#Check with 'print(model.summary())', in this case it is "block5_conv3"
last_conv_layer_name = "block5_conv3"
#Must include layers between last convolutional layer and prediction layer
#Layer names can be found through 'print(model.summary())'
classifier_layer_names = ["block5_pool", "flatten", "fc1", "fc2", "predictions"]

#This function is called from 'make_gradcam_heatmap'
#Takes iaage_path from 'get_command_line_arguments', turns into it an array
def get_img_array(img_path, size):
    img = tensorflow.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    # `array` is a float32 Numpy array
    array = tensorflow.keras.preprocessing.image.img_to_array(img)
    # We add a dimension to transform our array into a "batch"
    # of size (1, 299, 299, 3)
    array = np.expand_dims(array, axis=0)
    return array

#'make_gradcam_heatmap' is main function and ultimately returns heatmap superimposed onto the input image(s)

#inputs are the image path specified in the command line, the last convolutional layer and
#the classifier layer names of which both are defined above and depend on your model, and the output path
#for our heatmap superimposed onto original image which are specified in the script's final if statement
def make_gradcam_heatmap(
    img_path, model, last_conv_layer_name, classifier_layer_names, output_path
):
    #pre_processes the array returned from 'get_img_array'
    img_array = preprocess_input(get_img_array(img_path, size= (224, 224)))

    # First, we create a model that maps the input image to the activations
    # of the last conv layer
    last_conv_layer = model.get_layer(last_conv_layer_name)
    last_conv_layer_model = tensorflow.keras.Model(model.inputs, last_conv_layer.output)

    # Second, we create a model that maps the activations of the last conv
    # layer to the final class predictions
    classifier_input = tensorflow.keras.Input(shape=last_conv_layer.output.shape[1:])
    x = classifier_input
    for layer_name in classifier_layer_names:
        x = model.get_layer(layer_name)(x)
    classifier_model = tensorflow.keras.Model(classifier_input, x)

    # Then, we compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tensorflow.GradientTape() as tape:

        # Compute activations of the last conv layer and make the tape watch it
        last_conv_layer_output = last_conv_layer_model(img_array)
        tape.watch(last_conv_layer_output)

        # Compute class predictions
        preds = classifier_model(last_conv_layer_output)
        top_pred_index = tensorflow.argmax(preds[0])
        top_class_channel = preds[:, top_pred_index]

    # This is the gradient of the top predicted class with regard to
    # the output feature map of the last conv layer
    grads = tape.gradient(top_class_channel, last_conv_layer_output)

    # This is a vector where each entry is the mean intensity of the gradient
    # over a specific feature map channel
    pooled_grads = tensorflow.reduce_mean(grads, axis=(0, 1, 2))

    # We multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    last_conv_layer_output = last_conv_layer_output.numpy()[0]
    pooled_grads = pooled_grads.numpy()
    for i in range(pooled_grads.shape[-1]):
        last_conv_layer_output[:, :, i] *= pooled_grads[i]

    # The channel-wise mean of the resulting feature map
    # is our heatmap of class activation
    heatmap = np.mean(last_conv_layer_output, axis=-1)

    # For visualization purpose, we will also normalize the heatmap between 0 & 1
    heatmap = np.maximum(heatmap, 0) / np.max(heatmap)

    # We load the original image
    img = tensorflow.keras.preprocessing.image.load_img(img_path)
    img = tensorflow.keras.preprocessing.image.img_to_array(img)

    # We rescale heatmap to a range 0-255
    heatmap = np.uint8(255 * heatmap)

    # We use jet colormap to colorize heatmap
    jet = cm.get_cmap("jet")

    # We use RGB values of the colormap
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]

    # We create an image with RGB colorized heatmap
    jet_heatmap = tensorflow.keras.preprocessing.image.array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
    jet_heatmap = tensorflow.keras.preprocessing.image.img_to_array(jet_heatmap)

    # Superimpose the heatmap on original image
    superimposed_img = jet_heatmap * 0.4 + img
    superimposed_img = tensorflow.keras.preprocessing.image.array_to_img(superimposed_img)

    #Save the the superimposed image to the output path
    superimposed_img.save(output_path)

#Runs body of code for entirety of videoframs_path (folder specified in command line)
def process_video(videoframes_path, output_prefix):
    counter = 0
    #define output directory
    output_dir = output_prefix + "_output"

    #Creates directory output directoy if it doesn't already exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for input_path in sorted(glob.glob(videoframes_path + "/*.jpg")):
        counter += 1

        output_path = output_dir + "/result-" + str(counter).zfill(4) + '.jpg'

        #Runs main function with specified image_path, output_prefix, and layers defined near top of script
        make_gradcam_heatmap(input_path, model, last_conv_layer_name, classifier_layer_names, output_path)

#Function for taking inputs through the command line
def get_command_line_arguments():
    parser = ArgumentParser()
    #We specify either image or video to
    parser.add_argument("--process", choices=["image", "video"], required=True,
                        dest="process_type", help="Process a single image or video")
    parser.add_argument("--path", required=True, dest="path",
                        help="Path of image or directory containing video frames")
    return parser.parse_args()


args = get_command_line_arguments()

#If process is specified as 'image', defines image_path and output_prefix according to command line argument
if args.process_type == "image":
    #image path is location of image that we want to generate a heatmap for
    image_path = args.path
    output_prefix = os.path.splitext(os.path.basename(image_path))[0]
    #Runs main function with specified image_path and output_prefix from command line
    #layers defined near top of script
    make_gradcam_heatmap(image_path, model, last_conv_layer_name, classifier_layer_names, output_prefix + "_output.jpg")

    #Plot the superimposed image
    img = mpimg.imread(output_prefix + "_output.jpg")
    plt.imshow(img)
    plt.show()

#If process is specified as 'image', defines videoframes_path and output_prefix according to command line argument
elif args.process_type == "video":
    #videoframes_path is directory with the video frames split by ffmpeg
    videoframes_path = args.path
    #will be used to specify or create output folder
    output_prefix = os.path.dirname(videoframes_path)
    #Runs 'process_video' function with inputs taken from command line
    heatmaps = process_video(videoframes_path, output_prefix)
