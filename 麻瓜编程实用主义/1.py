import os
path="E:/iphon同步"
files=os.listdir(path)


for f in files:
    if '37' in f and f.endswith('.JPG'):
        print('Found it  '+f)
    # else:
    #     print("can't find it")