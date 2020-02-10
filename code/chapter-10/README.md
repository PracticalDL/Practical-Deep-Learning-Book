# Code for Chapter 10: AI in the Browser with TensorFlow.js and ml5.js

Every single individual who uses a computer or a smartphone uniformly has access to one software program—their browser. Reach all those users with browser-based deep learning libraries including TensorFlow.js and ml5.js. Guest author **Zaid Alyafeai** walks us through techniques and tasks such as body pose estimation, generative adversarial networks (GANs), image-to-image translation with Pix2Pix and more, running not on a server but in the browser itself. Bonus: Hear from TensorFlow.js and ml5.js teams on how the projects incubated. [Read online here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch10.html)

## Code

Go through the code in the following order:

1. [Running Pretrained Models using TensorFlow.js](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/mobilenet-example): We load a pretrained MobileNet model and run it in the browser.
2. [Teachable Machine](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/teachable-machine): We take it up a notch and train our own models directly in the browser using input from the webcam.
3. [Running Pretrained Model using ml5.js](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/ml5js): ml5.js is a higher abstraction of TensorFlow.js that makes it easy to use existing pre-trained deep learning models in a unified way, with a minimal number of lines of code. The package comes with a wide range of built-in models, ranging from image segmentation to sound classification to text generation, some of which we will use in this example.
4. [Running on a livestream from a webcam using p5js](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/p5js-webcam): p5.js is a library that works nicely in conjunction with ml5.js and makes it super easy to make model predictions in real-time using a live video stream.
5. [PoseNet](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/posenet): We explore the computer vision task of pose estimation.
6. [Pix2Pix](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/Pix2Pix): We dive in sci-fi and examine image translation.

### Scripts

[`benchmark/index.html`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-10/benchmark) is a script that benchmarks the system.

## Frameworks

We will need to install some libraries that allow us to train and test in the browser. These include `TensorFlow.js`, `ml5.js` and `p5.js`.
