"""
This script will split the data and labels between training and testing sets

@author: Nils Tijtgat (https://github.com/timebutt)
"""

import glob, os

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('/home/riccardo/darknet/data/train.txt', 'w')
file_test = open('/home/riccardo/darknet/data/test.txt', 'w')

# Current directory
images_dir = "/home/riccardo/darknet/images/"

# add the names of each of your classes
classes = ["cat", "dog", "car"]

print "Populating train and test files"
for cls in classes:
    # Directory for each separate class
    path_data = images_dir + cls + "/"

    counter = 1
    index_test = round(100 / percentage_test)
    for pathAndFilename in glob.iglob(os.path.join(path_data, "*.jpg")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        # Populate train.txt and test.txt
        if counter == index_test:
            counter = 1
            file_test.write(path_data + title + '.jpg' + "\n")
        else:
            file_train.write(path_data + title + '.jpg' + "\n")
            counter = counter + 1

print "Completed"
