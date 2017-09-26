#Adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#Importing gzip https://docs.python.org/2/library/gzip.html
import gzip

f = gzip.open('t10k-images-idx3-ubyte.gz', 'rb')

#File_content stores file data
file_content = f.read()
#Printing file data to console
print(file_content)