# Code for Chapter 5 - From Novice to Master Predictor: Maximizing Convolutional Neural Network Accuracy

We explore strategies to maximize the accuracy that our classifier can achieve, with the help of a range of tools including TensorBoard, What-If Tool, tf-explain, TensorFlow Datasets, AutoKeras, AutoAugment. Along the way, we conduct experiments to develop an intuition of what parameters might or might not work for your AI task. [Read online here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch05.html)

In this chapter, we will develop an intuition for recognizing opportunities to improve your models’ accuracy the next time you start training one. We will first look at the tools that will ensure that we won’t be going in blind. After that, for a good chunk of this chapter, we will be taking a very experimental approach by setting up a baseline, isolating individual parameters to tweak, and observing their effect on model performance and training speed. A lot of the code we will be using in this chapter is all aggregated in a single Jupyter notebook, along with an actionable [checklist](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/Checklist.md) with interactive examples. It is meant to be highly reusable should you choose to incorporate it in your next training script.

Through the experiments we will explore several questions that tend to come up during model training such as:
- I am unsure whether to use transfer learning or building from scratch to train my own network. What is the preferred approach for my scenario? 
- What is the least amount of data that I can supply to my training pipeline to get acceptable results?
- I want to ensure that the model is learning the right thing and not picking up spurious correlations. How can I get visibility into that?
- How can I ensure that I (or someone else) get the same results from my experiments every single time they are run? In other words, how do I ensure reproducibility of my experiments?
- Does changing the aspect ratio of the input images have an impact on the predictions?
- Does reducing input image size have a significant effect on prediction results?
- If I use transfer learning, what percentage of layers should I fine-tune to achieve my preferred balance of training time vs accuracy?
- Alternatively, if I were to train from scratch, how many layers should my model consist of?
- What is the appropriate ‘learning rate’ to supply during model training?
- There are too many things to remember. Is there a way to automate all of this work?

## Code

A lot of the code in this chapter can be executed through Google Colab. See [here](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=WzIRIt9d2huC) for instructions on how to load the [GitHub repository](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/) on Google Colab. keep in mind that you will access to your own Google Drive as we will be using data from a local system.

Go through the code in the following order:

