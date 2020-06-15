# Practical Deep Learning for Cloud, Mobile, and Edge

| This is the official code repository for the O'Reilly Publication,<br> [**Practical Deep Learning for Cloud, Mobile, and Edge**](https://www.oreilly.com/library/view/practical-deep-learning/9781492034858/) <br> by [Anirudh Koul](https://twitter.com/AnirudhKoul), [Siddha Ganju](https://twitter.com/siddhaganju) and [Meher Kasam](https://twitter.com/MeherKasam). <br><br><br> \*\* <b>Featured as a learning resource on the official [Keras](https://keras.io/getting_started/learning_resources/) website</b> \*\* | <a href="https://www.oreilly.com/library/view/practical-deep-learning/9781492034858/"><img src="https://github.com/sidgan/sidgan.github.com/raw/master/files/book-cover.PNG" width="360"> |
|---|---|

[[Online on Safari](https://www.oreilly.com/library/view/practical-deep-learning/9781492034858/)] | [[Buy on Amazon](https://www.amazon.com/Practical-Learning-Cloud-Mobile-Hands/dp/149203486X/)] | [[Online on Google Books](https://books.google.com/books?id=B_3ovwEACAAJ)] | [[Book Website](http://practicaldeeplearning.ai/)] | [[Presentation on Slideshare](https://www.slideshare.net/anirudhkoul/deep-learning-on-mobile-2019-practitioners-guide)]

Table of contents
=================

<!--ts-->
* [Book Description](#book-description)
* [Chapter List](#chapter-list)
* [How to Use this repository](#how-to-use-this-repository)
   * [Environment](#environment)
   * [Bug Reporting](#bug-reporting)
* [About the Authors](#about-the-authors)
* [Citation](#citation)
<!--te-->

## Book Description

Whether you’re a software engineer aspiring to enter the world of deep learning, a veteran data scientist, or a hobbyist with a simple dream of making the next viral AI app, you might have wondered where do I begin? This step-by-step guide teaches you how to build practical deep learning applications for the cloud, mobile, browser, and edge devices using a hands-on approach.

Relying on years of industry experience transforming deep learning research into award-winning applications, Anirudh Koul, Siddha Ganju, and Meher Kasam guide you through the process of converting an idea into something that people in the real world can use.

- Train, tune, and deploy computer vision models with Keras, TensorFlow, Core ML, and TensorFlow Lite
- Develop AI for a range of devices including Raspberry Pi, Jetson Nano, and Google Coral
- Explore fun projects, from Silicon Valley’s "Not Hotdog" app to 40+ industry case studies
- Simulate an autonomous car in a video game environment and build a miniature version with reinforcement learning.
- Use transfer learning to train models in minutes
- Discover 50+ practical tips for maximizing model accuracy and speed, debugging, and scaling to millions of users

## Chapter List
[**Chapter 1 - Exploring the Landscape of Artificial Intelligence**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-1) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch01.html) | [Figures](figures/chapter-1)

We take a tour of this evolving landscape, from 1950s till today, and analyze the ingredients that make for a perfect deep learning recipe, get familiar with common AI terminology and datasets, and take a peek into the world of responsible AI.

[**Chapter 2 - What’s in the Picture: Image Classification with Keras**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-2) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch02.html) | [Figures](figures/chapter-2)

We delve into the world of image classification in a mere five lines of Keras code. We then learn what neural networks are paying attention to while making predictions by overlaying heatmaps on videos. Bonus: we hear the motivating personal journey of **François Chollet**, the creator of Keras, illustrating the impact a single individual can have.

[**Chapter 3 - Cats versus Dogs: Transfer Learning in 30 Lines with Keras**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-3) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch03.html) | [Figures](figures/chapter-3)

We use transfer learning to reuse a previously trained network on a new custom classification task to get near state-of-the-art accuracy in a matter of minutes. We then slice and dice the results to understand how well is it classifying. Along the way, we build a common machine learning pipeline, which is repurposed throughout the book. Bonus: we hear from **Jeremy Howard**, co-founder of fast.ai, on how hundreds of thousands of students use transfer learning to jumpstart their AI journey.

[**Chapter 4 - Building a Reverse Image Search Engine: Understanding Embeddings**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-4) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch04.html) | [Figures](figures/chapter-4)

Like Google Reverse Image Search, we explore how one can use embeddings—a contextual representation of an image to find similar images in under ten lines. And then the fun starts when we explore different strategies and algorithms to speed this up at scale, from thousands to several million images, and making them searchable in microseconds.

[**Chapter 5 - From Novice to Master Predictor: Maximizing Convolutional Neural Network Accuracy**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-5) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch05.html) | [Figures](figures/chapter-5)

We explore strategies to maximize the accuracy that our classifier can achieve, with the help of a range of tools including TensorBoard, What-If Tool, tf-explain, TensorFlow Datasets, AutoKeras, AutoAugment. Along the way, we conduct experiments to develop an intuition of what parameters might or might not work for your AI task.

[**Chapter 6 - Maximizing Speed and Performance of TensorFlow: A Handy Checklist**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-6) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch06.html) | [Figures](figures/chapter-6)

We take the speed of training and inference into hyperdrive by going through a checklist of 30 tricks to reduce as many inefficiencies as possible and maximize the value of your current hardware.

[**Chapter 7 - Practical Tools, Tips, and Tricks**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-7) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch07.html) | [Figures](figures/chapter-7)

We diversify our practical skills in a variety of topics and tools, ranging from installation, data collection, experiment management, visualizations, keeping track of the state-of-the-art in research all the way to exploring further avenues for building the theoretical foundations of deep learning.

[**Chapter 8 - Cloud APIs for Computer Vision: Up and Running in 15 Minutes**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-8) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch08.html) | [Figures](figures/chapter-8)

Work smart, not hard. We utilize the power of cloud AI platforms from Google, Microsoft, Amazon, IBM and Clarifai in under 15 minutes. For tasks not solved with existing APIs, we then use custom classification services to train classifiers without coding. And then we pit them against each other in an open benchmark, you might be surprised who won.

[**Chapter 9 - Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-9) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch09.html) | [Figures](figures/chapter-9)

