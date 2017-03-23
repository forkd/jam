# -*- Mode: Python -*- 
# -*- coding: utf-8 -*- 
# vi:si:et:sw=4:sts=4:ts=4 


"""Prepares an HTML code to use with SyntaxHighlighter."""


__author__ = "José Lopes de Oliveira Júnior (jlojunior _at_ gmail.com)"
__version__ = "$Revision: 2008.1 $"
__date__ = "$Date: 2008/11/22 17:38:39 $"
__website__ = "http://versaopropria.blogspot.com"
__licence__ = "GPLv3"


import os


print "\nStage 1/3: Opening files... ",

# Checking parameters
if len(os.sys.argv) == 3:
    input = open(os.sys.argv[1], 'r')
    output = open(os.sys.argv[2], 'w')

else:
    print "[error]"
    print "Use: $python %s PATH_TO_INPUT PATH_TO_OUTPUT" % os.sys.argv[0]
    exit(1)

print "[done]"

print "Stage 2/3: Reading input file... ", 

records = input.readlines()

print "[done]"

print "Stage 3/3: Writing output file... ", 
for record in records:
    output.write(record.replace('<', "&lt;").replace('>', "&gt;").
                 replace('"', "&quot;"))

print "[done]"

print "\nOutput written in %s." % os.path.abspath(os.sys.argv[2])

input.close()
output.close()