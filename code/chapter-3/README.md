# Code for Chapter 3: Cats versus Dogs: Transfer Learning in 30 Lines with Keras

We use transfer learning to reuse a previously trained network on a new custom classification task to get near state-of-the-art accuracy in a matter of minutes. We then slice and dice the results to understand how well is it classifying. Along the way, we build a common machine learning pipeline, which is repurposed throughout the book.

On the note of transfer learning, we hear from **Jeremy Howard**, co-founder of fast.ai on how hundreds of thousands of students use transfer learning to jumpstart their AI journey.

Read the chapter online [here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch03.html)

## Code

Go through the code in the following order:

1. [1-building-a -custom-classifier-in-keras-with-transfer-learning.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-3/1-keras-custom-classifier-with-transfer-learning.ipynb): We will build a custom classifier in Keras in 30 lines!
2. [2-analyzing-the-results.ipynb](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-3/2-analyzing-the-results.ipynb): With our trained model, we can analyze how it's performing over the validation dataset. Beyond the simpler accuracy metrics, looking at the actual images of mispredictions should give an intuition on whether the example was truly hard or if our model is not sophisticated enough.

## Data

Download the `Cats and Dogs` dataset from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/download/train.zip) and place it in the `data` directory. You may have to create an account on Kaggle in order to download the data.
