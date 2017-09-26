#Adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#Importing gzip https://docs.python.org/2/library/gzip.html
import gzip

#f = gzip.open('train-images-idx3-ubyte.gz', 'rb')

#File_content stores file data
#file_content = f.read()
#Printing file data to console
#print(file_content)

#Reading first byte
#firstbyte = f.read(1)
#print(firstbyte)

#Reading first four bytes
#magicNum = f.read(4)

#b'\x00\x00\x08\x03'
#print(magicNum)

#Binary = 2051
#magicNum = int.from_bytes(magicNum, 'big')
#print("The magic number is:", magicNum)

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