#!/usr/bin/python

#import modules
import os
import zipfile
import rarfile
from os import path


# Input folder
src = os.path.join(os.getcwd(), "launchPad")

for root, dirs, files in os.walk(src, topdown=True):
	for name in files:
                if zipfile.is_zipfile(name):
                        filePath = os.path.join(root, name)
		        #fpath = filePath[len(src):]
                        print(filePath)

                if rarfile.is_rarfile(name):
                        filePath = os.path.join(root, name)
                        print(filePath)


# need to keep working on this program
