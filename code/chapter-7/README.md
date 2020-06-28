# Chapter 7 - Practical Tools, Tips, and Tricks

We diversify our practical skills in a variety of topics and tools, ranging from installation, data collection, experiment management, visualizations, keeping track of the state-of-the-art in research all the way to exploring further avenues for building the theoretical foundations of deep learning. [Continue reading online.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch07.html)

Due to the fast-changing pace of the artificial intelligence (AI) field, this chapter is a small subset of the “living” document hosted here, where it is constantly evolving. A living document, such as an article on Wikipedia, is a document that is continually edited and updated to reflect the latest knowledge. We, the authors, encourage you to contribute towards this document. If you have more questions or, even better, answers that might help other readers, feel free to tweet them at [@PracticalDLBook](https://twitter.com/practicaldlbook) or submit a pull request.

## How to use this living document

First off, welcome! We are happy that you have decided to use the book and the code to learn more about Deep Learning! We wish you the best for your journey forward. Consider this a living chapter where you can contribute to make continual updates to the best practices guidelines that have been detailed in the chapter. Here are a few things to keep in mind while using the document:

- Due to the fast-changing pace of the artificial intelligence (AI) field, this “living” document is constantly evolving.
- With the power of crowdsourcing, we hope that this document can become ready reckoner to help a wide range of audience, from people starting out in the field, as well as practioners. Please see the `CONTRIBUTING` section below for information on how you can help.

### Contributing

Please file a issue according to [CONTRIBUTING](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/CONTRIBUTING.md) and we will investigate. If you have more questions or, even better, answers that might help other readers, feel free to tweet them at [@PracticalDLBook](https://twitter.com/practicaldlbook) or submit a pull request.

Table of contents
=================
- [Installation](#installation)
  * [Q: I came across an interesting and useful Jupyter Notebook on GitHub. Making the code run will require cloning the repository, installing packages, setting up the environment, and more steps. Is there an instant way to run it interactively?](#q-i-came-across-an-interesting-and-useful-jupyter-notebook-on-github-making-the-code-run-will-require-cloning-the-repository-installing-packages-setting-up-the-environment-and-more-steps-is-there-an-instant-way-to-run-it-interactively)
  * [Q: What is the quickest way to get my deep learning setup running on a fresh Ubuntu machine with NVIDIA Graphics Processing Units (GPUs)?](#q-what-is-the-quickest-way-to-get-my-deep-learning-setup-running-on-a-fresh-ubuntu-machine-with-nvidia-graphics-processing-units-gpus)
  * [Q: What is the fastest way to install TensorFlow on a Windows PC?](#q-what-is-the-fastest-way-to-install-tensorflow-on-a-windows-pc)
  * [Q: I have an AMD GPU. Could I benefit from GPU speedups in TensorFlow on my existing system?](#q-i-have-an-amd-gpu-could-i-benefit-from-gpu-speedups-in-tensorflow-on-my-existing-system)
  * [Q: Forget installation, where can I get preinstalled deep learning containers?](#q-forget-installation-where-can-i-get-preinstalled-deep-learning-containers)
  * [Q: I just learnt about this new shiny Python package. What are the different tools to install a Python package?](#q-i-just-learnt-about-this-new-shiny-python-package-what-are-the-different-tools-to-install-a-python-package)
- [Hardware](#hardware)
  * [Q: Do I really need a GPU?](#q-do-i-really-need-a-gpu)
  * [Q: I don’t have that kind of money. Could I get a free GPU please?](#q-i-don-t-have-that-kind-of-money-could-i-get-a-free-gpu-please)
  * [Q: Is there a way I can calculate the energy consumption of my model?](#q-is-there-a-way-i-can-calculate-the-energy-consumption-of-my-model)
- [Training](#training)
  * [Q: I don’t like having to stare at my screen constantly to check whether my training finished. Can I get a notification alert on my phone, instead?](#q-i-don-t-like-having-to-stare-at-my-screen-constantly-to-check-whether-my-training-finished-can-i-get-a-notification-alert-on-my-phone-instead)
  * [Q: I prefer graphics and visualizations over plain text. Can I get real-time visualizations for my training process?](#q-i-prefer-graphics-and-visualizations-over-plain-text-can-i-get-real-time-visualizations-for-my-training-process)
  * [Q: I conduct a lot of experiments iteratively and often lose track of what changed between each experiment as well as the effect of the change. How do I manage my experiments in a more organized manner?](#q-i-conduct-a-lot-of-experiments-iteratively-and-often-lose-track-of-what-changed-between-each-experiment-as-well-as-the-effect-of-the-change-how-do-i-manage-my-experiments-in-a-more-organized-manner)
  * [Q: How do I check whether TensorFlow is using the GPU(s) on my machine?](#q-how-do-i-check-whether-tensorflow-is-using-the-gpu-s-on-my-machine)
  * [Q: I have multiple GPUs on my machine. I don’t want my training script to consume all of them. How do I restrict my script to run on only a specific GPU?](#q-i-have-multiple-gpus-on-my-machine-i-don-t-want-my-training-script-to-consume-all-of-them-how-do-i-restrict-my-script-to-run-on-only-a-specific-gpu)
  * [Q: Sometimes, it feels like there are too many knobs to adjust when training. Can it be done automatically, instead, to get the best accuracy?](#q-sometimes-it-feels-like-there-are-too-many-knobs-to-adjust-when-training-can-it-be-done-automatically-instead-to-get-the-best-accuracy)
  * [Q: ResNet and MobileNet work well enough for my use case. Is it possible to build a model architecture that can achieve even higher accuracy for my scenario?](#q-resnet-and-mobilenet-work-well-enough-for-my-use-case-is-it-possible-to-build-a-model-architecture-that-can-achieve-even-higher-accuracy-for-my-scenario)
  * [Q: How do I go about debugging my TensorFlow script?](#q-how-do-i-go-about-debugging-my-tensorflow-script)
  * [Q: Is there a way to profile my code?](#q-is-there-a-way-to-profile-my-code)
- [Distributed Training](#distributed-training)
  * [Q: How can I make my Keras code 30x faster? Is there another magic one liner that I can use?](#q-how-can-i-make-my-keras-code-30x-faster-is-there-another-magic-one-liner-that-i-can-use)
  * [Q: What are some frameworks I can use to distribute training with minimal code changes?](#q-what-are-some-frameworks-i-can-use-to-distribute-training-with-minimal-code-changes)
- [Production](#production)
  * [Q: What are some open source libraries that ease deployment and monitoring of deployed models?](#q-what-are-some-open-source-libraries-that-ease-deployment-and-monitoring-of-deployed-models)
  * [Q: How can I stay updated on the best practices in deployment?](#q-how-can-i-stay-updated-on-the-best-practices-in-deployment)
- [Model](#model)
  * [Q: I want to quickly know the input and output layers of my model without writing code. How can I accomplish that?](#q-i-want-to-quickly-know-the-input-and-output-layers-of-my-model-without-writing-code-how-can-i-accomplish-that)
  * [Q: I need to publish a research paper. Which tool should I use to draw my organic, free-range, gluten-free model architecture?](#q-i-need-to-publish-a-research-paper-which-tool-should-i-use-to-draw-my-organic-free-range-gluten-free-model-architecture)
  * [Q: Is there a one-stop shop for all models?](#q-is-there-a-one-stop-shop-for-all-models)
  * [Q: I’ve finished training my model. How can I make it available for others to use?](#q-i-ve-finished-training-my-model-how-can-i-make-it-available-for-others-to-use)
  * [Q: I have a model previously trained in framework X but I need to use it in framework Y. Do I need to waste time retraining it in framework Y?](#q-i-have-a-model-previously-trained-in-framework-x-but-i-need-to-use-it-in-framework-y-do-i-need-to-waste-time-retraining-it-in-framework-y)
- [Data](#data)
  * [Q: Could I collect hundreds of images on a topic in a few minutes?](#q-could-i-collect-hundreds-of-images-on-a-topic-in-a-few-minutes)
  * [Q: Forget the browser. How do I scrape Google for images using the command line?](#q-forget-the-browser-how-do-i-scrape-google-for-images-using-the-command-line)
  * [Q: Those were not enough for collecting images. I need more control. What other tools can help me download data in more custom ways beyond the search engine?](#q-those-were-not-enough-for-collecting-images-i-need-more-control-what-other-tools-can-help-me-download-data-in-more-custom-ways-beyond-the-search-engine)
  * [Q: I have the images for the target classes, but now need images for the negative (not item/background) class. Any quick ways to build a big dataset of negative classes?](#q-i-have-the-images-for-the-target-classes-but-now-need-images-for-the-negative-not-item-background-class-any-quick-ways-to-build-a-big-dataset-of-negative-classes)
  * [Q: How can I search for a prebuilt dataset that suits my needs?](#q-how-can-i-search-for-a-prebuilt-dataset-that-suits-my-needs)
  * [Q: For datasets like ImageNet, downloading, figuring out the format, and then loading them for training takes far too much time. Is there an easy way to read popular datasets?](#q-for-datasets-like-imagenet-downloading-figuring-out-the-format-and-then-loading-them-for-training-takes-far-too-much-time-is-there-an-easy-way-to-read-popular-datasets)
  * [Q: Training on the millions of ImageNet images will take a long, long time. Is there a smaller representative dataset I could try training on, to quickly experiment and iterate with?](#q-training-on-the-millions-of-imagenet-images-will-take-a-long-long-time-is-there-a-smaller-representative-dataset-i-could-try-training-on-to-quickly-experiment-and-iterate-with)
  * [Q: What are the largest readily available datasets that I could use for training?](#q-what-are-the-largest-readily-available-datasets-that-i-could-use-for-training)
  * [Q: What are some of the readily available large video datasets I could use?](#q-what-are-some-of-the-readily-available-large-video-datasets-i-could-use)
  * [Q: Are those the largest labeled datasets ever assembled in the history of time?](#q-are-those-the-largest-labeled-datasets-ever-assembled-in-the-history-of-time)
  * [Q: How can I get help annotating data?](#q-how-can-i-get-help-annotating-data)
  * [Q: Is there a versioning tool for datasets, like Git is for code?](#q-is-there-a-versioning-tool-for-datasets-like-git-is-for-code)
  * [Q: What if I don’t have access to a large dataset for my unique problem?](#q-what-if-i-don-t-have-access-to-a-large-dataset-for-my-unique-problem)
- [Privacy](#privacy)
  * [Q: How do I develop a more privacy-preserving model without going down the cryptography rabbit hole?](#q-how-do-i-develop-a-more-privacy-preserving-model-without-going-down-the-cryptography-rabbit-hole)
  * [Q: Can I keep my model under wraps from prying eyes?](#q-can-i-keep-my-model-under-wraps-from-prying-eyes)
- [Education and Exploration](#education-and-exploration)
  * [Q: I want to become an AI expert. Beyond this book, where should I invest my time to learn more?](#q-i-want-to-become-an-ai-expert-beyond-this-book-where-should-i-invest-my-time-to-learn-more)
  * [Q: Where can I find interesting notebooks to learn from?](#q-where-can-i-find-interesting-notebooks-to-learn-from)
  * [Q: Where can I learn about the state of the art for a specific topic?](#q-where-can-i-learn-about-the-state-of-the-art-for-a-specific-topic)
  * [Q: I am reading a paper on Arxiv and I really like it. Do I need to write code from scratch?](#q-i-am-reading-a-paper-on-arxiv-and-i-really-like-it-do-i-need-to-write-code-from-scratch)
  * [Q: I don’t want to write any code, but I still want to interactively experiment with a model using my camera. How can I do that?](#q-i-don-t-want-to-write-any-code-but-i-still-want-to-interactively-experiment-with-a-model-using-my-camera-how-can-i-do-that)
  * [Q: If I can test without code, can I train without code, too?](#q-if-i-can-test-without-code-can-i-train-without-code-too)
- [One Last Question](#one-last-question)
  * [Q: Tell me a great deep learning prank?](#q-tell-me-a-great-deep-learning-prank)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Installation

### Q: I came across an interesting and useful Jupyter Notebook on GitHub. Making the code run will require cloning the repository, installing packages, setting up the environment, and more steps. Is there an instant way to run it interactively?

Simply enter the Git repository URL into Binder (mybinder.org), which will turn it into a collection of interactive notebooks. Under the hood, it will search for a dependency file, like `requirements.txt` or `environment.yml` in the repository’s root directory. This will be used to build a Docker image, to help run the notebook interactively in your browser.

### Q: What is the quickest way to get my deep learning setup running on a fresh Ubuntu machine with NVIDIA Graphics Processing Units (GPUs)?

Life would be great if pip install tensorflow-gpu would solve everything. However, that’s far from reality. On a freshly installed Ubuntu machine, listing all the installation steps would take at least three pages and more than an hour to follow, including installing NVIDIA GPU drivers, CUDA, cuDNN, Python, TensorFlow, and other packages. And then it requires carefully checking the version interoperability between CUDA, cuDNN and TensorFlow. More often than not, this ends in a broken system. A world of pain to say the least! Wouldn’t it be great if two lines could solve all of this effortlessly? Ask, and ye shall receive:

```
$ sudo apt update && sudo ubuntu-drivers autoinstall && sudo reboot
$ export LAMBDA_REPO=$(mktemp) \
&& wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb \
&& sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} \
&& sudo apt-get update && sudo apt-get install -y lambda-stack-cuda && sudo reboot
```

The first line ensures that all the drivers are updated. The second line is brought to us by the Lambda Labs, a San Francisco–based deep learning hardware and cloud provider. The command sets up the Lambda Stack, which installs TensorFlow, Keras, PyTorch, Caffe, Caffe 2, Theano, CUDA, cuDNN, and NVIDIA GPU drivers. Because the company needs to install the same deep learning packages on thousands of machines, it automated the process with a one-line command and then open sourced it so that others can also make use of it.

### Q: What is the fastest way to install TensorFlow on a Windows PC?

1. Install Anaconda Python 3.7
2. On the command line, run `conda install tensorflow-gpu`. This single command will enable Anaconda to install tensorflow-gpu, CUDA, and cuDNN.
3. If you do not have GPUs, run `conda install tensorflow`

One additional benefit of CPU-based Conda installations is that it installs Intel MKL optimized TensorFlow, running faster than the version we get by using `pip install tensorflow`.

### Q: I have an AMD GPU. Could I benefit from GPU speedups in TensorFlow on my existing system?

Although the majority of the deep learning world uses NVIDIA GPUs, there is a growing community of people running on AMD hardware with the help of the ROCm stack. Installation using the command line is simple:

```
1. sudo apt install rocm-libs miopen-hip cxlactivitylogger
2. sudo apt install wget python3-pip
3. pip3 install --user tensorflow-rocm
```

### Q: Forget installation, where can I get preinstalled deep learning containers?

Docker is synonymous with setting up environments. Docker helps run isolated containers which are bundled with tools, libraries and configuration files. There are several deep learning Docker containers available while selecting your virtual machine (VM) from major cloud providers (Amazon Web Services [AWS], Microsoft Azure, Google Cloud Platform [GCP], Alibaba, etc.) which are ready to start working. NVIDIA also freely provides NVIDIA GPU Cloud (NGC) containers, which are the same high-performance containers used to break training speed records on the MLPerf benchmarks. You can even run these containers on your desktop machine. You can also use NGC on Windows systems using the Windows Insider Preview program.

### Q: I just learnt about this new shiny Python package. What are the different tools to install a Python package?

Either build it manually from source or use a package manager like Pip or Conda. Let's look at these in detail:

- Pip:
  - Most commonly used installation tool for python packages.
  - Finds & installs packages visible on the Python Package Index:  https://pypi.org/

- Conda:
  - Going beyond Pip, handles dependencies outside python packages, so less chances of installation issues. For example, non-Python library dependencies, such as HDF5, MKL, LLVM get installed automatically by Conda when required.
  - Package dependency & management for many languages beyond Python, such as R, C++, Ruby, Lua, Java, etc
  - Package manager for Anaconda distribution, which sets up a full deep learning environment in one command.

Pip and Conda don’t work interoperably. Stick to using either one of them.

## Hardware

### Q: Do I really need a GPU?

While beginning on your deep learning journey, specially on small datasets, your personal non-GPU machine would still get you results, just slowly. But if you are getting serious about training deep learning models, then surely get a GPU. A decent GPU should instantly give you ~20x speedup over your CPU programs.

### Q: I don’t have that kind of money. Could I get a free GPU please?

Try Google Colab and Kaggle Kernels.

- Google Colaboratory (or Colab) is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud. With Colaboratory, you can write and execute code, save (on Google Drive or Github) and share your analyses. More importantly, you get access to powerful GPU accelerator - for free. Wait, free for real? What’s the catch? Your session cannot last longer than 12 hours, so don’t get started on mining Bitcoins.
- Kaggle Kernels also provides free coding and execution environment (like Jupyter notebook) along where the code can be run live. Essentially, it's a docker container with most of the common data science packages pre installed, which gets loaded in a virtual machine and accessible from a notebook like user interface. Plus it gives you access to a GPU. And what’s the catch here: GPU availability depends on how many other users are accessing it. Plus if your notebook has been idle for an hour with no code changes, the session is suspended.

Both these environments are great for learning and exploring the deep learning landscape, but not ideal for more professional work.

### Q: Is there a way I can calculate the energy consumption of my model?

Checkout the CO2 impact calculator: https://mlco2.github.io/impact/ that not only helps compute the carbon emissions from model training and experimentation but it also makes a case for transparency by including the results in publications. You can use it with popular cloud providers as well as on your desktop machines.


## Training

### Q: I don’t like having to stare at my screen constantly to check whether my training finished. Can I get a notification alert on my phone, instead?

Use Knock Knock, a Python library that, as the name suggests, notifies you when your training ends (or your program crashes) by sending alerts on email, Slack, or even Telegram! Best of all, it requires adding only two lines of code to your training script. No more opening your program a thousand times to check whether the training has finished.

Apart from KnockKnock, there is also [TensorDash](https://github.com/CleanPegasus/TensorDash) that allows training monitoring in real-time and can integrate with all the major deep learning frameworks. Like KnockKnock you’ll also get notifications for training completion and metrics along with graphs.

### Q: I prefer graphics and visualizations over plain text. Can I get real-time visualizations for my training process?

FastProgress progress bar (originally developed for fast.ai by Sylvain Gugger) comes to the rescue.

### Q: I conduct a lot of experiments iteratively and often lose track of what changed between each experiment as well as the effect of the change. How do I manage my experiments in a more organized manner?

Software development has had the ability to keep a historical log of changes through version control. Machine learning unfortunately did not have the same luxury. That’s changing now with tools like Weights and Biases, and CometML. They allow you to keep track of multiple runs and to log training curves, hyperparameters, outputs, models, notes and more with just two lines of code added to your Python script. Best of all, through the power of the cloud, you can conveniently track experiments even if you are away from the machine, and share the results with others.

### Q: How do I check whether TensorFlow is using the GPU(s) on my machine?

Use the following handy command `tf.test.is_gpu_available()`.

### Q: I have multiple GPUs on my machine. I don’t want my training script to consume all of them. How do I restrict my script to run on only a specific GPU?

Use `CUDA_VISIBLE_DEVICES=GPU_ID` . Simply prefix the training script command as follows:

```
$ CUDA_VISIBLE_DEVICES=GPU_ID python train.py
```

Alternatively, write the following lines early on in your training script:

```
import os
os.environ["CUDA_VISIBLE_DEVICES"]="GPU_ID"
```

GPU_ID can have values such as 0, 1, 2, and so on. You can see these IDs (along with GPU usage) using nvidia-smi command. For assigning to multiple GPUs, use a comma-separated list of IDs.

### Q: Sometimes, it feels like there are too many knobs to adjust when training. Can it be done automatically, instead, to get the best accuracy?

There are many options for automated hyperparameter tuning, including Keras-specific Hyperas and Keras Tuner, and more generic frameworks such as Hyperopt and Bayesian Optimization that perform extensive experimentation to maximize our objective (i.e., maximizing accuracy in our case) more intelligently than simple grid searches.

### Q: ResNet and MobileNet work well enough for my use case. Is it possible to build a model architecture that can achieve even higher accuracy for my scenario?

Three words: Neural Architecture Search (NAS). Let the algorithm find the best architecture for you. NAS can be accomplished through packages like Auto-Keras and AdaNet.

### Q: How do I go about debugging my TensorFlow script?

The answer is in the question: TensorFlow Debugger (tfdbg).

### Q: Is there a way to profile my code?

There are in fact, multiple options to choose from!

**TensorFlow Profiler**: Google released the TensorFlow profiler, which brings a new set of tools that you can use to measure the training performance and resource consumption of TensorFlow models.
Checkout the blog post from the TensorFlow team: https://www.tensorflow.org/guide/profiler 

**Deep Learning Profiler**: Another profiler from Nvidia is a tool for profiling deep learning models to help data scientists understand and improve performance of their models visually via Tensorboard or by analyzing text reports: https://docs.nvidia.com/deeplearning/frameworks/dlprof-user-guide/ 

**Cuda profiler**: This NVIDIA released profiling tool enables you to understand and optimize the performance of your CUDA, OpenACC or OpenMP applications. The Visual Profiler is a graphical profiling tool that displays a timeline of your application's CPU and GPU activity, and that includes an automated analysis engine to identify optimization opportunities. The nvprof profiling tool enables you to collect and view profiling data from the command-line: https://docs.nvidia.com/cuda/profiler-users-guide/index.html 

## Distributed Training

### Q: How can I make my Keras code 30x faster? Is there another magic one liner that I can use?

Of Course there is! Using UC Berkeley's Ray as a distribution method under the hood while maintaining the same Keras API gives us an open-source framework called dKeras: https://github.com/dkeras-project/dkeras.

There’s a fantastic article on Medium introducing dKeras that talks about the functionalities that it offers: https://medium.com/@offercstephen/dkeras-make-keras-faster-with-a-few-lines-of-code-a1792b12dfa0.

### Q: What are some frameworks I can use to distribute training with minimal code changes?

DeepSpeed from Microsoft is a deep learning optimization library that makes distributed training easy, efficient, and effective. It claims to enable training models with over a hundred billion parameters on the latest GPUs and achieves 10x system performance over SOTA: https://github.com/microsoft/DeepSpeed/blob/master/README.md

## Production

### Q: What are some open source libraries that ease deployment and monitoring of deployed models?

There are a bunch of open source libraries that not only help in deployment but also enable scaling, automatic versioning, monitoring of deployed models and making sure that your model is kept hidden from prying eyes. You can find a detailed list here: https://github.com/EthicalML/awesome-production-machine-learning

### Q: How can I stay updated on the best practices in deployment?

The ML in Production newsletter publishes best practices for running ML systems in production: https://mlinproduction.com/

One of the more latest open source platforms for model serving is BentoML. Check out this Reddit thread for a cost comparison between BentoML, TensorFlow Serving, Clipper and AWS SageMaker: https://www.reddit.com/r/deeplearning/comments/g1civx/bentoml_an_opensource_platform_for/

## Model

### Q: I want to quickly know the input and output layers of my model without writing code. How can I accomplish that?

Use Netron. It graphically shows your model, and on clicking any layer, provides details on the architecture.

### Q: I need to publish a research paper. Which tool should I use to draw my organic, free-range, gluten-free model architecture?

MS Paint, obviously! No, we’re just kidding. We are fans of NN-SVG as well as Plot‐NeuralNet for creating high-quality Convolutional Neural Network (CNN) diagrams.

### Q: Is there a one-stop shop for all models?

Indeed! Explore PapersWithCode.com, ModelZoo.co, and ModelDepot.io for some inspiration.

### Q: I’ve finished training my model. How can I make it available for others to use?

You can begin by making the model to download from GitHub. And then list it on model zoos mentioned in the previous answer. For even wider adoption, upload it to Tensorflow Hub (tfhub.dev). In addition to the model, you should publish a “model card,” which is essentially like a résumé of the model. It’s a short report that details author information, accuracy metrics and the dataset it was benchmarked on. Additionally, it provides guidance on
potential biases and out-of-scope uses.

### Q: I have a model previously trained in framework X but I need to use it in framework Y. Do I need to waste time retraining it in framework Y?

Nope. All you need is the power of Open Neural Network Exchange (ONNX). For models not in the TensorFlow ecosystem, most major deep learning libraries support saving them in ONNX format that can then be converted to the TensorFlow format. Microsoft’s MMdnn can help in this conversion.

## Data

### Q: Could I collect hundreds of images on a topic in a few minutes?

Yes, you can collect hundreds of images in three minutes or less with a Chrome extension called Fatkun Batch Download Image. Simply search for a keyword in your favorite image search engine, filter images by the correct usage rights (e.g., Public Domain), and press the Fatkun extension to download all images. See Chapter 12, where we use it to build a Not Hotdog app.

Bonus tip: to download from a single website, search for a keyword followed by site:website_address. For example “horse site:flickr.com.”

Note: Since more extensions slow the browser load time, it is recommended to turn off the browser extension after it has been used.

### Q: Forget the browser. How do I scrape Google for images using the command line?

```
$ pip install google_images_download
$ googleimagesdownload -k=horse -l=50 -r=labeled-for-reuse
-k , -l , and -r are shorthand for keyword , limit (number of images), and usage_rights , respectively. This is a powerful tool with many options for controlling and filtering what images to download from Google searches.
```
Plus, instead of just loading the thumbnails shown by Google Images, it saves the original images linked by the search engine. For saving more than 100 images, install the `selenium` library along with `chromedriver`.

### Q: Those were not enough for collecting images. I need more control. What other tools can help me download data in more custom ways beyond the search engine?

With a graphical user interface (GUI) (no programming needed):
- ScrapeStorm.com
  Easy GUI to identify rules for elements to extract
- WebScraper.io
  Chrome-based scraping extension, especially for extracting structured output from single websites
- 80legs.com
  Cloud-based scalable scraper, for parallel, large tasks

Python-based programmatic tools:
- Scrapy.org
  For more programmable controls on scraping, this is one of the most famous scrapers. Compared to building your own naive scraper to exploring websites, it offers throttling rate by domain, proxy, IP, can handle robots.txt, offers flexibility in browser headers to show to web servers, and takes care of several possible edge cases.
- InstaLooter
  A Python-based tool for scraping Instagram.

### Q: I have the images for the target classes, but now need images for the negative (not item/background) class. Any quick ways to build a big dataset of negative classes?

ImageN offers 1,000 images—5 random images for 200 ImageNet categories—which you can use as the negative class. If you need more, download a random sample programmatically from ImageNet.

### Q: How can I search for a prebuilt dataset that suits my needs?

Try, Google Dataset Search, VisualData.io and DatasetList.com.

### Q: For datasets like ImageNet, downloading, figuring out the format, and then loading them for training takes far too much time. Is there an easy way to read popular datasets?

TensorFlow Datasets is a growing collection of datasets ready to use with TensorFlow. It includes ImageNet, COCO (37 GB) and Open Images (565 GB) among others. These datasets are exposed as tf.data.Datasets , along with performant code to feed them in your training pipeline.

### Q: Training on the millions of ImageNet images will take a long, long time. Is there a smaller representative dataset I could try training on, to quickly experiment and iterate with?

Try Imagenette. Built by Jeremy Howard from fast.ai, this 1.4 GB dataset contains only 10 classes instead of 1,000.

### Q: What are the largest readily available datasets that I could use for training?


|   **Name**    | **Details** | **Task** |
|:-----------:|:-----------:|:------------:|
| Tencent ML Images | <ul><li>17.7 million images with 11,000 category labels</li><li>8 tags per image (avg)</li><li>1447 images per category (avg)</li><li>Combines ImageNet & Open Images</li></ul> |Classification|
| Open Images V4 (from Google) |  <ul><li>9 million images in 19.7K categories</li><li>1.74M images with 600 categories (bounding boxes)</li><li>8 objects per image (avg)</li><li>Randomly sampled from Flickr without a predefined list of tags, leading to natural class statistics. </li></ul>  |  <ul><li>Classification</li><li>Detection</li></ul> |
| BDD100K (from UC Berkeley) | <ul><li>100K driving videos over 1100 hours</li><li>100K images with bounding boxes for 10 categories</li><li>100K images with lane markings</li><li>100K images with drivable area segmentation</li><li>10K images with pixel level instance segmentation</li></ul> |  <ul><li>Classification</li><li>Detection</li><li>Segmentation</li></ul> |
| YFCC100M (from Yahoo) | <ul><li>99.2M images</li><li>0.8M videos</li><li>Random sample collected from Flickr</li><li>Noisy user-added tags</li><li>Creative Commons license</li></ul>| Classification | 
| Microsoft COCO: Common Objects in Context | <ul><li>330K images with 80 objects categories</li><li>Contains bounding boxes, segmentation, and 5 captions per image</li></ul> | <ul><li>Classification</li><li>Detection</li><li>Segmentation</li><li>Captioning</li></ul> |
| Fashion MNIST (from Zalando) | <ul><li>70,000 images in 10 clothing classes</li><li>28x28 greyscale</li><li>Drop in replacement for MNIST dataset </li></ul> | Classification|

### Q: What are some of the readily available large video datasets I could use?

|   **Name**   | **Details**|
|:-----------:|:-----------:|
|   YouTube-8M    |  <ul><li>6.1 million videos</li><li>3,862 classes</li><li>2.6 billion audio-visual features</li><li>3.0 labels/video</li><li>1.53 Terabytes of randomly sampled videos</li></ul>     |
|  Something Something (from Twenty Billion Neurons)   |     <ul><li>221,000 videos in 174 action classes</li><li>For example, “Pouring water into wine glass but missing so it spills next to it”</li><li>Humans performing predefined actions with everyday objects</li></ul> |
|Jester (from Twenty Billion Neurons) | <ul><li>148,000 videos in 27 classes</li><li>For example, “Zooming in with two fingers”</li><li>Predefined hand gestures in front of a webcam</li></ul> |

### Q: Are those the largest labeled datasets ever assembled in the history of time?

Nope! Companies like Facebook and Google curate their own private datasets that are much larger than the public ones we can play with:

- Facebook: 3.5 billion Instagram images with noisy labels (First reported in 2018)
- Google - JFT-300M: 300 million images with noisy labels (First reported in 2017)

Sadly, unless you’re an employee at one of these companies, you can’t really access these datasets. Nice recruiting tactic, though, we must say.

### Q: How can I get help annotating data?

There are several companies out there that can assist with labeling different kinds of annotations. A few worth mentioning include SamaSource, Digital Data Divide, and iMerit, which employ people who otherwise have limited opportunities, eventually creatingpositive socio-economic change through employment in underprivileged communities.

### Q: Is there a versioning tool for datasets, like Git is for code?

Qri and Quilt can help version control our datasets, aiding in reproducibility of experiments.

### Q: What if I don’t have access to a large dataset for my unique problem?

Try to develop a synthetic dataset for training! For example, find a realistic 3-D model of the object of interest and place it in realistic environments using a 3-D framework such as Unity. Adjust the lighting and camera position, zoom, and rotation to take snapshots of this object from many angles, generating an endless supply of training data. Alternatively, companies like AI.Reverie, CVEDIA, Neuromation, Cognata, Mostly.ai, and DataGen Tech provide realistic simulations for training needs. One big benefit of synthesized training data is that the labeling process is built into the synthesization process. After all, you would know what you are creating. This automatic labeling can save a lot of money and effort, compared to manual labeling.

## Privacy

### Q: How do I develop a more privacy preserving model without going down the cryptography rabbit hole?

TensorFlow Encrypted might be the solution you’re looking for. It enables development using encrypted data, which is relevant, especially if you are on the cloud. Internally, lots of secure multiparty computation and homomorphic encryptions result in privacy-preserving machine learning.

### Q: Can I keep my model under wraps from prying eyes?

Well, unless you are on the cloud, weights are visible and can be reverse engineered. Use Fritz library for protecting your model’s IP when deployed on smartphones.

## Education and Exploration

### Q: I want to become an AI expert. Beyond this book, where should I invest my time to learn more?

There are several resources on the internet to learn deep learning in depth. We highly recommend these video lectures from some of the best teachers, covering a variety of application areas from computer vision to natural language processing.

- Fast.ai (by Jeremy Howard and Rachel Thomas) features a free 14-video lecture series, taking a more learn-by-doing approach in PyTorch. Along with the course comes an ecosystem of tools, active community which has led to many breakthroughs in the form of research papers and ready-to-use code (like three lines of code to train a state-of-the-art network using the fast.ai library).
- Deeplearning.ai (by Andrew Ng) features a five-course “Deep Learning Specialization.” It’s free of cost (although you could pay a small fee to get a certificate) and will solidify your theoretical foundation further. Dr. Ng’s first Coursera course on machine learning has taught more than two million students, and this series continues the tradition of highly approachable content loved by beginners and experts alike. An online set of notes for this course have been developed by Chris Maxwell ([maxxiimo](https://github.com/maxxiimo)) and are available at: http://chrismaxwell.com/ai/Deep%20Learning%20Specialization.pdf. 
- We would be remiss if we didn’t encourage you to note O’Reilly’s Online Learning platform in this list. Helping more than two million users advance their
careers, it contains hundreds of books, videos, live online trainings, and keynotes given by leading thinkers and practitioners at O’Reilly’s AI and data conferences.

Following are some resources that allow one to play with different training scenarios in the browser without the need to install any packages! It covers not only the theory but also helps to build the intuition to solve future problems. Take a look at the table below outlining a few video series, online books, and browser-based tools that will help further your understanding of the subject matter. 

| Name | What is it?| YouTube/Blog|
|:---:|:---:|:---:|
| [Teachable Machine](https://end-to-end-machine-learning.teachable.com/p/how-deep-neural-networks-work) by [Brandon Rohrer](https://www.linkedin.com/in/brohrer/) | Series of lectures describing how CNNs, RNNs and LSTMs work.| You can either register free-of-cost on the website, or view on [YouTube](https://www.youtube.com/watch?v=ILsA4nyG7I0&list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp)  | 
| [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) by [Michael Nielsen](http://michaelnielsen.org/)  | A free online book on Neural networks that is grounded in principles of deep learning.  |   |
| [TensorFlow Playground](https://playground.tensorflow.org/) by Google's Daniel Smilkov and Shan Carter  | An interactive browser-based tool that allows one to tinker with a neural network in the browser.  | [Blog](https://cloud.google.com/blog/products/gcp/understanding-neural-networks-with-tensorflow-playground)  |
| [ConvNet PlayGround](https://convnetplayground.fastforwardlabs.com/#/) By Cloudera's Fast Forward Labs  |  An interactive browser-based tool that does semantic image search using convolutional neural networks | [Blog](https://towardsdatascience.com/convnetplayground-979d441ebf82)  |
| [ConvNetJS](https://cs.stanford.edu/people/karpathy/convnetjs/) by Andrej Karpathy  | A Javascript library for training models in the browser. "Open a tab and you're training. No software requirements, no compilers, no installations, no GPUs, no sweat."  | [Introduction](https://cs.stanford.edu/people/karpathy/convnetjs/started.html)  |
| [CNN Explainer](https://poloclub.github.io/cnn-explainer/)  |  Visualize each convolution and filter as they pass through each image. | [YouTube](https://www.youtube.com/watch?v=HnWIHWFbuUQ&feature=youtu.be)  |




### Q: Where can I find interesting notebooks to learn from?

Google Seedbank is a collection of interactive machine learning examples. Built on top of Google Colaboratory, these Jupyter notebooks can be run instantly without any installations. Some interesting examples include:

- Generating audio with Generative Adversarial Networks (GANs)
- Action recognition on video
- Generating Shakespeare-esque text
- Audio-style transfer

### Q: Where can I learn about the state of the art for a specific topic?

Considering how fast the state of the art moves in AI, SOTAWHAT is a handy command line tool to search research papers for the latest models, datasets, tasks, and more. For example, to look up the latest results on ImageNet, use `sotawhat imagenet` on the command line. Additionally, PapersWithCode.com/SOTA also features repositories for papers, their source code and released models, along with an interactive visual timeline of benchmarks.

### Q: I am reading a paper on Arxiv and I really like it. Do I need to write code from scratch?

Not at all! ResearchCode Chrome extension makes it easy to find code when browsing arxiv.org or Google Scholar. All it takes is a press of the extension button. You can also look up code without installing the extension on ResearchCode.com website.

### Q: I don’t want to write any code, but I still want to interactively experiment with a model using my camera. How can I do that?

Runway ML is an easy-to-use yet powerful GUI tool that allows you to download models (from the internet or your own), use the webcam or other input, such as video files, to see the output interactively. This allows further combining and remixing outputs of models to make new creations. And all of this happens with just a few mouse clicks; hence, it’s attracting a large artist community!

### Q: If I can test without code, can I train without code, too?

We discuss this in detail in Chapter 8 (web-based) and Chapter 12 (desktop-based). To keep it short, tools such as Microsoft’s CustomVision.ai, Google’s Cloud AutoML Vision, Clarifai, Baidu EZDL and Apple’s Create ML provide drag-and-drop training capabilities. Some of these tools take as little as a few seconds to do the training.

## One Last Question

### Q: Tell me a great deep learning prank?

Print and hang poster from keras4kindergartners.com near the watercooler, and watch people’s reaction.