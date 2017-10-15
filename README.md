![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

#Darknet#
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).


# Training
NOTE: I have only started writing this guide for myself. It is probably not clear and surely not complete. This is at the moment just to help me keep track of what steps I am doing to train yolo, as I am sure the majority of you have seen how complicated it can be. If I get it to work, I will try to keep expanding on this, and make a very clear guide which will hopefully help out. I am using this for a university project.

I am using the following to help me understand the training process:
- [How to train YOLOv2 to detect custom objects](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/) by [Nils Tijtgat](https://github.com/timebutt)
- [Start Training YOLO with Our Own Data](http://guanghan.info/blog/en/my-works/train-yolo/) by [Guanghan](https://github.com/Guanghan)
- [Yolo-v2 Windows and Linux version](https://github.com/AlexeyAB/darknet) by [Alexey](https://github.com/AlexeyAB)

## Prerequisite
- [Darknet](https://github.com/pjreddie/darknet)
- [CUDA](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- [cuDNN v7.0 Runtime Library](https://developer.nvidia.com/rdp/cudnn-download), install [instructions](http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)
- [Anaconda](https://www.anaconda.com/download/#linux) for Python 2.7

## Gather & format data
I have just started taking photos on my own as most datasets/databases online did not have images which I wanted, or the download were too large. I used my  phone to take photos, however the smallest photos I could take were 3264\*1836, and their names were not as wanted, so I did the renamed them, and resized them.

### Batch rename images:
- Install PyRenamer `sudo apt-get install pyrenamer`
- Open it: `pyrenamer`
- On the patterns tab, select all images, then use the patters to highlight which part you want changed, and replace it [ADD EXAMPLE]

### Batch resize images:
- Install Imagemagick: `sudo apt-get install imagemagick`
- Resize keeping aspect ratio: `mogrify -resize 640x360 *.jpg`

## Labeling
- In the home directory, clone [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool.git): `git close https://github.com/puzzledqs/BBox-Label-Tool.git`
- Empty the `Images/001` directory and place all your images for one class inside it
- Empty the `Labels/001` directory, where the text files will be saved
- Create incrementing folders (002, 003, ...) for each class, within the Images and Labels folder
NOTE: You can also open main.py and change the directories to your own.
- Open main: `python main.py`
NOTE: if this does not work, check if python is the default or Anaconda version when opened. If it is the defaults version, open .bachrc from the home directory (using either nano, vim, Atom, etc..), and add at the very end `export PATH=~/anaconda2/bin:$PATH`, then in the command line type `source .bashrc`. Try to open main now, it should work.
- Label every image, check [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool.git) repo for info. (will take some time)

### Converting labels
- Download [convert.py](https://github.com/Guanghan/darknet/tree/master/scripts), written by [Guanghan](https://github.com/Guanghan)
- Move convert.py to `darknet/scripts`
- Change the paths to your own
- Run `python convert.py` from the scripts directory
