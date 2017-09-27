# MNIST Reader
This repository contains solutions to the [MNIST data set problem sheet](https://emerging-technologies.github.io/problems/digits.html) completed as part of my course work for the module [Emerging Technologies](https://emerging-technologies.github.io/).
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie/) in the Department of Computer Science and Applied Physics for the course [B.S.c. (Hons) in Software Developement.](https://www.gmit.ie/software-development/bachelor-science-honours-software-development) The lecturer is  [Dr. Ian McLoughlin](https://ianmcloughlin.github.io/).

## How to run:
Download the repository and using the command console CD into the directory then launch jupyter notebook by typing `jupyter notebook` and select `MNIST.py`.

**Note:** This repository does not include copies of the .gz files contained in the MNIST database, but can be downloaded from the [MNIST website](http://yann.lecun.com/exdb/mnist/). These files should then be placed directly inside this project's folder.

Short guide on how to install jupyter notebook can be viewed [here](http://jupyter.readthedocs.io/en/latest/install.html).

Keep in mind that due to the large number of items within each file, it may cause the program to run very slow especially when reading the test images file.

## Exercises:
## 01. Read the data files
Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.
## 02. Output an image to the console
Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.  
![3rd train image](https://github.com/RicardsGraudins/MNIST-Reader/blob/master/Images/train-0002-4.PNG)
## 03. Output the image files as PNGs
Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format `train-XXXXX-Y.png` or `test-XXXXX-Y.png` where `XXXXX` is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be `train-04999-2.png`. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.  
![5-thousandth train image](https://github.com/RicardsGraudins/MNIST-Reader/blob/master/Images/train-4999-2.png)
