# Chapter 4 - Building a Reverse Image Search Engine: Understanding Embeddings

Note: All images in this directory, unless specified otherwise, are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

## Figure List

| Figure number | Description | Notes |
|:---|:---|:---|
| [4-1](1-rgb-histogram?raw=true) | RGB histogram-based "Similar Image Detector" program | |
| [4-2](2-amazon-scan.png?raw=true) | Product scanner in Amazon app with visual features highlighted | |
| [4-3](3-tqdm.png) | Progress bar shown with tqdm_notebook | |
| [4-4](4-original-image.png?raw=true) |The query image from the Caltech-101 dataset | |
| [4-5](5-first-result.png?raw=true) | The nearest neighbor to our query image | |
| [4-6](6-second-closest.png?raw=true) | The second nearest neighbour of the queried image | |
| [4-7](7-nearest-neighbors.png?raw=true) | Nearest neighbor for different images returns similar-looking images | |
| [4-8](8-tsne.png?raw=true) | t-SNE visualizing clusters of image features, where each cluster represents one object class in the same color | |
| [4-9](9-tsne-clusters.png?raw=true) | t-SNE visualization showing image clusters; similar images in the same cluster | |
| [4-10](10-tsne-grid.png?raw=true) | t-SNE visualization with tiled images; similar images are close together | |
| [4-11](11-tensorflow-embedding-projector.png?raw=true) | TensorFlow Embedding projector showing a 3D representation of 10,000 common English words and highlighting words related to "Beatles" | |
| [4-12](12-variance-vs-num-pca-dimensions.png?raw=true) | Variance for each PCA dimension |
| [4-13](13-cumulative-variance-vs-num-pca-dimensions.png?raw=true) | Cumulative variance with each PCA dimension | |
| [4-14](14-test-time-vs-accuracy.png?raw=true) | Test time versus accuracy for each PCA dimension | |
| [4-15](15-recall-vs-qps.png?raw=true) | Comparison of ANN libraries ([data source](http://ann-benchmarks.com/)) | |
| [4-16](16-before-finetune.png?raw=true) | t-SNE visualization of feature vectors of least-accurate classes before fine tuning | |
| [4-17](17-after-finetune.png?raw=true) | t-SNE visualization of feature vectors of least-accurate classes after fine tuning | |
| [4-18](18-siamese-network-flowchart.png?raw=true) | A Siamese network for signature verification; note that the same CNN was used for both input images | |
| [4-19](https://code.flickr.net/2017/03/07/introducing-similarity-search-at-flickr/) | Similar patterns of a desert photo | |
| [4-20](https://labs.pinterest.com/user/themes/pin_labs/assets/paper/visual_search_at_pinterest.pdf) | The Similar Looks feature of the Pinterest application | |
| [4-21](21-celebs-like-me.png?raw=true) | Testing our friend Pete Warden’s photo on the [celebslike.me](celebslike.me) website | |
| [4-22](https://papers.nips.cc/paper/5004-deep-content-based-music-recommendation.pdf) | t-SNE visualization of the distribution of predicted usage patterns, using latent factors predicted from audio | Page 7 |
| [4-23a](23a-image-captioning.png?raw=true), [4-23b](23b-image-captioning.png?raw=true), [4-23c](23c-image-captioning.png?raw=true) | Image captioning feature in Seeing AI: the Talking Camera App for the blind community | |
| [4-24](https://arxiv.org/pdf/1608.08716.pdf) | Defining a CNN and visualizing the output of each layer during training in ConvNetJS | Page 2 |