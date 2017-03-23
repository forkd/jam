# Cria e imprime a serie de Fibonacci de forma recursiva, na tela.

# Calcula a serie de Fibonacci recursivamente, onde n e' o numero de termos a
# +calcular.
def fibonacci ( n ) :
    if n < 0 :
        return -1
    
    elif n == 0 or n == 1 :
        return n
    
    else:
        return fibonacci ( n - 1 ) + fibonacci( n - 2 )

num = int( raw_input( "Entre com o numero de termos a calcular: " ) )

print "Fibonacci(%d): %d" % ( num, fibonacci( num ) )