from myCourses import l1
import os
path = 'C:\\Users\\user-name\\Desktop\\Moodle'  #path of your Desktop with the directory Moodle specified
                                                #change the directory name as per your wish


if not os.path.exists(path):
    os.makedirs(path)
for i in l1:
    if not os.path.exists(path + "\\\\" + i):
        os.makedirs(path + "\\\\"+ i)
    
