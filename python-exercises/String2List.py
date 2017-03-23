# Transforma uma string composta por algarismos em uma lista de numeros in-
# +teiros.

import string    

def str2IntList ( string ) :
    list = [] # Uma lista vazia para ser preenchida pelos caracteres da string.
    
    for index in range ( len( string ) ) :
        list += [ int( string[ index ] ) ]
    
    return list

cpf = raw_input( "Entre com um numero de CPF - apenas os 9 1os digitos: " )

if not cpf.isdigit() :
    print "Entre APENAS com os digitos!"
    exit()

print str2IntList( cpf )