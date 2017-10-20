#Adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#Importing gzip https://docs.python.org/2/library/gzip.html
import gzip

f = gzip.open('train-images-idx3-ubyte.gz', 'rb')

#File_content stores file data
file_content = f.read()
#Printing file data to console
#print(file_content)

#Reading first byte
firstbyte = f.read(1)
print("The first byte is: ", firstbyte)

#Reading first four bytes
magicNum = f.read(4)

#b'\x00\x00\x08\x03'
print("The magic number in bytes is: ", magicNum)

#Binary = 2051
magicNum = int.from_bytes(magicNum, 'big')
print("The magic number is: ", magicNum)

#ref. https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
import os

path = "Images/"
dir = os.path.dirname(path)

if not os.path.exists(dir):
	os.makedirs(dir)