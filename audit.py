#!/usr/bin/python

# import modules
import os, datetime, shutil
from os import path
from datetime import datetime

# main function declaration
def main():
    # Input and output folders
    src = os.path.join(os.getcwd(), "launchPad")
    dstDir = os.path.join(os.getcwd(), "Result")

    # Change directory to input
    os.chdir(src)

    # List the input folders directory
    lst = os.listdir(os.getcwd())

    # Iterate through the input folders directory
    for x in lst:
        # Join the input folder to the path
        currDir = os.path.join(os.getcwd(), x)

        # Create the timestamp for the file name
        currTime = datetime.now()
        shortDate = currTime.strftime("%Y%m%d")
        longDate = currTime.strftime("%b %d %Y %I:%M:%S%p")

        # Create the file name for the current folder
        fileName = shortDate+"_"+x+"_Audit Report (gen. "+longDate+").xlsx"
        f = open(fileName, "w+")

        # Move file to destination
        shutil.move(fileName, dstDir)

        # Iterate the current directory of the input folder
        for root, dirs, files in os.walk(currDir, topdown=True):
            # Create a list, for sorting
            tempList = []

            # Iterate through the files
            for name in files:
                # Join file name to root
                filePath = os.path.join(root, name)
                fpath = filePath[len(currDir):]

                # Append file name to list
                tempList.append(fpath)

            # Sort the list
            tempList.sort()

            # Write the list to file
            for b in tempList:
                f.write("\"" + b + "\"\n")

        # Close file
        f.close()

# main function
if __name__ == "__main__":
    main()
