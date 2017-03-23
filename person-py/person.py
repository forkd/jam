"""Implements methods for person."""

import datetime

class Person:
    
    def __init__(self, name_1, name_2, birthdate_year, birthdate_month, 
                 birthdate_day, email_):
        self.first_name = name_1
        self.last_name = name_2
        self.birthdate = datetime.date(birthdate_year, birthdate_month, 
                                       birthdate_day)
        self.email = email_
    
    def __str__(self):
        return "%s %s - %d/%d/%d" % (self.first_name, self.last_name, 
                                     self.birthdate.__getattribute__("year"), 
                                     self.birthdate.__getattribute__("month"), 
                                     self.birthdate.__getattribute__("day"))

# Main
p = Person("J", "Lopes", 1984, 6, 14)
print p