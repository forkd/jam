#!/usr/bin/env python

# Sieve of Eratosthenes
#    Calculate and print on the screen the numbers that compose the sieve
# of Eratosthenes.
#
# AUTHOR: Jose' Lopes de Oliveira Ju'nior - http://versaopropria.blogspot.com
#
# CONTACT: jlojunior _at_ gmail _dot_ com
#
# DATE: 2008-09-30
#
# LICENCE: GPLv3 - http://www.gnu.org/licenses/gpl.html
#
#    For more information about the Sieve of Eratosthenes, plase visit its page
# on Wikipedia: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
###############################################################################

import math

def fill_list(lim=10):
    """Fill a list with values from 2 to lim.
    
    Requires the limit.
    
    """
    
    list = []
    
    for index in range(2, lim + 1):
        list.append(index)
    
    return list

def sieve_of_eratosthenes(lim=10):
    """Calculate Sieve of Eratosthenes.
    
    Returns a list with the primes between 2 and lim, which is passed by
    parameter.
    
    """
    # Create the list of values and calculate the square root of the
    # +limit. 
    sieve = fill_list(lim)
    limit = int(math.sqrt(lim))
    
    # The 1st for structure will iterate till the square root of the limit.
    # +The 2nd for structure will iterate till the limit.
    for index1 in range(0, limit):
        
        # Jump zeroes.
        if not sieve[index1]:
            continue
        
        for index2 in range(index1 + 1, lim - 1):
            
            if sieve[index2] and (not (sieve[index2] % sieve[index1])):
                sieve[index2] = 0
    
    return remove_zeros(sieve)

def remove_zeros(list):
    """Remove zeros from the list passed.
    
    Requires the list of integers.
    
    """
    
    list2 = []
    
    for index in range(len(list)):
        
        if list[index]:
            list2.append(list[index])
    
    return list2