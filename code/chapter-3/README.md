# Code for Chapter 3: Cats versus Dogs: Transfer Learning in 30 Lines with Keras

We use transfer learning to reuse a previously trained network on a new custom classification task to get near state-of-the-art accuracy in a matter of minutes. We then slice and dice the results to understand how well is it classifying. Along the way, we build a common machine learning pipeline, which is repurposed throughout the book.

On the note of transfer learning, we hear from **Jeremy Howard**, co-founder of fast.ai on how hundreds of thousands of students use transfer learning to jumpstart their AI journey.

Read the chapter online [here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch03.html)

## Code

Go through the code in the following order:

1. [1-building-a -custom-classifier-in-keras-with-transfer-learning.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-3/1-keras-custom-classifier-with-transfer-learning.ipynb): We will build a custom classifier in Keras in 30 lines!
2. [2-analyzing-the-results.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-3/2-analyzing-the-results.ipynb): With our trained model, we can analyze how it's performing over the validation dataset. Beyond the simpler accuracy metrics, looking at the actual images of mispredictions should give an intuition on whether the example was truly hard or if our model is not sophisticated enough.

## Data

The `Cats and Dogs` dataset from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/download/train.zip) can be downloaded from the notebook using the kaggle CLI. 

## Further Reading

Even if you are a first-time learner of deep learning or a hobbiyst, you can develop foundational knowledge through these resources that allow one to play with different training scenarios in the browser without the need to install any packages! It covers not only the theory but also helps to build the intuition to solve future problems. 

Take a look at the table below outlining a few video series, online books, and browser-based tools that will help further your understanding of the subject matter. 

| Name | What is it?  | YouTube/Blog  | 
|---|---|---|
| [Teachable Machine](https://end-to-end-machine-learning.teachable.com/p/how-deep-neural-networks-work) by [Brandon Rohrer](https://www.linkedin.com/in/brohrer/) | Series of lectures describing how CNNs, RNNs and LSTMs work.  | You can either register free-of-cost on the website, or view on [YouTube](https://www.youtube.com/watch?v=ILsA4nyG7I0&list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp)  | 
| [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) by [Michael Nielsen](http://michaelnielsen.org/)  | A free online book on Neural networks that is grounded in principles of deep learning.  |   |
| [TensorFlow Playground](https://playground.tensorflow.org/) by Google's Daniel Smilkov and Shan Carter  | An interactive browser-based tool that allows one to tinker with a neural network in the browser.  | [Blog](https://cloud.google.com/blog/products/gcp/understanding-neural-networks-with-tensorflow-playground)  |
| [ConvNet PlayGround](https://convnetplayground.fastforwardlabs.com/#/) By Cloudera's Fast Forward Labs  |  An interactive browser-based tool that does semantic image search using convolutional neural networks | [Blog](https://towardsdatascience.com/convnetplayground-979d441ebf82)  |
| [ConvNetJS](https://cs.stanford.edu/people/karpathy/convnetjs/) by Andrej Karpathy  | A Javascript library for training models in the browser. "Open a tab and you're training. No software requirements, no compilers, no installations, no GPUs, no sweat."  | [Introduction](https://cs.stanford.edu/people/karpathy/convnetjs/started.html)  |
| [CNN Explainer](https://poloclub.github.io/cnn-explainer/)  |  Visualize each convolution and filter as they pass through each image. | [YouTube](https://www.youtube.com/watch?v=HnWIHWFbuUQ&feature=youtu.be)  |