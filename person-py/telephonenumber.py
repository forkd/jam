#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""Implements TelephoneNumber class."""

__author__ = "José Lopes de Oliveira Júnior"
__version__ = "2008.1"
__license__ = "GPLv3"

class TelephoneNumber:
    
    
    """Implements structures and operations for phone numbers."""
    
    def __init__(self, country_code_, area_code_, prefix_, suffix_, branch_):
        
        """Initializes all attributes with user's values."""
        
        self.country_code = country_code_ 
        self.area_code = area_code_
        self.prefix = prefix_ 
        self.suffix = suffix_
        self.branch = branch_
    
    def __getattr__(self, name):
        
        """Retrieves any attribute for the user."""
        
        if name == "country_code":
            return self._country_code
        
        elif name == "area_code":
            return self._area_code
        
        elif name == "prefix":
            return self._prefix
        
        elif name == "suffix":
            return self._suffix
        
        elif name == "branch":
            return self._branch
        
        else:
            raise AttributeError, name
    
    def __setattr__(self, name, value):
        
        """Change the value of any attribute."""
        
        if name == "area_code":
            if 0 <= value <= 99:
                self.__dict__["_area_code"] = value
            
            else:
                raise ValueError, "Invalid %s value: %d" % (name, value)
        
        elif ((name == "country_code") or (name == "prefix") or 
              (name == "suffix") or (name == "branch")): 
            if 0 <= value <= 9999:
                self.__dict__["_" + name] = value
            
            else:
                raise ValueError, "Invalid %s value: %d" % (name, value)
    
    def __str__(self):
        
        """A string representation of the object."""
        
        return "+%.4d (%.2d) %.4d-%.4d - %.4d" % (self.country_code, 
                                                  self.area_code, self.prefix, 
                                                  self.suffix, self.branch)


# Main
if __name__ == "__name__":
    tel = TelephoneNumber(55, 32, 3332, 3394, 33)
    print tel