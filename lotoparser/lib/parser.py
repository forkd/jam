#!/usr/bin/env python
#coding: utf8

"""Parser

It's an interface to LotoCSV and LotoXML classes.

"""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"


from os.path import abspath
from lotocsv import LotoCSV
from lotoxml import LotoXML


class Parser(object):
    
    """This class is an interface for LotoCSV and 
    LotoXML classes.
    
    """
    
    def csv_parser(self, file_input, file_csv):
        """Process file_input and generates file_csv file."""
        
        file_input = "file://" + abspath(file_input)
        LotoCSV(file_input, file_csv)
    
    def xml_parser(self, file_csv, file_xml):
        """Process file_csv and generates file_xml file."""
        
        LotoXML(file_csv, file_xml)
        
#EOF
