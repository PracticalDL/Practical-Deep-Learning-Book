# Code for Chapter 14: Building the Purrfect Cat Detector App with TensorFlow Object Detection API

We explore four different methods for locating the position of objects within images. We take a look at the evolution of object detection over the years, and analyze the tradeoffs between speed and accuracy. This builds the base for case studies such as crowd counting, face detection, and autonomous cars. [Read online here.](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch14.html)

## Code

Please use this code in conjunction with the [chapter](https://learning.oreilly.com/library/view/practical-deep-learning/9781492034858/ch14.html).

You’ll want to initialize your terminal with the `practicaldl` virtual environment before running any of the scripts in this chapter.

`$ source {path to practicaldl virtualenv}/bin/activate`

- Step 1:

    Please clone the [`tensorflow/models/`](https://github.com/tensorflow/models/) repository and move all the files from the current folder to the `models/research/object_detection` directory.

    ```
    git clone https://github.com/tensorflow/models.git && cd models/research
    ```

    Apart from the scripts provided in the [`tensorflow/models/research/object_detection`](https://github.com/tensorflow/models/tree/master/research/object_detection) repo, we have provided the following additional scripts:

    1. [`xml_to_csv.py`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/xml_to_csv.py): Combines all the XML annotations to one CSV file. This file is based on utilize **Dat Tran's** [script](https://github.com/datitran/raccoon_dataset) and is modified to suit the example at hand.
    2. [`pipeline.config`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/pipeline.config): Outlines the architecture of the model we will train. You can choose to use any model with its own `pipeline.config` file, which should be available when you download the model itself.
    3. [`generate_tfrecord.py`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/generate_tfrecord.py): This file generates the `tfrecord` files for the train and test splits. The code has been built according to the [instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md) from TensorFlow and we utilize **Dat Tran's** [script](https://github.com/datitran/raccoon_dataset) too. You will need to edit the file to reflect the absolute path of the repository and add information about your labelmap. All the user defined edits are at the top of the script.
    4. [`label_map.pbtxt`](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/label_map.pbtxt): Provides the label and identifier mappings for all of our classes. Please edit according to the classes you are training for.

    Please move all the above scripts to the `models/research/object_detection` folder to proceed. The directory structure outlining the main files that we will be using should look something like this:

    ```
    models/research/object_detection
    |___images/
    |___ssd_mobilenet_v2_coco_2018_03_29/
    |___export_inference_graph.py
    |___export_tflite_ssd_graph.py
    |___generate_tfrecord.py
    |___label_map.pbtxt
    |___test_labels.csv
    |___test.tfrecord
    |___train_labels.csv
    |___train.tfrecord
    |___xml_to_csv.py
    ```

    ```
    models/research
    |___add_protoc.sh
    ```

- Step 2:

    Before proceeding with the code make sure the environment is set correctly. To ensure this, we first need to update `PYTHONPATH` as follows:

    ```
    export PYTHONPATH="${PYTHONPATH}:`pwd`:`pwd`/slim"
    ```
    
    Second, we will use the [add_protoc.sh](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/add_protoc.sh) script. From `models/research` run:

    ```
    chmod +x add_proto.sh
    ./add_protoc.sh
    ```

- Step 3:

    At the same location of `models/research` please run:

    ```
    python setup.py build
    python setup.py install
    ```

    To test if everything works fine, run the [`object_detection_tutorial.ipynb`](https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb) notebook.

The setup is all done, let's move onto the data!

## Data

- Step 1: Data Collection

    We will be collecting our own data for this chapter. Go crazy collecting images of any object in your surroundings! Divide the images amongst a training and test set and place at the following locations: `object_detection/images/train` and `object_detection/images/test`.

- Step 2: Data Labling

    Use the [LabelImg](https://github.com/tzutalin/labelImg) tool to annotate the bounding boxes for your dataset. Each image that you annotate will have its own XML file that serves as its label. Here is an example of the image and corresponding [XML file](https://github.com/practicaldl/Practical-Deep-Learning-Book/blob/master/code/chapter-14/data/pascal-voc-sample.xml) generated.

- Step 3: Data Conversion

    Here we will combine all the XML files to a single CSV file using the `xml_to_csv.py` script and then convert to `tfrecord` files using the `generate_tfrecord.py` script.

    You will find samples of the data, annotations, and the TFRecord files that we used in the current directory.

- Step 4: Download the model

    Download your model of choice from TensorFlow's [Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). For the current example we will be using the [SSD MobileNetv2](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz) model. Unzip the model into `models/research/object_detection`. It should contain the following:

    ```
    $ ls ssd_mobilenet_v2_coco_2018_03_29
    checkpoint                      model.ckpt.data-00000-of-00001  model.ckpt.meta                 saved_model
    frozen_inference_graph.pb       model.ckpt.index                pipeline.config
    ```

    Repeat the test to make sure the model works fine by plugging it into the [`object_detection_tutorial.ipynb`](https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb) notebook.
