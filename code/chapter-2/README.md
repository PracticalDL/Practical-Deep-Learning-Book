# Code for Chapter 2: What’s in the Picture: Image Classification with Keras

We delve into the world of image classification in a mere five lines of Keras code. We then learn what neural networks are paying attention to while making predictions by overlaying heatmaps on videos. [Read online here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch02.html)

We also hear the motivating personal journey of **François Chollet**, the creator of Keras, illustrating the impact a single individual can have.

## Setup

Run the following commands prior to running the scripts in this directory:

`$ pip install tensorflow==2.0.0`

`$ pip install keras -U`

`$ pip install numpy -U`

`$ pip install matplotlib -U`

`$ pip install tf-explain==0.1.0`

`$ pip install pillow -U`

`$ pip install pathlib -U`

## Code

The following Jupyter Notebooks are provided. Please go through the code in the given order:

1. [1-predict-class.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/1-predict-class.ipynb): We examine the image classification task, to answer the question “Does the image contain X” where X can be a cat, dog or any other category/class of objects.
2. [2-what-does-my-neural-network-think.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/2-what-does-my-neural-network-think.ipynb): We try to understand why the neural network made a particular prediction. We use visualization (a heatmap) to understand the decision-making that is going on within the network. Using color, we visually identify the areas within an image that prompted a decision. “Hot” spots, represented by warmer colors (red, orange, and yellow) highlight the areas with the maximum signal, whereas cooler colors (blue, purple) indicate low signal. (To run on Colab, use [2-colab-what-does-my-neural-network-think.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/2-colab-what-does-my-neural-network-think.ipynb)) instead. For the Colab version you will be prompted to restart the runtime and rerun the code after `TensorFlow 2.0.0` is installed through `pip install tensorflow==2.0.0`.)

### Scripts

[visualization.py](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/visualization.py) is a script that does most of the processing, and is being called by [2-what-does-my-neural-network-think.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/2-what-does-my-neural-network-think.ipynb). The script produces the heatmap for one or more input images, overlays it on the image, and stitches it side-by-side with the original image for comparison. Please download the [`imagenet_class_index.json`](https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json) and update the path in the [`visualization.py`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/visualization.py#L24) (line 24) file. The `imagenet_class_index.json` file provides a mapping from the ImageNet class ids to the string classnames. The script accepts arguments for image path or a directory that contains frames of a video (see below).

## Data

You will be collecting data using a camera phone. Make a video of any common food items you encounter in the kitchen such as in the [sample video we provided](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/kitchen-input.mov). Follow the instructions in [2-what-does-my-neural-network-think.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/2-what-does-my-neural-network-think.ipynb) to run the [visualization.py](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/visualization.py) script on the video. The script is using `ffmpeg` to parse the video. Please install it using the [instructions](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg) on their website.

Don't forget to post your heatmap videos on Twitter with the hashtag [#PracticalDL](https://twitter.com/hashtag/PracticalDL)!

We have also provided the following sample inputs and the expected outputs.

- Input video: [kitchen-input.mov](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/kitchen-input.mov)
- Output video: [kitchen-output.mov](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/kitchen-output.mp4)
- Input frames of video: [kitchen](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/kitchen)
- Output frames of video: [kitchen-output](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/kitchen-output)
- Output of sample cat image: [cat-output.jpg](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/cat-output.jpg)
- Output of sample dog image: [dog-output.jpg](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-2/data/dog-output.jpg)
