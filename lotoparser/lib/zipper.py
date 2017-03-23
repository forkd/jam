#!/usr/bin/env python
#coding: utf8

"""Zipper

A class that can zip and unzip files.

"""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"


import os
import zipfile
try:
    import zlib
    has_zlib = True
except:
    has_zlib = False
 

class Zipper(object):
    
    """This is the main class.
    
    Can zip and unzip files.
    
    """
    
    def zip(self, file_to_zip, dir="./", name="Zipped_File.zip", mode="w"):
        """Zips file into dir with name.
        
        Mode can be w to write a new file or
        a to append in an existing file.
        
        """
        
        if not name.endswith(".zip"):
            name += ".zip"
        
        if has_zlib:
            compression = zipfile.ZIP_DEFLATED
        else:
            compression = zipfile.ZIP_STORED
        
        zf = zipfile.ZipFile(name, mode)
        zf.write(file_to_zip, compress_type=compression)
        zf.close()
    
    def unzip(self, file_to_unzip, dir="./"):
        """Unzips file into dir."""
        
        zf = zipfile.ZipFile(file_to_unzip)
        
        for content in zf.namelist():
            if content.endswith('/'):
                os.makedirs(content)
            
            else:
                out_file= open(os.path.join(dir, content), "wb")
                out_file.write(zf.read(content))
                out_file.close()
#EOF
