# MNIST Reader
This repository contains solutions to the [MNIST data set problem sheet](https://emerging-technologies.github.io/problems/digits.html) completed as part of my course work for the module [Emerging Technologies](https://emerging-technologies.github.io/).
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie/) in the Department of Computer Science and Applied Physics for the course [B.S.c. (Hons) in Software Developement.](https://www.gmit.ie/software-development/bachelor-science-honours-software-development) The lecturer is  [Dr. Ian McLoughlin](https://ianmcloughlin.github.io/).

## What is MNIST:
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets.  

The MNIST database of handwritten digits has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image. Additional information can be viewed [here](https://en.wikipedia.org/wiki/MNIST_database) and the MNIST database [website](http://yann.lecun.com/exdb/mnist/).

## How to run:
Download the repository and using the command console CD into the directory and type `python MNIST.py`.  
**Or**  
Download the repository and using the command console CD into the directory and launch jupyter notebook by typing `jupyter notebook` and in the browser window that pops up click on `MNIST.ipynb`. To run the code click inside the coding block and press shift enter.


**Note:** This repository does not include copies of the .gz files contained in the MNIST database, but can be downloaded from the [MNIST website](http://yann.lecun.com/exdb/mnist/). These files should be placed directly inside this project's folder before running the code.

**Prerequisites**:   
Python must be installed. Recommended version [3.6.1](https://www.python.org/downloads/release/python-361/).  
Short guide on how to install jupyter notebook can be viewed [here](http://jupyter.readthedocs.io/en/latest/install.html).

Keep in mind that due to the large number of items within each file, it may cause the program to run very slow depending on hardware.

## Exercises:
## 01. Read the data files
Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.
## 02. Output an image to the console
Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.  
![3rd train image](https://github.com/RicardsGraudins/MNIST-Reader/blob/master/Images/train-0002-4.PNG)
## 03. Output the image files as PNGs
Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format `train-XXXXX-Y.png` or `test-XXXXX-Y.png` where `XXXXX` is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be `train-04999-2.png`. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.  
![5-thousandth train image](https://github.com/RicardsGraudins/MNIST-Reader/blob/master/Images/train-4999-2.png)  

**Note:** It is possible to save all of the training set and testing set images using the code supplied in this repository however the images are not included inside this repository. If the code is run it will save 10,000 testing images and 60,000 training images inside the `Images` folder. A small sample of the testing set images can be viewed inside `SampleImages.zip` and here is a sample image of the testing set images if they are saved: ![test-set example](https://github.com/RicardsGraudins/MNIST-Reader/blob/master/Images/test-set-example.PNG)
