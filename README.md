# Darknet
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

<p align="center"><img src="http://pjreddie.com/media/files/darknet-black-small.png" height="300"></p>



# Training
NOTE: I have started writing this guide for a thesis project, and not everything may be yet clear or complete. I will try to keep expanding on this, and make a very clear guide which will hopefully help out. 

I used the following to help me understand the training process:
- [How to train YOLOv2 to detect custom objects](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/) by [Nils Tijtgat](https://github.com/timebutt)
- [Start Training YOLO with Our Own Data](http://guanghan.info/blog/en/my-works/train-yolo/) by [Guanghan](https://github.com/Guanghan)
- [Yolo-v2 Windows and Linux version](https://github.com/AlexeyAB/darknet) by [Alexey](https://github.com/AlexeyAB)

## Shortcuts
1. [Prerequisites](#prerequisites)
2. [Gather & format data](#1---gather--format-data)
3. [Labelling](#2---labelling)
4. [Creating train/test sets](#3---creating-traintest-sets)
5. [Configuration files](#4---configuration-files)
6. [Training](#5---training)
7. [Testing](#6---testing)
8. [Additional Notes](#additional-notes)

## TO DO
- Better explanation of prerequisites and installattion instructions
- Better explanation of training multiple classes
- Add more solutions to common issues
- Add more example images

## Prerequisites
- Ubuntu 16.04 or other Linux distribution
- Linux gcc compiler and toolchain, acquired from development tools of your Linux distribution
- A GPU of compute capability 3.0 or higher, check with [NVIDIA](https://developer.nvidia.com/cuda-gpus)
- [Darknet](https://github.com/pjreddie/darknet)
- [CUDA](https://developer.nvidia.com/cuda-downloads) 8.0 or 9.0. Install [instructions](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- [cuDNN v7.0 Runtime Library](https://developer.nvidia.com/rdp/cudnn-download), will require free NVIDIA dev team membership. Install [instructions](http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)
- [Anaconda](https://www.anaconda.com/download/#linux) for Python 2.7

NOTE: OpenCV can also be optionally installed.

## 1 - Gather Data
If you already have data from a dataset/database and it is in the correct format, skip to [step 2](https://github.com/RiccardoGrin/darknet#2---labeling). <br /> 

Though there are many image datasets/databases online, I could not find the images which I wanted, or these were part of a very large set, or the download was simply too large. Therefore, I just used my  phone to take photos. However the smallest photos I could take were 3264\*1836, and their names were not as desired. From research, apparently at least 250 different images are needed for each class. Taking 250 photos can take some time and creativity, therefore I took only half, and did some image augmentation (flipping, rotating, etc...) to get all 250 images. <br />
NOTE: Much better results will be achieved by get the 250 images or more, without applying any augmentation, as there will be more difference between the images. Thus image augmentation should only really be used to increase the set, to further improve the classification accuracy, though it will not be as large an increase as using original iamges.

Both Pre-processing and image augmentation steps will require Imagemagick, which is a free and open-source software suite used for formatting images. Install it using: `sudo apt-get install imagemagick`

## 2 - Pre-processing
Darknet requires the images to be in .jpg format, and of course, the smaller the images, the less computation is required. Thus, if your images are also large, make sure to resize them to something below 640\*640 pixels. 

### 2.1 - Batch convert images format (eg .png to .jpg):
- Travel to folder with images to convert via terminal
- Convert image format: `mogrify -format jpg *.png`

### 2.2 - Batch resize:
- Travel to the folder containing all image to be resized using the terminal
- Resize keeping aspect ratio: `mogrify -resize 640x360 *.jpg`

### 2.3 - Batch rename:
- Install PyRenamer `sudo apt-get install pyrenamer`
- Open it: `pyrenamer`
- Travel to folder containng images from the left panel
- On the right preview panel, select/highlight all images by pressing `ctrl-a`
- In the "Original file name pattern" box, type ".jpg"
- In the "Renamed file name pattern" box, type "{num3}.jpg"
- Click on the Preview button to see changes to be made. This will rename all .jpg images to ascending numbers (000, 001, 002, etc...)
- Press the Rename button to complete

## 3 - Augmentation
Images may be augmented in order to expand the dataset with which you can work and train from. It might also be useful in creasting a validation or testing set, though as stated previously, it is always better to have new original images, rather than augmented ones. Not all the following steps are necessary, it depends on how many more images you want to create. 
NOTE: It is not always a great idea to flip images, as most thing are not usually found to be seen upside-down.

Copy and paste all images to be augmented in the same folder (these should be automatically renamed to img_name(copy).jpg). If you are intending to do multiple augmentations, images may need to be renamed to not have the '(copy)' text after their name.

### 3.1 - Batch flip:
- Flip all image copies from the terminal: `mogrify -flip *(copy).jpg`

### 3.2 - Batch flop:
- Flop all image copies from the terminal: `mogrify -flop *(copy).jpg`

### 3.3 - Batch rotate:
The angel can be changed from 90 degrees to whatever is desired. I believe the images get padded for non multiples of 90 degree rotations (not tested though).
- Rotate all image copies from the terminal by 90 degrees: `mogrify -rotate 90 *.jpg`

<p align="center">
  <img src="readme_images/rename_exp.jpg" width="700"><br>
</p>


## 2 - Labelling
To make the process easier, I have changed the orginal [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool.git) by [puzzledqs](https://github.com/puzzledqs), so that images would not need to be shifted from fodler to folder to get all the different scripts to work. Also I have made it so that you can open a file with the name of the class in the images folder.
- In the home directory, clone the revised BBox-Label-Tool: `git clone https://github.com/RiccardoGrin/BBox-Label-Tool`
- Open `main.py` in an editor (I personally prefer Atom)
- Change lines 109 and 123 to point to your 'images' and 'labels' folders respectively
- Create a folder within the 'images' folder, for each class, with the class name
- Collect each image from each class and place it in their respective folder
- Create a folder within the 'labels' folder, for each class, with the class name
- Open main: `python main.py`
- Label every image (will take some time)

NOTE: If you cannot open 'main.py', check if python is opened as the default or Anaconda version by opening it from the terminal by typing `which python`. If it is the defaults version, open `.bachrc` from the home directory using an edition (Atom, nano, vim, etc...), and add at the very end `export PATH=~/anaconda2/bin:$PATH`, then in the command line type `source .bashrc`. Try to open 'main.py' again.

<p align="center">
  <img src="readme_images/label_exp.jpg" width="700"><br>
</p>

### 2.1 - Converting labels
I have done some changes to the original [convert.py](https://github.com/Guanghan/darknet/tree/master/scripts), written by [Guanghan](https://github.com/Guanghan) while I was learning to use it.
- Download the revised version of [convert.py](https://github.com/RiccardoGrin/darknet/blob/master/scripts/convert.py)
- Move 'convert.py' to `darknet/scripts`
- Change the paths on lines 39, 40, and 45 to your own
- Add all your classes in the array on line 16
- Run `python convert.py` from the scripts directory

## 3 - Creating train/test sets
I have made some changes to the 'process.py' script, written by [Nils Tijtgat](https://github.com/timebutt)  as seen on his [guide](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/). This script creates a 'train.txt' and 'test.txt' files required for training and validation. I have made some changes to the script to make it easier to use for multiple classes.
- Download the revised version of [process.py](https://github.com/RiccardoGrin/darknet/blob/master/scripts/process.py)
- Move 'process.py' to `darknet/scripts`
- Set the percentage of images to be set as testing images
- Update the directory in which to create the train and test files on lines 13, 14
- Update the image directory on line 17
- Add all your classes in the array on line 20 (similar to convert.py)
- Run `python process.py` from the scripts directory

## 4 - Configuration files
- In the 'data' directory, create a `obj.names` file, where every line should be a different class names
- In the 'cfg' directory, create a `obj.data` file with the following text:
  ```
  classes = 1  
  train = data/train.txt  
  valid = data/test.txt  
  names = data/obj.names  
  backup = backup/
  ```
- Duplicate `yolo-voc.cfg`, and change the name to `obj.cfg`
    - line 3: set `batch=64`
    - line 4: set `subdivisions=8`
    - line 244: set `classes=1`
    - line 237: set `filters=30`, (calculated as `(classes + 5)*5`)
- Create a folder named `backup` in the main darknet directory
- Download [darknet19_488.conv.23](https://pjreddie.com/media/files/darknet19_448.conv.23), and save it into the 'cfg' directory

## 5 - Training
- Open the darknet Makefile and switch GPU and CUDNN to 1 (Make sure there are setup correctly, otherwise training will take forever)
- Run `make` if you have not done so already
- Run `./darknet detector train cfg/obj.data cfg/obj.cfg darknet19_448.conv.23`

This will save save a `.weights` files within the backup folder, initially every 100 iterations, till 1000 (not included), and then every 10000 after that. This used to be every 1000 after the first 1000 interations but it was changed. To change it back, edit line 136 in `exemples/detector.c` from 10000 to 1000.

Make sure to read the [explanation](https://github.com/AlexeyAB/darknet#when-should-i-stop-training) by [Alexey](https://github.com/AlexeyAB) on when to stop training.

## 6 - Testing
Test your newly trained algorithm by running the following with a new image:
`./darknet detector test cfg/obj.data cfg/obj.cfg obj1000.weights images/image.jpg`

## Additional notes
1. If the training is ever interrupted at any point, it can be continued by substituting the last saved `.weights` file from the backup folder, with `darknet19_448.conv.23`, in the training command
2. If you get an error like: `darknet: ./src/cuda.c:36: check_error: Assertion '0' failed.`
You can fix it by changing your ARCH (architecture) in the make file, to be appropriate for your GPU. Another simple way I found to temporarely solve it, is to just turn your computer off and on again.
