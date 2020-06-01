# Code for Chapter 6: Maximizing Speed and Performance of TensorFlow: A Handy Checklist

We take the speed of training and inference into hyperdrive by going through a checklist of 30 tricks to reduce as many inefficiencies as possible and maximize the value of your current hardware. [Read online here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch06.html)

## Checklist

This chapter is meant to serve as a handy checklist of potential performance optimizations that we can make when building all stages of the deep learning pipelines, and useful throughout the book. Specifically, we will discuss optimizations related to data preparation, data reading, data augmentation, training, and finally inference. Some of the checklist items are accompanied by code samples below:

| Section | Guideline |
| :---: | :---: |
| Data Preparation | [Store as TF Records](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-6/storing-data-as-tfrecord.ipynb) |

### How to Use This Checklist

In business, an oft-quoted piece of advice is “You can't improve what you can't measure.” This applies to deep learning pipelines, as well. Tuning performance is like a science experiment. You set up a baseline run, tune a knob, measure the effect, and iterate in the direction of improvement. The items on the following checklist are our knobs— some are quick and easy, whereaswhile others are more involved.

To use this checklist effectively, do the following:
1. Isolate the part of the pipeline that you want to improve.
2. Find a relevant point on the checklist.
3. Implement, experiment, and observe if runtime is reduced. If not reduced, ignore change.
4. Repeat steps 1 through 3 until the checklist is exhausted.

Some of the improvements might be minute, some more drastic. But the cumulative effect of all these changes should hopefully result in faster, more efficient execution and best of all, more bang for the buck for your hardware.

You can view the checklist in [Markdown](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-6/Performance-Checklist.md), or download in [PDF](https://github.com/PracticalDL/Practical-Deep-Learning-Book/blob/master/code/chapter-6/Performance-Checklist.pdf) and keep it handy for future use.
