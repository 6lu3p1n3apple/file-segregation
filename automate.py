import os
import shutil

source="C:/Users/mahaj/Downloads"
destination="C:/Users/mahaj/Downloads/Documents"

files=os.listdir(source)

for file in files:
    name,ext=os.path.splitext(file)
    if ext==".pdf":
        continue
    if ext in [".pdf"]:
        path1=source+"/"+file
        path2=destination
        path3=destination+"/"+file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)
