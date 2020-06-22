#!/usr/bin/python

import os, datetime, shutil
from os import path
from datetime import datetime


dataroom = os.path.join(os.getcwd(), "launchPad")
localfolder = os.path.join(os.getcwd(), "localfolder")
dstDir = os.path.join(os.getcwd(), "Result")

currTime = datetime.now()
shortDate = currTime.strftime("%Y%m%d")
longDate = currTime.strftime("%b %m %Y %I:%M:%S%p")

fileName = shortDate+"_SX Entity_Moved Files (gen. "+longDate+").txt"
f = open(fileName, "w+")
shutil.move(fileName, dstDir)

for root, dirs, files in os.walk(dataroom, topdown=True):
	for name in files:
		filePath = os.path.join(root, name)
		fpath = filePath[len(dataroom):]
		f.write(fpath + '\n')


		for root, dirs, files in os.walk(localfolder, topdown=True):
			for other in files:
				if name == other:
					filePath2 = os.path.join(root, other)
					fpath2 = filePath2[len(localfolder):]
					f.write(fpath2 + '\n')
		f.write('\n')

f.close()
