# Code for Chapter 4: Building a Reverse Image Search Engine: Understanding Embeddings

Like Google Reverse Image Search, we explore how one can use embeddings — a contextual representation of an image to find similar images in under ten lines. And then the fun starts when we explore different strategies and algorithms to speed this up at scale, from thousands to several million images, and making them searchable in microseconds.

## Code

Go through the code in the following order:

1. [1-feature-extraction.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-4/1-feature-extraction.ipynb): We will extract features from pretrained models like VGG-16, VGG-19, ResNet-50, InceptionV3 and MobileNet and benchmark them using the Caltech101 dataset.
2. [2-similarity-search-level-1.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-4/2-similarity-search-level-1.ipynb): We write an indexer to index features and search for most similar features using various nearest neighbor algorithms, and explore various methods of visualizing plots.
3. [2-similarity-search-level-2.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-4/2-similarity-search-level-2.ipynb): we benchmark the algorithms based on the time it takes to index images and locate the most similar image based on its features using the Caltech-101 dataset. We also experiment with t-SNE and PCA.
4. [2-similarity-search-level-3.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-4/2-similarity-search-level-3.ipynb): So far we experimented with different visualization techniques on the results, t-SNE and PCA on the results. Now we will calculate the accuracies of the features obtained from the pretrained and finetuned models. The finetuning here follows the same finetuning technique we learnt in Chapter 2.
5. [3-reduce-feature-length-with-pca.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-4/3-reduce-feature-length-with-pca.ipynb): We will experiment with PCA and figure out what is the optimum length of the features to use in our experiments.
6. [4-improving-accuracy-with-fine-tuning.ipynb](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-4/4-improving-accuracy-with-fine-tuning.ipynb): Many of the pre-trained models were trained on the ImageNet dataset. Therefore, they provide an incredible starting point for similarity computations in most situations. That said, if you tune these models to adapt to your specific problem, they would perform even more accurately for finding similar images.

In this portion of the chapter, we will find the least accurate (worst) performing categories, visualize them with t-SNE, fine-tune and then see how their t-SNE graph changes.

## Data

We will be using the Caltech101 dataset. Please download the [Caltech101](http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz) dataset and place it in a `caltech101` directory.
