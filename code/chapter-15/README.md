# Code for Chapter 15: Becoming a Maker: Exploring Embedded AI at the Edge

Guest author Sam Sterckval brings deep learning to low-power devices as he showcases a range of AI-capable edge devices with varying processing power and cost including Raspberry Pi, NVIDIA Jetson Nano, Google Coral, Intel Movidius, PYNQ-Z2 FPGA, opening the doors for robotics and maker projects.

## Code

Go through the code in the following order:

1. [benchmark.py](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-15/benchmark.py): This script will make a prediction on the [cat.jpg](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-15/images/cat.jpg) file 250 times and measure how long it takes to run.
2. [benchmark_tflite.py](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-15/benchmark_tflite.py): This script will make a prediction on the [cat.jpg](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-15/images/cat.jpg) file 250 times using a TensorFlow Lite model and measure how long it takes to run.
3. [benchmark_edgetpu.py](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-15/benchmark_edgetpu.py): This script can make a prediction on the [cat.jpg](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-15/images/cat.jpg) file 250 times on a Raspberry Pi and measure how long it takes to run.
4. [benchmark_jetson.py](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-15/benchmark_jetson.py): This script can make a prediction on the [cat.jpg](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-15/images/cat.jpg) file 250 times on a Jetson Nano and measure how long it takes to run.

Please note that all the examples on edge devices showcased above work only on `TensorFlow 1.x` as of now.
