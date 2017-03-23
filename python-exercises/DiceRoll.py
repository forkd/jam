# Simula o rolamento de uma quantidade de dados definida pelo usuario.

import random # Importa o modulo de geracao automatica de numeros.

# Le a quantidade de dados a ser rolada.
rolls = int( raw_input( "Entre com o numero de rolagens: " ) )

for i in range( 1, rolls + 1 ) :
    print "%10d" % ( random.randrange( 1, 7 ) ),
    
    # Solta uma linha entre cada 4 rolagens.
    if not ( i % 8 ) :
        print