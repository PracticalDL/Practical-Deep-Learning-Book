# FAQ

This document is a set of quick questions and generally useful FAQs.

## Installation

### `virtualenv`

1. Install **pip** `sudo apt-get install python3-pip`

2. Install **virtualenv** using pip3 `sudo pip3 install virtualenv`

3. Create the virtual environment `virtualenv -p /usr/bin/python3.6 practicaldl`
  
4. Active the virtual environment `source practicaldl/bin/activate`

5. Install all the requirements `pip install -r requirements.txt`

6. When we want to exit, use the deactivate command `deactivate`

Within the `virtualenv` environment, please install the following:

#### TensorFlow 2.0 Environment

Please follow the [instructions](https://www.tensorflow.org/install) on the website. Keras will also be installed as part of TensorFlow 2.0.

For [Chapter 14 - Building the Purrfect Cat Locator App with TensorFlow Object Detection API](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14), please use the [`protoc.sh`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/protoc.sh) script to install everything needed.

#### Jupyter Notebook

1. Install `jupyter` inside the `virtualenv`.

2. Run using `jupyter notebook`. You can also add `--ip 0.0.0.0 --port 8888 --no-browser` if you want to remotely access the notebooks.

#### Tmux

Use `tmux` to keep sessions ongoing.
