# Chapter 6 - Maximizing Speed and Performance of TensorFlow: A Handy Checklist

Note: All images in this directory, unless specified otherwise, are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

## Figure List

| Figure number | Description | Notes |
|:---|:---|:---|
| [6-1](1-gpu-starvation.png?raw=true) | GPU starvation, while waiting for CPU to finish preparing the data | |
| [6-2](2-nvidia-smi.png?raw=true) | Terminal output of nvidia-smi highlighting the GPU utilization | |
| [6-3](3-tensorboard-idle-gpu-cpu.png?raw=true) | Profiler’s timeline in TensorBoard shows an idle GPU while the CPU is processing as well as CPU idling while the GPU is processing | |
| [6-4](4-dali-architecture.png?raw=true) | The NVIDIA DALI pipeline | |
| [6-5](5-time-per-epoch-vs-gpu-util.png?raw=true) | Effect of varying batch size on time per epoch (seconds) as well as on percentage GPU utilization (Log scales have been used for both X- and Y-axes.) | |
| [6-6](6-plot-loss.png?raw=true) | A graph showing the change in loss as the learning rate is increased | |
| [6-7](7-plot-loss-change.png?raw=true) | A graph showing the rate of change in loss as the learning rate is increased | |
| [6-8](8-matrix-multiplication.png?raw=true) | A matrix multiplication for A x B operation with one of the multiplications highlighted | |
| 6-9 | The $400,000 NVIDIA DGX-2 deep learning system | |
| [6-10](https://arxiv.org/pdf/1605.07678.pdf) | Comparing different models for size, accuracy, and operations per second (adapted from “An Analysis of Deep Neural Network Models for Practical Applications” by Alfredo Canziani, Adam Paszke, and Eugenio Culurciello) | Page 2, Figure 2 |
| [6-11](https://arxiv.org/pdf/1907.09595.pdf) | Comparison of several mobile-friendly models in the paper “MixNet: Mixed Depthwise Convolution Kernels” by Mingxing Tan and Quoc V. Le | Page 9, Figure 7 |
| [6-12](12-quantization-line.png?raw=true) | Quantizing from a 0 to 1 32-bit floating-point range down to an 8-bit integer range for reduced storage space | |