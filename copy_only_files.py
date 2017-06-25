
'''
This script copy only files from one directory to other
'''
import sys
import os
import shutil

args = sys.argv[1:]

if not len(args) == 2:
  print("Type Destnination file 1st and source file 2nd and make sure both present")
  sys.exit(1)

Dest_dir = args[0]
Source_dir = args[1]
filenames = os.listdir(Source_dir)

def copy_to(abs_path,Dest_dir):
  if not os.path.exists(Dest_dir):
    os.mkdir(Dest_dir)

  shutil.copy(abs_path,Dest_dir)

for fname in filenames:
  file_path = os.path.join(Source_dir,fname)
  abs_path = os.path.abspath(file_path)
  copy_to(abs_path,Dest_dir)
  

