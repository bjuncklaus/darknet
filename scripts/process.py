"""
This script will split the data and labels between training and testing sets

@author: Nils Tijtgat (https://github.com/timebutt)
"""

import glob, os

# Current directory
current_dir = "/home/riccardo/darknet/images/"

# Directory where the data will reside, relative to 'darknet.exe'
path_data = "/home/riccardo/darknet/images/"

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('/home/riccardo/darknet/data/train.txt', 'w')
file_test = open('/home/riccardo/darknet/data/test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.jpg' + "\n")
    else:
        file_train.write(path_data + title + '.jpg' + "\n")
        counter = counter + 1