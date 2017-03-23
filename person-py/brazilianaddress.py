"""Implements class BrazilianAdress."""

class BrazilianAddress:
    def __init__(self, street_, number_, neighborhood_, complement_="", city_, 
                 state_, cep_): 
        
        """Initializes an object with user's values."""
        
        self.street = street_
        self.number = number_
        self.neighborhood = neighborhood_
        self.complement = complement_
        self.city = city_
        self.state = state_
        self.cep = cep_
    
    def __getattr__(self, name):
        if name == "street": 
            return self._street
        
        elif name == "number": 
            return self._number
        
        elif name == "neghborhood": 
            return self._neighborhood
        
        elif name == "complement": 
            return self._complement
        
        elif name == "city": 
            return self._city
        
        elif name == "state": 
            return self._state
        
        elif name == "cep": 
            return self._cep
        
        else:
            raise AttributeError, name
    
    def __setattr__(self, name, value):
        if name == "street": 
            if len(value) > 0: 
                self.__dict__["_street"] = value
            
            else:
                raise ValueError, "Invalid %s value: %s" % (name, value)
        
        elif name == "number": 
            if value > 0:
                self.__dict__["__number"] = value
            
            else:
                raise ValueError, "Invalid %s value: %s" % (name, value)
        
        elif name == "neighborhood": 
            if len(value) > 0: 
                self.__dict["_neighborhood"] = value
            
            else:
                raise ValueError, "Invalid %s value: %s" % (name, value)
        
        elif name == "