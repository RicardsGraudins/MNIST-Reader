#Importing gzip https://docs.python.org/2/library/gzip.html
import gzip
#Importing http://pillow.readthedocs.io/en/3.4.x/reference/Image.html
import PIL.Image as pil
#Importing numpy http://www.numpy.org/
import numpy as np
#Importing os https://docs.python.org/2/library/os.html
import os

#Reading labels, passing in file as parameter
def readLabelsFromFile(filename):
    #Ref. https://docs.python.org/3/whatsnew/2.6.html#pep-343-the-with-statement
    with gzip.open(filename, 'rb') as f:
        magicNum = f.read(4)
        magicNum = int.from_bytes(magicNum, 'big')
        print("The magic number is: ", magicNum)

        numLabels = f.read(4)
        numLabels = int.from_bytes(numLabels, 'big')
        print("The number of labels is: ", numLabels)

        #Add to list
        labels = [f.read(1) for i in range(numLabels)]
        labels = [int.from_bytes(label, 'big') for label in labels]
    return labels

print("Training set label file:")
print("------------------------")
trainLabels = readLabelsFromFile('train-labels-idx1-ubyte.gz')
print("\nTest set label file:")
print("------------------------")
testLabels = readLabelsFromFile('t10k-labels-idx1-ubyte.gz')

#Reading images, passing in file as parameter
def readImagesFromFile(filename):
    with gzip.open(filename, 'rb') as f:
        magicNum = f.read(4)
        magicNum = int.from_bytes(magicNum, 'big')
        print("The magic number is: ", magicNum)

        numImgs = f.read(4)
        numImgs = int.from_bytes(numImgs, 'big')
        print("The number of images is: ", numImgs)

        numRows = f.read(4)
        numRows = int.from_bytes(numRows, 'big')
        print("The number of rows is: ", numRows)

        numCols = f.read(4)
        numCols = int.from_bytes(numCols, 'big')
        print("The number of columns is: ", numCols)

        images = []
        for i in range(numImgs):
            rows = []
            for r in range(numRows):
                cols = []
                for c in range(numCols):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
    return images

print("\nTraining set image file:")
print("------------------------")
trainImages = readImagesFromFile('train-images-idx3-ubyte.gz')
print("\nTest set image file:")
print("------------------------")
testImages = readImagesFromFile('t10k-images-idx3-ubyte.gz')

#Output 3rd image in training set to console
def outputConsole():
    for row in trainImages[2]:
        for col in row:
            print('.' if col<= 127 else '#', end='')
        print()
        

#Saving the five-thousandth training image
def saveImage():
	path = "Images/"
	dir = os.path.dirname(path)
	if not os.path.exists(dir):
		os.makedirs(dir)
		
	img = pil.fromarray(np.array(trainImages[4999]))
	img = img.convert('RGB')
	img.show()
	#img.save('train-4999-2.png')
	img.save('Images/train-4999-2.png')
	print("Image saved.")
    
outputConsole()
saveImage()

#Saving all images from testImages/trainImages
def saveImages(image, name, index, label):
    path = "Images/%s-%05d-%d.png"
    img = pil.fromarray(np.array(image))
    img = img.convert('RGB')
    img.save(path % (name, index, label))

choice = input("Would you like to save all the test images? (yes/no)\n")
if (choice == "yes"):
    #Saving 10000 test images
    for i in range(len(testImages)):
        saveImages(testImages[i],'test', (i+1), testLabels[i])
    
choice2 = input("Would you like to save all the train images? (yes/no)\n")
if (choice2 == "yes"):
    #Saving 60000 training images
    for i in range(len(trainImages)):
        saveImages(trainImages[i],'train', (i+1), trainLabels[i])