class Person:
    """Person abstract data type definition."""
    
    def __init__(self):
        """Initialize all attributes with zero, empty or None."""
        
        self._name = ""
        self._cpf = []
    
    def print_name (self):
        """Returns the name on the screen."""
        
        return self._name
    
    def print_cpf(self):
        """Prints the CPF formated on the screen."""
        
        if len(self._cpf) < 11:
            return "000.000.000-00"
        else:
            return "%d%d%d.%d%d%d.%d%d%d-%d%d" % (self._cpf[0], self._cpf[1],
                                                  self._cpf[2], self._cpf[3],
                                                  self._cpf[4], self._cpf[5],
                                                  self._cpf[6], self._cpf[7],
                                                  self._cpf[8], self._cpf[9],
                                                  self._cpf[10])