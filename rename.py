#!/usr/bin/python

# import modules
import os, sys, getopt
from os import path

def main(argv):
    # old & new text
    oldText = ''
    newText = ''
    
    # Check command line 
    try:
        opts, args = getopt.getopt(argv, "ho:n:", ["oldText=", "newText="])
    except getopt.GetoptError:
        print("rename.py -o <oldText> -n <newText>")
        sys.exit(2)

    # Check & set flags
    for opt, arg in opts:
        if opt == '-h':
            print("rename.py -o <oldText> -n <newText>")
            sys.exit()
        elif opt in ("-o", "--oldText"):
            #print("Opt: ", opt)
            oldText = arg
        elif opt in ("-n", "--newText"):
            newText = arg

    # Set directory
    src = os.path.join(os.getcwd(), "launchPad")

    # Iterate through directory files
    for root, dirs, files in os.walk(src, topdown=True):
        for name in files:

            # if old or new text is null
            if not oldText or not newText:
                break
            else:
                # Replace old with new text
                newName = name.replace(oldText, newText)

                # Join the old file with root
                oldFileName = os.path.join(root, name)
                print("Old: ", oldFileName)

                # Join the new file with root
                newFileName = os.path.join(root, newName)
                print("New: ", newFileName)
                
                # to rename the file, FINAL
                os.rename(oldFileName, newFileName)

    print("Old Text: ", oldText)
    print("New Text: ", newText)

# main function    
if __name__ == "__main__":
    main(sys.argv[1:])
