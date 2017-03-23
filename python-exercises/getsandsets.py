class People:
    def __init__(self, name="", tel=""):
        self.name = name
        self.tel = tel
    
    def __getattr__(self, name):
        if name == "name":
            return self._name
        
        elif name == "tel":
            return self._tel
    
    def __setattr__(self, name, value):
        if name == "name":
            if len(value) > 2:
                self.__dict__["_name"] = value
            
            else:
                raise ValueError, "Invalid %s value: %s" % (name, value)
        
        elif name == "tel":
            if len(value) > 8:
                self.__dict__["_tel"] = value
            
            else:
                raise ValueError, "Invalid %s value: %s" % (name, value)
    
    def __str__(self):
        return "%s - %s" % (self._name, self._tel)
    
    def __del__(self):
        print "You killer! :-)"

# Main
person = People("Eddie", "01-555-9934")
print person.__getattr__("name")
person.__setattr__("name", "Eddie Vedder")
print person.__getattr__("name")
person.tel = '987654321'
print person.__getattr__("tel")
print person