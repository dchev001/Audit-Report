#!/usr/bin/python

# Import modues
import os, datetime, shutil, csv
from os import path
from datetime import datetime

# Input folder & output folder
src = os.path.join(os.getcwd(), "launchPad")
dstDir = os.path.join(os.getcwd(), "Result")

# Change directory to input
os.chdir(src)

# List the input files
lst = os.listdir(os.getcwd())

# Create the timestamp for the file name
currTime = datetime.now()
shortDate = currTime.strftime("%Y%m%d")
longDate = currTime.strftime("%b %d %Y %I:%M:%S%p")

# Create full audit file
fileName = shortDate+"_Full Audit Report (gen. "+longDate+").txt"
f = open(fileName, "w+")

# Move file to destination
shutil.move(fileName, dstDir)

# Iterate through the files
for x in lst:
    # Write current file title to audit report
    f.write(x+"\n")
    
    # Open the current file
    curr = open(x, "r")
    line = curr.readline()
    while line:
        line = curr.readline()
        f.write(line.lstrip('"').rstrip('"'))
        
    f.write("\n")
        
    
    # close current file
    curr.close()

# Close Full audit file
f.close()


