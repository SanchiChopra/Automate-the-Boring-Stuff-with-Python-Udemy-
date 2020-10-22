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
