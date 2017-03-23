"""Implements CPF class."""

__author__ = "Jose Lopes de Oliveira Junior - pipeless.blogspot.com"
__version__ = "2009.1" 
__licence__ = "GPLv3" 

import modulus

class CPF:
    
    
    """Implements structures and operations for CPFs.
    
    CPF stands for Cadastro de Pessoa Fisica. It's a
    document for all brazilian citizens.
    All CPFs has this structure: YYY.YYY.YYX-ZZ,
    where Y is controlled by the state, X indicates 
    the citizen's state and Z is mod11 check number.
    
    """
    
    def __init__(self, cpf_):
        
        """Initializes CPF with user's value.
        
        list must be a valid CPF, where each digit
        must be an integer between 0 and 9.
        Ex.: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        """
        
        self.cpf = cpf_
    
    def __getattr__(self, name):
        
        """Retrieves the cpf attribute."""
        
        if name == "cpf":
            return self._cpf
        
        else:
            raise AttributeError, name
    
    def __setattr__(self, name, value):
        
        """Change the value of cpf attribute."""
        
        if name == "cpf":
            if self.check(value):
                self.__dict__["_cpf"] = value
                
            else:
                raise ValueError, "Invalid %s value: %s" % (name, value)
    
    def __str__(self):
        
        """String representation of the object."""
        
        return self.format(1)
    
    def __int__(self):
        
        """Integer representation of the object."""
        
        return int(self.__str__())
    
    def __float__(self):
        
        """Floating point representation of the object."""
        
        return float(self.__str__())
    
    def __oct__(self):
        
        """Octal representation of the object."""
        
        return oct(self.__int__())
    
    def __hex__(self):
        
        """Hexadecimal representation of the object."""
        
        return hex(self.__int__())
    
    def __long__(self):
        
        """Long integer representation of the object."""
        
        return long(self.__int__())
    
    
    def check(self, cpf_):
        
        """Check the validity of a CPF number.
        
        Receives a CPF number as a list of integers 
        in list. Returns True or False for a its 
        validity. 
        
        """
        
        if len(cpf_) == 11:
            if ((cpf_[9] == modulus.mod11(cpf_[:9], 10)) and 
                (cpf_[10] == modulus.mod11(cpf_[:10], 11))): 
                return True
            
            else:
                return False
        
        else:
            return False
    
    def generate(cpf_=[]):
        
        """Generates a CPF number.
        
        Receives a list of up to 9 integers in list.
        Returns a CPF number as a list of 11 integers.
        If the format of list were wrong, an empty
        list will be returned.
        It's a static method.
        
        """
        
        if len(cpf_) <= 9: 
            # If cpf_ < 9, the next line complete-it.
            cpf_ = modulus.generate_int_list(cpf_, 9)
            
            cpf_.append(modulus.mod11(cpf_, 10))
            cpf_.append(modulus.mod11(cpf_, 11))
        
            return cpf_
        
        else:
            return []
    
    generate = staticmethod(generate)
    
    def format(self, flag=0):
        
        """Format a CPF object.
        
        flag indicates the format output. flag == 0 
        outputs YYY.YYY.YYY-XX and flag == 1 outputs 
        YYYYYYYYYXX. 
        
        """
        
        if not flag: 
            return "%d%d%d.%d%d%d.%d%d%d-%d%d" % (self._cpf[0], self._cpf[1], 
                                                  self._cpf[2], self._cpf[3], 
                                                  self._cpf[4], self._cpf[5], 
                                                  self._cpf[6], self._cpf[7], 
                                                  self._cpf[8], self._cpf[9], 
                                                  self._cpf[10])
        
        else: 
            return "%d%d%d%d%d%d%d%d%d%d%d" % (self._cpf[0], self._cpf[1], 
                                               self._cpf[2], self._cpf[3], 
                                               self._cpf[4], self._cpf[5], 
                                               self._cpf[6], self._cpf[7], 
                                               self._cpf[8], self._cpf[9], 
                                               self._cpf[10])

# Main
cpf = CPF([7,7,7,7,7,7,7,7,7,7,7])
print cpf.__getattr__("cpf")

cpf.__setattr__("cpf", [0,6,6,4,4,3,1,5,6,9,0])
print cpf.format()

cpf.__setattr__("cpf", [4,4,4,4,4,4,4,4,4,4,4])
print cpf.format(1)

cpf.__setattr__("cpf", [1,1,1,1,1,1,1,1,1,1,1])

print "String.:", cpf
print "Integer:", int(cpf)
print "Float..:", float(cpf)
print "Octal..:", oct(cpf)
print "Hex....:", hex(cpf)
print "Long...:", long(cpf)

cpf1 = CPF(CPF.generate())
print "CPF 1 = %s" % cpf1.format()