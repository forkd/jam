#!/usr/bin/env python
#coding: utf8

"""Implements class Jack."""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"


import hashlib
import os


class Jack(object):
    
    """Jack - A class that splits/joins/checks files.
    
    Jack can split a file in many pieces with its split() method.
    Then, it can join these files with join() method. Jack can
    either generate the MD5 checksum for the file.
    
    All files are splitted in parts which size depends on metr to
    determine if its size is in KiB, MiB, GiB etc. mult determines
    the file size (e.g., if metr is 2 and mult is 250, each part 
    will have 250 MiB).
    
    The name 'Jack' is because of Jack, The Ripper.
    
    """
    
    def __init__(self, finput, foutput='', times=1, metric=2, size=1024, extension=True):
        """Initializes all attrs with __getattr__() and __setattr__()."""
        
        if not foutput:
            foutput = finput
        
        self.inpath = os.path.dirname(finput)
        self.infile = os.path.basename(finput)
        self.outpath = os.path.dirname(foutput)
        self.outfile = os.path.basename(foutput)
        self.size = size
        self.metric = metric
        self.times = times
        self.fext = extension
    
    def __getattr__(self, name):
        """Retrieves attrs values."""
        
        if name == 'inpath':
            return self._inpath
            
        elif name == 'infile':
            return self._infile
            
        elif name == 'outpath':
            return self._outpath
            
        elif name == 'outfile':
            return self._outfile
            
        elif name == 'size':
            return self._size
            
        elif name == 'metric':
            return self._metric
            
        elif name == 'times':
            return self._times
        
        elif name == 'fext':
            return self._fext
            
        else:
            raise AttributeError('Attr \'{0}\' does\'t exist.'.format(name))
    
    def __setattr__(self, name, value):
        """Sets attrs values."""
        
        if name == 'inpath':
            if value:
                self.__dict__['_inpath'] = value
            else:
                self.__dict__['_inpath'] = '.'
            
        elif name == 'infile':
            if value:
                self.__dict__['_infile'] = value
            else:
                raise ValueError('Input file not defined.')
            
        elif name == 'outpath':
            if value:
                self.__dict__['_outpath'] = value
            else:
                self.__dict__['_outpath'] = '.'
            
        elif name == 'outfile':
            if value:
                self.__dict__['_outfile'] = value
            else:
                self.__dict__['_outfile'] = self.infile
            
        elif name == 'size':
            if value == 1024 or value == 1000:
                self.__dict__['_size'] = value
            else:
                raise ValueError('Attr \'{0}\' out of range.'.format(name))
                
        elif name == 'metric':
            if 0 < value < 10:
                self.__dict__['_metric'] = value
            else:
                raise ValueError('Attr \'{0}\' out of range.'.format(name))
                
        elif name == 'times':
            if 0 < value < self.size:
                self.__dict__['_times'] = value
            else:
                raise ValueError('Attr \'{0}\' out of range.'.format(name))
                
        elif name == 'fext':
            if value:
                self.__dict__['_fext'] = True  # File extensions will be letters
            else:
                self.__dict__['_fext'] = False  # File extensions will be numbers
                
        else:
            raise AttributeError('Attr \'{0}\' doesn\'t exist.'.format(name))
    
    def chriter(self, input_string):
        """Allows to use extensions like .aa, .ab, .ac etc."""
        
        input_string = input_string.lower()
        
        for index in input_string:
            if not index.islower():
                raise IOError('Only ASCII letters are allowed.')
        
        index = -1
        input_list = list(input_string)
        len_input_list = -len(input_list)
        
        while 1:
            if index != len_input_list:
                if input_list[index] != 'z':
                    input_list[index] = chr(ord(input_list[index]) + 1)
                    break
                else:
                    input_list[index] = 'a'
                    index -= 1
            else:
                if input_list[index] != 'z':
                    input_list[index] = chr(ord(input_list[index]) + 1)
                    break
                else:
                    input_list[index] = 'a'
                    input_list.insert(0, 'a')
                    break
                
        return ''.join(input_list)
    
    def split(self):
        """Splits a file (self.finput) in several parts."""
        
        if self.fext:
            fext = 'aa'
        else:
            fext = 1
            
        finput = open('{0}/{1}'.format(self.inpath, self.infile), 'r')
        
        while 1:
            fpart = finput.read(1)
            
            if fpart:
                if self.fext:
                    foutput = open('{0}/{1}.{2}'.format(self.outpath, 
                                                        self.outfile, 
                                                        fext), 'w')
                    fext = self.chriter(fext)
                else:
                    foutput = open('{0}/{1}.{2:03d}'.format(self.outpath, 
                                                            self.outfile, 
                                                            fext), 'w')
                    fext += 1
                foutput.write(fpart)
                foutput.write(finput.read((self.size ** self.metric * 
                                           self.times) - 1))
                foutput.close()
                
            else:
                break
            
        finput.close()
    
    def join(self):
        """Joins a splitted file into a single file in self.ffolder."""
        
        if self.fext:
            fext = 'aa'
        else:
            fext = 1
            
        foutput = open('{0}/{1}'.format(self.outpath, self.outfile), 'w')
        
        while 1:
            try:
                if self.fext:
                    finput = open('{0}/{1}.{2}'.format(self.inpath, 
                                                       self.infile, 
                                                       fext), 'r')
                    fext = self.chriter(fext)
                else:
                    finput = open('{0}/{1}.{2:03d}'.format(self.inpath, 
                                                           self.infile, 
                                                           fext), 'r')
                    fext += 1
                    
                fpart = finput.read(1)
                
                if fpart:
                    foutput.write(fpart)
                    foutput.write(finput.read())
                    
                finput.close()
                
            except IOError:
                break
                
        foutput.close()
        
        if not os.path.getsize('{0}/{1}'.format(self.outpath, self.outfile)):
            os.remove('{0}/{1}'.format(self.outpath, self.outfile))
            
            if self.fext:
                raise IOError('[Errno 2] No such file or directory: \
\'{0}/{1}.{2}\''.format(self.inpath, self.infile, fext))
            else:
                raise IOError('[Errno 2] No such file or directory: \
\'{0}/{1}.{2:03d}\''.format(self.inpath, self.infile, fext))
    
    def checksum(self, cs=''):
        """Checks or generate the file's MD5 checksum."""
        
        check = hashlib.md5()
        finput = open('{0}/{1}'.format(self.inpath, self.infile), 'r')
        
        while 1:
            fpart = finput.read(self.size ** self.metric * self.times)
            
            if fpart:
                check.update(fpart)
                
            else:
                break
        
        finput.close()
        
        if not cs:
            return check.hexdigest()
        
        elif cs == check.hexdigest():
            return True
        
        else:
            return False
        
#EOF
