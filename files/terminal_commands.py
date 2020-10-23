import os
os.sep  # displays the separator: \\
os.getcwd()  # returns the current working directory

# change the current working directory
os.chdir('c:\\')
os.getcwd()  # returns c:\\

os.path.abspath('spam.png')
# above gives the absolute file path for spam.png - C:\\Program...

os.path.abspath('..\\..\\spam.png')
# go to the current folder's parent folder and its parent folder again and find spam.png

os.path.isabs('..\\..\\spam.png')  # returns false since input path is relative

# returns true since input path is absolute
os.path.isabs('c:\\folder\\folder')


os.path.relpath('a', 'b')  # gives relative path from path b to path a
os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
# outputs: folder2\\spam.png

os.path.dirname('c:\\folder1\\folder2\\spam.png')
# returns - c:\\folder1\\folder2

os.path.basename('c:\\folder1\\folder2\\spam.png')
# outputs - spam.png, i.e., the part after the final \\

os.path.basename('c:\\folder1\\folder2')
# returns folder2


os.path.exists('c:\\folder1\\folder2\\spam.png')
# returns false since there exists no such path

os.path.isfile('c:\\folder1\\folder2\\spam.png')
# true


os.path.isfile('c:\\folder1\\folder2')
# false


os.path.isdir('c:\\windows\\system32\\calc.exe')
# false

os.path.isdir('c:\\windows\\system32')
# true

os.path.getsize('c:\\windows\\system32\\calc.exe')
# returns 918528 type of number

os.listdir('c:\\automatebook')
# returns all files and folders names that are inside the dir name we passed

os.makedirs('c:\\delicious\\waffles')
# creates a folder delicious in the root folder and another folder waffles inside delicious
