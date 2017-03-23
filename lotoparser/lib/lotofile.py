#!/usr/bin/env python
#coding: utf8

"""LotoFile

Downloads results of lottery games from Caixa 
Econômica Federal's website and manages files.

"""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"


import os
from zipfile import BadZipfile
from urllib import urlretrieve, ContentTooShortError

from zipper import Zipper


BASE_URL_PATH = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/"
BASE_DIR_PATH = "./loto/"
ZIP_FILES = ["D_megase.zip", "D_lotfac.zip", "D_quina.zip", "D_lotoma.zip", 
    "d_dplsen.zip", "D_FEDERA.zip", "d_lotogo.zip", "d_loteca.zip", 
    "D_timema.zip"]
HTM_FILES = ["D_MEGA.HTM", "D_LOTFAC.HTM", "D_QUINA.HTM", "D_LOTMAN.HTM", 
    "D_DPLSEN.HTM", "D_LOTFED.HTM", "D_LOTOGO.HTM","D_LOTECA.HTM", 
    "D_TIMEMA.HTM"]
PIC_FILES = ["T2.GIF", "LOTFACIL.GIF", "T7.GIF", "T11.GIF", "T5.GIF", 
    "T1.GIF", "LOTOGO.GIF", "LOTECA.GIF", "T12.GIF"]
OUT_FILES = ["megasena", "lotofacil", "quina", "lotomania", "duplasena", 
    "federal", "lotogol", "loteca", "timemania"]


class LotoFile(object):
    
    """A class that downloads results 
    of lottery games from Caixa Econômica 
    Federal's website and manages files.
    
    """
    
    def download(self, file_to_download, file_name):
        """Downloads file_to_download, saving as file_name."""
        
        # Can raise IOError or ContentTooShortError.
        urlretrieve(BASE_URL_PATH + file_to_download, 
            BASE_DIR_PATH + file_name)
    
    def unzip(self, file_to_extract):
        """Unzips file_to_extract."""
        
        # Can raise BadZipfile.
        Zipper().unzip(BASE_DIR_PATH + file_to_extract, BASE_DIR_PATH)
        
    def remove(self, file_to_delete):
        """Removes zip, html and gif files."""
        
        # Can raise OSError.
        os.remove(BASE_DIR_PATH + file_to_delete)
            
#EOF
