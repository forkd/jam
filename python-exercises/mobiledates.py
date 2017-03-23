# mobiledates
#    Calculate and print on the screen many of the mobile holidays
# through the year - all related with the catolic calendar.
#
# AUTHOR: Jose' Lopes de Oliveira Ju'nior - http://versaopropria.blogspot.com
#
# CONTACT: jlojunior _at_ gmail _dot_ com
#
# LICENCE: GPLv3 - http://www.gnu.org/licenses/gpl.html
#
# Python: v2.5

import calendar
import datetime

def easter(date):
    """Calculate the date of the easter.
    
    Requires a datetime type object. Returns a datetime object with the
    date of easter for the passed object's year.
    
    """
    
    if 1583 <= date.year < 10000:  # Delambre's method
        b = date.year / 100  # Take the firsts two digits of the year.
        
        h = (((19 * (date.year % 19) + b - (b / 4)) - 
              ((b - ((b + 8) / 25) + 1) / 3) + 15) % 30)
        k = ((32 + 2 * (b % 4) + 2 * ((date.year % 100) / 4) - h - 
              ((year % 100) % 4)) % 7)
        m = ((date.year % 19) + 11 * h + 22 * k) / 451
        
        return datetime.date(date.year, (h + k - 7 * m + 114) / 31, 
                            ((h + k - 7 * m + 114) % 31) + 1)
    
    elif 1 <= date.year < 1583:  # Julian calendar
        d = (19 * (date.year % 19) + 15) % 30
        e = (2 * (date.year % 4) + 4 * (date.year % 7) - d + 34) % 7
        
        return datetime.date(date.year, (d + e + 114) / 31, 
                            ((d + e + 114) % 31) + 1)
    
    else:  # Negative value
        raise ValueError, "Invalid year: %d." % year

def print_date(name, date_obj):
    """Print a formated string with the date of the passed date object."""
    
    print "%s %0.2d/%0.2d/%0.4d - %s" % (name, date_obj.day, date_obj.month, 
                                         date_obj.year, 
                                         calendar.day_name[date_obj.weekday()])


# Main

# Read year from user.
year = int(raw_input("Enter with the year : "))

# Create a date object with the year passed.
date = datetime.date(year, 1, 1)

# Calculate easter
easter_day = easter(date)

# Calculate every possible date.
mardi_gras = easter_day - datetime.timedelta(47)
palm = easter_day - datetime.timedelta(7)
passion = easter_day - datetime.timedelta(2)
ascension = easter_day + datetime.timedelta(39)
pentecost = easter_day + datetime.timedelta(49)
corpus_christi = easter_day + datetime.timedelta(60)

# Print the result for the user.
print_date("Carnaval.....:", mardi_gras)
print_date("Ramos........:", palm)
print_date("Paixao.......:", passion)
print_date("Pascoa.......:", easter_day)
print_date("Ascensao.....:", ascension)
print_date("Pentecostes..:", pentecost)
print_date("Corpus Cristi:", corpus_christi)