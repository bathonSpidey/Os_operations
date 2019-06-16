# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:41:37 2019

@author: Abir
"""

from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

a=get_exif("IMG_1526.JPG")
print(a["DateTimeOriginal"])

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("E:\\udemy\\Python prog"):
    f.extend(filenames)
    break

print(f)