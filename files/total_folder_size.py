# find total size of all files present inside a folder

import os
totalsize = 0
for filename in os.listdir('c:\\Users\\Sanchi'):
    if not os.path.isfile(os.path.join('c:\\Users\\Sanchi', filename)):
        continue
    totalsize = totalsize + \
        os.path.getsize(os.path.join('c:\\Users\\Sanchi', filename))
print(totalsize)
