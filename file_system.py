# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:41:37 2019

@author: Abir
"""

from PIL import Image
from PIL.ExifTags import TAGS

import glob
import os
from datetime import datetime
import shutil


search_dir = "/home/spidey/seperate_files/"
new_files=[]
# remove anything from the list that is not a file (directories, symlinks)
# thanks to J.F. Sebastion for pointing out that the requirement was a list 
# of files (presumably not including directories)  
files = filter(os.path.isfile, glob.glob(search_dir + "*"))
for file in files:
    new_files.append(file)

new_files.sort(key=lambda x: os.path.getmtime(x))



def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret



#a=get_exif("05160238.JPG")
#print(a["DateTimeOriginal"])

#from os import walk

#f = []
#for (dirpath, dirnames, filenames) in walk("/home/spidey/seperate_files"):
 #   f.extend(filenames)
  #  break

#print(new_files)
check_day=0
set_hour=0
set_min=0
trap_time=0
odd_hour=0
reference_time=0
refer_two=0
reference_file=''
fmt = '%Y:%m:%d %H:%M:%S'

for file in new_files:
    #print(file[-1]) !='G'
    #print(reference_time,file)
    if file[-1] == 'G' or file[-1]=='g':
        a=get_exif(file)
        t1 = datetime.strptime(a["DateTimeOriginal"], fmt)
        #print('######## NEW IMAGE INFO########')
        #print('##########new Image data{}: {}#######'.format(file, a))
        if reference_time==0:
            reference_time=t1
        diff=t1-reference_time
        days, seconds = diff.days,diff.seconds
        minutes = int((seconds % 3600) // 60)
        print(minutes)
        if minutes<=0:
            print('I need to send it to no action')
            shutil.move(file, '/home/spidey/seperate_files/no_action')
        elif minutes<5:
            print('send it to action')
            shutil.move(file, '/home/spidey/seperate_files/action')
        elif minutes>=5:
            reference_time=t1
            print('send to no action')
            shutil.move(file, '/home/spidey/seperate_files/no_action')
            
            
        
        #new_check_day=int(a["DateTimeOriginal"][8:10]
    
        #if check_day == new_check_day:
         #   new_hour=int(a["DateTimeOriginal"][11:13])
          #  if set_hour==0:
           #     set_hour=new_hour
            #    set_min=
            #elif abs(new_hour-set_hour)==0:
              #  new_min=int(a["DateTimeOriginal"][14:16])
             #   if set_min==0:
              #      set_min=new_min
               # elif 
              

                
                
        