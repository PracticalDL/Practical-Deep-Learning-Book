# Code for Chapter 9: Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow

We take our custom trained model to the cloud/on-premises to scalably serve from tens to millions of requests. We explore Flask, Google Cloud ML Engine, TensorFlow Serving, and KubeFlow, showcasing the effort, scenario, and cost-benefit analysis. [Continue reading online.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch09.html)

## Code

Go through the code in the following order:

1. [hello.py](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-9/hello.py): Get a Flask server up and running. We will need to install Flask using `pip install flask`.
2. [infer.py](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-9/infer.py): Run a simple web application using Flask to serve image classification requests with a Keras model.
3. [h5_to_pb.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-9/h5_to_pb.ipynb): Convert a pretrained Keras model to a format that is compatible with Google Cloud ML Engine and TensorFlow serving.
4. [image-to-json.py](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-9/image-to-json.py): This will produce the `request.json` which is the image format accepted by Google Cloud ML Engine  and TensorFlow serving. A sample [`request.json`](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-9/request.json) is also provided of the provided sample [dog](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/sample-images/dog.jpg) image is also provided.

Please update the path of the `h5` model in `ADD_H5_MODEL_PATH`, and the desired location and model name in `ADD_PATH_OF_PB_MODEL`.

## Data

Use the [sample images](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/sample-images) and models from previous chapters.

If not already present on our machines, we can download and install the Google Cloud SDK from the installation website here: https://cloud.google.com/sdk/install.