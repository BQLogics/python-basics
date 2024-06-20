import os
directory= "IBM_intership"
parent_dir="D:/"
path=os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '%s' created" % directory)