1. [1-develop-tool.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/1-develop-tool.ipynb): In this file, we will develop a tool to experiment with various parameter settings of a model. One can choose amongst different kinds of augmentation techniques, use different datasets available in TensorFlow Datasets, choose to train either from scratch or use finetune from MobileNet or any model of your choice, all in the browser without any framework installs on your system.
1. [2-running-the-what-if-tool.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/2-running-the-what-if-tool.ipynb): Run the What-If tool on the trained model and dataset. A sample model and data is provided in the [`what-if-stuff`](https://github.com/PracticalDL/Practical-Deep-Learning-Book/tree/master/code/chapter-5/what-if-stuff) folder.
1. [3-tf-explain.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/3-tf-explain.ipynb): tf-explain (by Raphael Meudec) helps understand the results and inner workings of a neural network with the help of visualizations, removing the veil on bias in our datasets. Few different visualization approaches are available with tf.explain. In this notebook we will produce different visualizations on the sample images.
1. [4-keras-tuner.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/4-keras-tuner.ipynb): With so many potential combinations of hyperparameters to tune, coming up with the best model can be a tedious process. Often two or more parameters might have correlated effects on the overall speed of convergence as well as validation accuracy, so tuning one at a time might not lead to the best model. And if curiosity gets the best of us, we might want to experimentation on all the hyperparameters together! Keras Tuner comes to automate this hyperparameter search!
1. [5-autokeras.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/5-autokeras.ipynb): AI can finally automate designing AI architectures too. Neural Architecture Search (NAS) approaches utilize reinforcement learning to join together mini architectural blocks, till they are able to maximize the objective function - i.e. our validation accuracy. The current state of the art networks are all based on NAS, leaving human-designed architectures in the dust. Research in this area started showing promising results in 2017, with a bigger focus on making train faster in 2018. AutoKeras (Haifeng Jin et al), also apply this state of the art technique on our particular datasets in a relatively accessible manner.
1. [6-hparams.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-5/6-hparams.ipynb): One can experiment with absolutely ALL the parameters in the network such as the size of filters, optimizers, dropout value, etc. All the experiments that are in this chapter can be done via UI using HParams. All one needs to is tick the parameters in the UI and viola HParams will do the job! We will develop one such parameter server that allows one to filter the hyperparameters and metrics whose values should be shown on the dashboard, and like most TensorBoard visualizations, allows one to choose which run to visualize.

### Experiments

If you find yourself asking questions like:

- What is the appropriate ‘learning rate’ to supply during model training?
- There are several optimization algorithms to choose from. Which one is most appropriate for my scenario?
- How can I arrive at a good batch size for model training? What are the implications if the batch size was higher or lower?
- I want to ensure that the model is learning the right thing and not picking up spurious correlations. How can I get visibility into that?
- Is accuracy the only metric I should be concerned about? What other metrics are available to judge my model by?
- I don’t have equal amounts of data for each category I want to train on. Does that have a negative impact on model performance?
- How similar does my dataset have to be to ImageNet to get successful results from transfer learning? If it’s too dissimilar, what are my options?
- How do I prevent my model from overtraining and memorizing the input data?

Then, this chapter is just for you! The following experiments should help you make a choice:

- Transfer Learning vs Training from Scratch
- Effect of Number of Layers Fine-Tuned in Transfer Learning
- Effect of Choice of CNN Architecture on Transfer Learning
- Effect of number of layers in Custom Architectures
- Effect of number of filters in Custom Architectures
- Effect of initialization of filters in Custom Architectures
- Effect of Data Size on Transfer Learning
- Effect of Learning Rate
- Effect of optimizers
- Effect of batch size
- Effect of Resizing
- Effect of change in Aspect Ratio on Transfer Learning
- Effect of Image Resize Interpolation
- Effect of Augmentation
- Effect of Regularization - Dropout
- Effect of Regularization - Batch Normalization
- Effect of Activations - TanH vs Relu vs Sigmoid vs LeakyRelu vs ELU

### Guide to Improving Neural Network Accuracy

Using the above listed experiments, you will be able to develop your own guide to improving accuracy and speed. Such a guide will include:

- Using ReLu as an activation function is significantly faster.
- Batch Normalization layer is best placed after the linear activation layer, but if youre using dropout and RELU the order does not matter because the result will be the same.
- Recommended dropout value are between 0.3 to 0.5. Too much and your network will under train. Too little and it might over train. 0.3 to 0.5 sets a good range to try out.

## Data

In this chapter, we are trying to develop a single data input pipeline that can be used for training almost any model. The main advantage of pipelining is that we can choose any of the large number of available datasets and just plug and play.

TensorFlow Datasets is a collection of ~100 ready to use datasets that can quickly help build high-performance input data pipelines for training TensorFlow models. Instead of downloading and manipulating data sets manually, and figuring out how to read their labels, TensorFlow Datasets standardizes the data format, so it’s easy to swap one dataset with another, often with just a single line of code change. In this chapter, we will chiefly experiment with the datasets listed below:

| Dataset | Contents | Number of Categories  | Number of Images |
|---|---| -----| -----|
| Oxford Flowers 102 | Images of flowers commonly occurring in the United Kingdom | 102 | 8189 |
| Colorectal Histology | Textures in colorectal cancer histology | 8 | 5000 |
|Cats and Dogs| Images from [Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image Categorization](https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/)  | 2 | 23262|
| Caltech 101 | Pictures of objects belonging to 101 categories.  | 101 | 9801 |

We chose these datasets because they’re relatively difficult to train on due to how similar different categories are. They force the model to learn finer-level details of the data in order to distinguish them. In comparison to these, a lot of other datasets are easier to train on. If the techniques we cover in this chapter will work on these datasets, they should work on a lot of other datasets as well.
