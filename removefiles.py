import time
import shutil
import os

path = input("Enter the folder path")
days = 30

days = time.time()

doesExist = os.path.exists(path)

if(doesExist == True):
    flcheck = os.path.exists(path)
    folwalk = os.walk(path)

    crtime  = os.stat(path).st_crtime

    if(crtime >= days):
        os.remove(path)
        shutil.rmtree()
else:
    print("Path does not exist")