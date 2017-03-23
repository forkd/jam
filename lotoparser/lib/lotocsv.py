#!/usr/bin/env python
#coding: utf8

"""LotoCSV

A class that parse a HTML file - downloaded from
http://www1.caixa.gov.br/loterias/loterias/ - and
creates a Comma Separated Value (CSV) file from it.

"""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"


from HTMLParser import HTMLParser
from urllib import urlopen
 

class LotoCSV(HTMLParser):
   
    """Main class.
    
    Receives as attributes the file's URL and the file
    where the output will be recorded.
    Example of use: LotoCSV(URL, file)
   
    """
    
    def __init__(self, url, file_output):
        """Initializes the class' attributes and start
        reading the HTML file.
        
        """
        
        HTMLParser.__init__(self)  # Superclass' initializer.
        
        url = urlopen(url)
        
        self.file_output = open(file_output, "w")
        self.record = False
        self.start_line = False
        self.line = ""
        
        self.feed(url.read())
        
        self.file_output.close()
        
    def handle_starttag(self, tag, attrs):
        """When a start tag will be found..."""
        
        if tag == "tr":  # A line could be starting...
            self.start_line = True
            return
        
        if self.start_line and tag == "td":  # Start recording data.
            self.record = True
        
    def handle_endtag(self, tag):
        """When a end tag will be found..."""
        
        if tag == "tr":  # A line was read. Record in file and restart attrs.
            if len(self.line):
                self.line += "\n"
                self.file_output.write(self.line)
            
            self.line = ""
            
            return
        
        elif self.start_line and tag == "td":  # End recording data.
            self.record = False
        
        elif tag == "th":  # This hack eliminates Federal´s heading.
            self.line = ""
            self.record = False
        
    def handle_data(self, data):
        """When data will be found..."""
        
        if self.record:
            self.line += data + ";"

#EOF