We take our custom trained model to the cloud/on-premises to scalably serve from tens to millions of requests. We explore Flask, Google Cloud ML Engine, TensorFlow Serving, and KubeFlow, showcasing the effort, scenario, and cost-benefit analysis.

[**Chapter 10 - AI in the Browser with TensorFlow.js and ml5.js**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-10) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch10.html) | [Figures](figures/chapter-10)

Every single individual who uses a computer or a smartphone uniformly has access to one software program—their browser. Reach all those users with browser-based deep learning libraries including TensorFlow.js and ml5.js. Guest author **Zaid Alyafeai** walks us through techniques and tasks such as body pose estimation, generative adversarial networks (GANs), image-to-image translation with Pix2Pix and more, running not on a server but in the browser itself. Bonus: Hear from TensorFlow.js and ml5.js teams on how the projects incubated.

[**Chapter 11 - Real-Time Object Classification on iOS with Core ML**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-11) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch11.html) | [Figures](figures/chapter-11)

We explore the landscape of deep learning on mobile, with a sharp focus on the Apple ecosystem with Core ML. We benchmark models on different iPhones, investigate strategies to reduce app size and energy impact, dynamic model deployment, training on device, and how professional apps are built.

[**Chapter 12 - Not Hotdog on iOS with Core ML and Create ML**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-12) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch12.html) | [Figures](figures/chapter-12)

Silicon Valley’s Not Hotdog app (from HBO) is considered the “Hello World” of mobile AI, so we pay tribute by building a real-time version in not one, not two, but three different ways.

[**Chapter 13 - Shazam for Food: Developing Android Apps with TensorFlow Lite and ML Kit**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-13) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch13.html) | [Figures](figures/chapter-13)

We bring AI to Android with the help of TensorFlow Lite. We then look at cross-platform development using ML Kit (which is built on top of TensorFlow Lite) and Fritz to explore the end-to-end development life cycle for building a self-improving AI app. Along the way we look at model versioning, A/B testing, measuring success, dynamic updates, model optimization, and other topics. Bonus: We get to hear about **Pete Warden’s** (technical lead for Mobile and Embedded TensorFlow) rich experience in bringing AI to edge devices.

[**Chapter 14 - Building the Purrfect Cat Locator App with TensorFlow Object Detection API**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-14) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch14.html) | [Figures](figures/chapter-14)

We explore four different methods for locating the position of objects within images. We take a look at the evolution of object detection over the years, and analyze the tradeoffs between speed and accuracy. This builds the base for case studies such as crowd counting, face detection, and autonomous cars.

[**Chapter 15 - Becoming a Maker: Exploring Embedded AI at the Edge**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-15) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch15.html) | [Figures](figures/chapter-15)

Guest author Sam Sterckval brings deep learning to low-power devices as he showcases a range of AI-capable edge devices with varying processing power and cost including Raspberry Pi, NVIDIA Jetson Nano, Google Coral, Intel Movidius, PYNQ-Z2 FPGA, opening the doors for robotics and maker projects. Bonus: Hear from the **NVIDIA Jetson Nano team** on how people are building creative robots quickly from their open-sourced recipe book.

[**Chapter 16 - Simulating a Self-Driving Car using End-to-End Deep Learning with Keras**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-16) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch16.html) | [Figures](figures/chapter-16)

