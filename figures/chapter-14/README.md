# Chapter 14 - Building the Purrfect Cat Locator App with TensorFlow Object Detection API

Note: All images in this directory, unless specified otherwise, are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

## Figure List

| Figure number | Description | Notes |
|:---|:---|:---|
| [14-1](1-havahart-sprinkler.jpg) |  Building an AI cat sprinkler system, like this Havahart Spray Away Motion Detector | |
| [14-2](2-dog-baby-google-object-detection.png) | Running a familiar photo on Google’s Vision AI API to obtain object detection results | |
| [14-3](3-cat-detection-juypter.png) | Object detection prediction in the ready-to-use Jupyter Notebook from the TensorFlow Models repository | |
| [14-4](4-cat-inference-android.jpg) | Running a real-time object detector model on an Android device | |
| [14-5](5-simpsons-new-project.png) | Creating a new Object Detection project in CustomVision.ai | |
| [14-6](6-custom-vision-draw-bounding-box.png) | Dashboard with bounding box and class name | |
| [14-7](7-map-vs-num-images-per-character.png) | Measuring improvement in percent mean average precision with increasing number of images per class | |
| [14-8](8-simpsons-annotated.png) | Detected Simpsons characters with the final model, represented by US congress members of the same first name (see note at the beginning of this section) | |
| [14-9](https://arxiv.org/pdf/1908.03673.pdf) | A timeline of different object detection architectures (image source: Recent Advances in Deep Learning for Object Detection by Xiongwei Wu et al.) | Page 3, Figure 2 |
| [14-10](https://arxiv.org/pdf/1611.10012.pdf) | The effect of object detection architecture as well as the backbone architecture (feature extractor) on the percent mean average precision and prediction time | Page 8, Figure 2 |
| [14-11](11-iou.png) | A visual representation of the IoU ratio | |
| [14-12](12-higher-iou.png) | IoU illustrated; predictions from better models tend to have heavier overlap with the ground truth, resulting in a higher IoU | |
| [14-13](13-cat.png) | Using NMS to find the bounding box that best represents the location of the object in an image | |
| [14-14](14-objects-variety.jpg) | Photographs of objects taken in a variety of different settings to train an object detector model | |
| [14-15](15-creative-photos.png) | Some creative photographs taken during the process of building a diverse currency dataset | |
| [14-16](16-labelimg-open-dir.png) | Click the Open Dir button and then select the directory that contains the training data | |
| [14-17](17-cat-rectbox.png) | Select the Create RectBox from the panel on the left to make a bounding box that covers the cat | |
| [14-18](18-cat-labels.png) | Each image is accompanied by an XML file that contains the label information and the bounding box information | |
| [14-19](19-hair-color.png) | Colorizing hair with ModiFace app by accurately mapping the pixels belonging to the hair | |
| [14-20](20-self-driving-segmentation.png) | Image segmentation performed on frames from a dashcam (CamVid dataset) | |
| [14-21](https://www.geekwire.com/2016/microsoft-building-smart-fridge-not-smart-grocery-shoppers-like/) | Detected objects along with their classes from the SmartDeviceBox refrigerator| |
| [14-22](https://news.mongabay.com/2019/03/combining-artificial-intelligence-and-citizen-science-to-improve-wildlife-surveys/) | An aerial photograph of wildebeest taken from a small survey airplane | |
| [14-23](https://www.flickr.com/photos/sebadella/8509366052) | The 2013 Kumbh Mela, as captured by an attendee | Image credit: [Seba Della y Sole Bossio](https://www.flickr.com/photos/sebadella/), used under [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) |
| [14-24](24-seeingai.png) | Face detection feature on Seeing AI | |
| [14-25](https://blogs.nvidia.com/blog/2019/08/21/drive-labs-autonomous-vehicle-ride/) | Detecting traffic lights and signs on a self-driving car using the NVIDIA Drive Platform (image source)| |