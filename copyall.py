'''
     This simple script copies all the directories and files from one directory to other directory..
     Sample output:
     python copyall.py C:\Users\WELCOME\Desktop\python E:\dd
     This will copies all the content from the source to destination..
     
'''

from distutils.dir_util import copy_tree
import sys

source_dest = sys.argv[1:]
if not len(source_dest) == 2:
    print("you should give source directory first and destination next")
    exit(1)

source = source_dest[0]
dest = source_dest[1]

copy_tree(source,dest)