Using the photorealistic simulation environment of Microsoft AirSim, guest authors **Aditya Sharma** and **Mitchell Spryn** guide us in training a virtual car by driving it first within the environment and then teaching an AI model to replicate its behavior. Along the way, this chapter covers a number of concepts that are applicable in the autonomous car industry.

[**Chapter 17 - Building an Autonomous Car in Under an Hour: Reinforcement Learning with AWS DeepRacer**](https://github.com/practicaldl/Practical-Deep-Learning-Book/tree/master/code/chapter-17) | [Read online](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch17.html) | [Figures](figures/chapter-17)

Moving from the virtual to the physical world, guest author **Sunil Mallya** showcases how AWS DeepRacer, a miniature car, can be assembled, trained and raced in under an hour. And with the help of reinforcement learning, the car learns to drive on its own, penalizing mistakes and maximizing success. We learn how to apply this knowledge to races from the Olympics of AI Driving to RoboRace (using full-sized autonomous cars). Bonus: Hear from **Anima Anandkumar (NVIDIA)** and **Chris Anderson (founder of DIY Robocars)** on where the self-driving automotive industry is headed.

## How to Use this Repository

First off, welcome! We are happy that you have decided to use the book and the code to learn more about Deep Learning! We wish you the best for your journey forward. Here are a few things to keep in mind while using the repository.

- Code for each chapter is present in the [`code`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code) folder.
- There is a respective README in each chapter that provides chapter-specific instructions on how to proceed with the code, and what data to download.

Please follow [these](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=WzIRIt9d2huC) instructions to load the GitHub repo on Google Colab. Keep in mind that you will need access to your own Google Drive as we will be using data from a local system.

### Environment
We will use a `virtualenv` by the name of `practicaldl` throughout the book. The `requirements.txt` for this `virtualenv` are in the root directory. Help and instructions to install `virtualenv` are in the [Installation](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/FAQ.md#installation) section in the [FAQ](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/FAQ.md) document.

### Bug Reporting
Please file a issue according to [CONTRIBUTING](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/CONTRIBUTING.md) and we will investigate.

## About the authors
[**@AnirudhKoul**](https://twitter.com/AnirudhKoul) is a noted AI expert, UN/TEDx speaker and a former scientist at Microsoft AI & Research, where he founded Seeing AI, often considered the most used technology among the blind community after the iPhone. Anirudh serves as the Head of AI & Research at Aira, recognized by Time Magazine as one of the best inventions of 2018. With features shipped to a billion users, he brings over a decade of production-oriented Applied Research experience on PetaByte scale datasets. He has been developing technologies using AI techniques for Augmented Reality, Robotics, Speech, Productivity as well as Accessibility. His work in the AI for Good field, which IEEE has called ‘life-changing’, has received awards from CES, FCC, MIT, Cannes Lions, American Council of the Blind, showcased at events by UN, World Economic Forum, White House, House of Lords, Netflix, National Geographic, and lauded by world leaders including Justin Trudeau and Theresa May.

[**@SiddhaGanju**](https://twitter.com/SiddhaGanju), an AI researcher who Forbes featured in their 30 under 30 list, is a Self-Driving Architect at Nvidia. As an AI Advisor to NASA FDL, she helped build an automated meteor detection pipeline for the CAMS project at NASA, which ended up discovering a comet. Previously at Deep Vision, she developed deep learning models for resource constraint edge devices. Her work ranges from Visual Question Answering to Generative Adversarial Networks to gathering insights from CERN's petabyte-scale data and has been published at top-tier conferences including CVPR and NeurIPS. She has served as a featured jury member in several international tech competitions including CES. As an advocate for diversity and inclusion in technology, she speaks at schools and colleges to motivate and grow a new generation of technologies from all backgrounds.

[**@MeherKasam**](https://twitter.com/MeherKasam) is a seasoned software developer with apps used by tens of millions of users every day. Currently an iOS developer at Square, and having previously worked at Microsoft and Amazon, he has shipped features for a range of apps from Square’s Point of Sale to the Bing iPhone app. Previously, he worked at Microsoft, where he was the mobile development lead for the Seeing AI app, which has received widespread recognition and awards from Mobile World Congress, CES, FCC, and the American Council of the Blind, to name a few. A hacker at heart with a flair for fast prototyping, he’s won several hackathons and converted them to features shipped in widely used products. He also serves as a judge of international competitions including Global Mobile Awards and Edison Awards.

## Citation
Please cite us if you use our code.

```
@book{Koul2019PracticalDLBook,
  title={Practical Deep Learning for Cloud, Mobile and Edge: Real-World AI and Computer Vision Projects Using Python, Keras and TensorFlow},
  author={Koul, A. and Ganju, S. and Kasam, M.},
  isbn={9781492034865},
  url={https://www.oreilly.com/library/view/practical-deep-learning/9781492034858/},
  year={2019},
  publisher={O'Reilly Media, Incorporated}
}
```
