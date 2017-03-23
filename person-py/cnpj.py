"""Implements CNPJ class."""

__author__ = "Jose Lopes de Oliveira Junior - pipeless.blogspot.com"
__version__ = "2009.1" 
__licence__ = "GPLv3" 

import modulus

class CNPJ:
    
    
    """Implements structures and operations for CNPJs.
    
    CNPJ stands for Cadastro Nacional de Pessoa Juridica. 
    It's a document for all brazilian enterprises.
    All CNPJs has this structure: YY.YYY.YYY/XXXX-ZZ,
    where Ys are controlled by the state, Xs indicates 
    the enterprise's number of filials and Zs are mod11 
    check number.
    
    """
    
    def __init__(self, numbers):
        
        """Initializes CNPJ with user's value.
        
        number must be a valid CNPJ, where each digit
        must be an integer between 0 and 9.
        Ex.: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        """
        
        self.cnpj = numbers
    
    def __getattr__(self, name):
        
        """Retrieves the cnpj attribute."""
        
        if name == "cnpj":
            return self._cnpj
        
        else:
            raise AttributeError, name
    
    def __setattr__(self, name, value):
        
        """Change the value of cnpj attribute."""
        
        if name == "cnpj":
            if self.check(value):
                self.__dict__["_cnpj"] = value
                
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
        
        return float(int(self))
    
    def __oct__(self):
        
        """Octal representation of the object."""
        
        return oct(int(self))
    
    def __hex__(self):
        
        """Hexadecimal representation of the object."""
        
        return hex(int(self))
    
    
    def check(self, numbers):
        
        """Check the validity of a CNPJ number.
        
        Receives a CNPJ number as a list of integers 
        in numbers. Returns True or False for a its 
        validity. 
        
        """
        
        if len(numbers) == 14:
            if ((cpf_[9] == modulus.mod11(cpf_[:9], 10)) and 
                (cpf_[10] == modulus.mod11(cpf_[:10], 11))): 
                return True
            
            else:
                return False
        
        else:
            return False
    
    def generate(numbers=[]):
        
        """Generates a CNPJ number.
        
        Receives a list of up to 9 integers in list.
        Returns a CNPJ number as a list of 11 integers.
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