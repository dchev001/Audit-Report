#!/usr/bin/python

import os
import datetime
import time
import shutil
from datetime import datetime
from os import path


def main():

    src = os.path.join(os.getcwd(), "launchPad")
    dstDir = os.path.join(os.getcwd(), "Result")

    currTime = datetime.now()
    shortDate = currTime.strftime("%Y%m%d")
    longDate = currTime.strftime("%b %m %Y %I:%M:%S%p")

    fileName = shortDate+"_SX Entity_List files (gen. "+longDate+").txt"
    f = open(fileName, "w+")
    shutil.move(fileName, dstDir)
 
    for root, dirs, files in os.walk(src, topdown=True):
        for name in files:
            filePath = os.path.join(root, name)
            fpath = filePath[len(src):]
            f.write(fpath + '\n')

    f.close()

    
if __name__ == "__main__":
    main()
