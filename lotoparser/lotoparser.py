#!/usr/bin/env python
#coding: utf8

"""LotoParser

This is the program's main file. Implements user 
interface and call other files to do the job.

"""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"
__version__ = "0.1.0"


import sys
from os import makedirs
from os.path import dirname, exists
from urllib import ContentTooShortError
from zipfile import BadZipfile

from lib.lotofile import (LotoFile, BASE_DIR_PATH, ZIP_FILES, HTM_FILES, 
    PIC_FILES, OUT_FILES)
from lib.parser import Parser


class LotoParser(object):
    
    """Program's main class.
    
    Implements every routines to process user's
    requirements and generate the CSV and XML
    files.
    
    """
    
    def version(self):
        return """LotoParser %s
Copyright (C) 2010 %s <http://joselopes.org>
License %s: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
        
Written by %s.""" % (__version__, __author__, __license__, __author__)
    
    def help(self):
        return """Usage: lotoparser [OPTION]
Retrieves the loto results from Caixa Econômica Federal's site and 
generates a CSV and a XML file with these results for each game.

These are the options:
-c, --csv           Generates CSV files.
-x, --xml           Generates XML files.
-h, --help          Display this help and exit.
-v, --version       Output version information and exit."""
    
    def main(self):
        """The main method.
        
        Returns the code to OS (used in sys.exit()).
        
        """
        
        # Iterates over all parameters.
        for parameter in range(1, len(sys.argv)):
            
            if (sys.argv[parameter] == "-c" or
                sys.argv[parameter] == "--csv"):
                
                # Check if destination directory exists. 
                # If not, create it.
                try:
                    if not exists(dirname(BASE_DIR_PATH)):
                        makedirs(dirname(BASE_DIR_PATH), mode=0755)
                
                except OSError:
                    print("LotoParser: Could not create working directory.")
                    return 1
                
                lf = LotoFile()
                files_with_errors = []
                
                print("Downloading files from Caixa's website...")
                for game in ZIP_FILES:
                    try:
                        lf.download(game, game)
                    
                    except (IOError, ContentTooShortError):
                        files_with_errors.append(game)
                
                if files_with_errors:
                    print("LotoParser: A download problem occurred with \
these files: {0}.".format(files_with_errors))
                
                files_with_errors = []  # Restarts errors.
                
                print("Unzipping downloaded files...")
                for game in ZIP_FILES:
                    try:
                        lf.unzip(game)
                    except (IOError, BadZipfile):
                        files_with_errors.append(game)
                    
                if files_with_errors:
                    print("LotoParser: A unzip problem occurred with these \
files: {0}.".format(files_with_errors))
                
                files_with_errors = []  # Restarts errors.
                p = Parser()
                index = -1
                
                print("Parsing HTML files...")
                for game in HTM_FILES:
                    try:
                        index += 1
                        p.csv_parser(BASE_DIR_PATH + game, 
                            BASE_DIR_PATH + OUT_FILES[index] + ".csv")
                    except IOError:
                        files_with_errors.append(game)
                
                if files_with_errors:
                    print("LotoParser: A parse problem occurred with these \
files: {0}.".format(files_with_errors))
                
                files_with_errors = []  # Restarts errors.
                
                print("Removing junk files...")
                for index in range(9):
                    try:
                        lf.remove(ZIP_FILES[index])
                    except OSError:
                        files_with_errors.append(ZIP_FILES[index])
                    
                    try:
                        lf.remove(HTM_FILES[index])
                    except OSError:
                        files_with_errors.append(HTM_FILES[index])
                    
                    try:
                        lf.remove(PIC_FILES[index])
                    except OSError:
                        files_with_errors.append(PIC_FILES[index])
                    
                if files_with_errors:
                    print("LotoParser: A removing problem occurred with \
these files: {0}.".format(files_with_errors))
                
                return 0
            
            elif (sys.argv[parameter] == "-x" or
                sys.argv[parameter] == "--xml"):
                
                print("LotoParser: CSV files must be generated first.")
                
                print("Generating MegaSena's XML file...")
                Parser().xml_parser("./loto/megasena.csv", 
                    "./loto/megasena.xml")
                print("Generating LotoFacil's XML file...")
                Parser().xml_parser("./loto/lotofacil.csv", 
                    "./loto/lotofacil.xml")
                print("Generating Quina's XML file...")
                Parser().xml_parser("./loto/quina.csv", 
                    "./loto/quina.xml")
                print("Generating LotoMania's XML file...")
                Parser().xml_parser("./loto/lotomania.csv", 
                    "./loto/lotomania.xml")
                print("Generating DuplaSena's XML file...")
                Parser().xml_parser("./loto/duplasena.csv", 
                    "./loto/duplasena.xml")
                print("Generating Federal's XML file...")
                Parser().xml_parser("./loto/federal.csv", 
                    "./loto/federal.xml")
                print("Generating LotoGol's XML file...")
                Parser().xml_parser("./loto/lotogol.csv", 
                    "./loto/lotogol.xml")
                print("Generating Loteca's XML file...")
                Parser().xml_parser("./loto/loteca.csv", 
                    "./loto/loteca.xml")
                print("Generating TimeMania's XML file...")
                Parser().xml_parser("./loto/timemania.csv", 
                    "./loto/timemania.xml")
                
                return 0
            
            elif (sys.argv[parameter] == "-h" or
                sys.argv[parameter] == "--help"):
                print(self.help())
                return 0
            
            elif (sys.argv[parameter] == "-v" or 
                sys.argv[parameter] == "--version"):
                print(self.version())
                return 0
            
            else:
                # Invalid parameter.
                # Finnishes loop to display help.
                break
            
        # No parameters were given.
        print(self.help())
        return 1    
        
        
# 
# Main
# 

if __name__ == "__main__":
    sys.exit(LotoParser().main())

#EOF
