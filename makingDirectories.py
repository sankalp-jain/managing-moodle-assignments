from myCourses import l1
import os
path = 'C:\\Users\\sankalpjain\\Desktop\\Moodle'


if not os.path.exists(path):
    os.makedirs(path)
for i in l1:
    if not os.path.exists(path + "\\\\" + i):
        os.makedirs(path + "\\\\"+ i)
    
