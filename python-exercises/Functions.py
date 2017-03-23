# Le 3 valores do usuario (numeros ou strings) e entao retorna o maior valor
# +entre eles.

# Recebe 3 valores e retorna o maior.
def maximumValue ( x, y, z ) :
    max = x
    
    if y > x :
        max = y
    
    if z > max :
        max = z
    
    return max

# Testando a funcao maximumValue com valores inteiros.
a = int( raw_input( "Entre com o 1o inteiro: " ) )
b = int( raw_input( "Entre com o 2o inteiro: " ) )
c = int( raw_input( "Entre com o 3o inteiro: " ) )

# Testando a funcao com valores reais.
d = float( raw_input( "Entre com o 1o real: " ) )
e = float( raw_input( "Entre com o 2o real: " ) )
f = float( raw_input( "Entre com o 3o real: " ) )

# Testando com strings.
g = raw_input( "Entre com a 1a string: " )
h = raw_input( "Entre com a 2a string: " )
i = raw_input( "Entre com a 3a string: " )

# Imprimindo os resultados.
print "O maior valor entre %d, %d e %d e' %d. " % \
( a, b, c, maximumValue( a, b, c ) )

print "O maior valor entre %.2f, %.2f e %.2f e' %.2f. " % \
( d, e, f, maximumValue( d, e, f ) )

print "O maior valor entre %s, %s e %s e' %s. " % \
( g, h, i, maximumValue( g, h, i ) )