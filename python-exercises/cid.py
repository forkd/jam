# -*- coding: utf-8 -*- 

class ICD:
    
    """Represents an ICD.
    
    ICD stands for International Statistical 
    Classification of Diseases and Related Health
    Problems.
    
    """
    
    def __init__(self):
         
        """Initializes an icd object with default values."""
        
        self._code = "A000"
        self.__name = "Cólera devida a Vibrio Cholerae 01, biótipo Cholerae"
    
    def __del__(self):
        print self, "muerto!"
    
    
    def get_name(self):
        return self.__name
    
    def get_code(self):
        return self._code
    
    
    def set_code(self, new_code):
        self._code = new_code
        # Here, a search through the CID table should be done,
        # +to maintain the coherence between the code and it's
        # +name.
    
    def set_name(self, new_name):
        self.__name = new_name
        # Like set_code method, the code should be updated here.

cid = ICD()
print cid._ICD__name
del cid