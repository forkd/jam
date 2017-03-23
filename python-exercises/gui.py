import easygui

import Eratosthenes

sieve = Eratosthenes.sieve_of_eratosthenes(easygui.integerbox("Enter with the \
sieve's limit", "User interaction", 0, 0, 10000))

str = "\t-\t".join(["%s" % index for index in sieve])

easygui.msgbox(str)