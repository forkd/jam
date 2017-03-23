# -*- Mode: Python -*- 
# -*- coding: utf-8 -*- 
# vi:si:et:sw=4:sts=4:ts=4 

"""Implements mod10, mod11 and related algorithms."""

# 2008/11/08 
# Author: José Lopes de Oliveira Júnior
#     http://versaopropria.blogspot.com
#     jlojunior _at_ gmail _dot_ com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
# USA.

import random

__all__ = ["mod10", "mod11", "generate_int_list"]
__version__ = "2008.1.1"

def mod10(list):
    
    """Implements the Luhn Algorithm (a.k.a. mod10), which 
    is a checksum formula to validade a variety of 
    identification numbers, such as credit card numbers.
    
    Requires a list of integers with the numbers to be 
    validated.
    
    """
    
    sum = 0
    double = True
    
    # Iterates til the last item of the list, adding to 
    # +sum the item and two times item, interspersed.
    for item in reversed(list):
        if double:
            item *= 2
            
            if item > 9:  # Casting out nines
                item -= 9
        
        sum += item
        double = not double
    
    mod = sum % 10
    
    # sum must be a multiple of 10. If it is, zero is 
    # +returned. Else, got to calculate how many numbers 
    # +are missing until 10.
    if mod:
        return 10 - mod
    
    else:
        return mod

def mod11(list, max_weight=7):
    
    """Implements Modulus 11 check digit algorithm.
    
    It's a variation of the HP's Modulus 11 algorithm.
    Requires the sequence to be calculated in a list of
    integers.
    The HP's Modulus 11 algorithm can be accessed through
    the following link:
    http://docs.hp.com/en/32209-90024/apds02.html
    
    Requires a list of integers with the values to be
    calculated and the maximum value of weight variable.
    
    """
    
    sum = 0
    weight = 2
    
    # Iterates through the list from right to left,
    # +multiplying each value for it's weight. If
    # +the weight reaches max_weight, then it is
    # +restarted to 2.
    for item in reversed(list):
        sum += item * weight
        weight += 1
        
        if weight > max_weight:
            weight = 2
    
    mod = 11 - sum % 11
    
    # HP's Modulus 11 algorithm says that a 10
    # +result is invalid and a 11 result is equal
    # +to 0. So, both values are returned as 0.
    if mod > 9:
        return 0
    
    else:
        return mod


def generate_int_list(list=[], length=10, min_value=0, max_value=10):
    
    """Generate and return a list of random integers.
    
    The random values will be between min_value and 
    max_value - 1. If list's length were less than length, 
    it'll be completed with random values until list's 
    length were equal to length.
    
    """
    
    # Using a variable to check list length, avoid calling 
    # +the same function (len()) more than once.
    length_list = len(list)
    
    while length_list < length:
        list.append(random.randrange(min_value, max_value))
        length_list += 1
    
    return list