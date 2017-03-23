# Gera uma lista de n numeros aleatorios.

import random

# Gera a lista de numeros aleatorios, cujo tamanho e' passado por parametro.
# +Alem disso, a funcao recebe os valores que o menor e o maior itens podem
# +receber - o escopo inclui o menor e exclui o maior item!
def genRandomList ( size = 10, minor = 0, more = 10 ) :
    list = [] # Cria uma lista em branco
    
    # Itera de 0 ate a quantidade passada pelo usuario.
    for index in range( size ) :
        # Gera um numero aleatorio e o insere na lista.
        list += [ random.randrange( minor, more ) ]
    
    return list # Retorna a lista preenchida.

cpf = genRandomList( 9 )
cnpj = genRandomList( 12 )
te = genRandomList()

print "CPF: %d%d%d.%d%d%d.%d%d%d" % ( cpf[ 0 ], cpf[ 1 ], cpf[ 2 ], cpf[ 3 ], \
                                      cpf[ 4 ], cpf[ 5 ], cpf[ 6 ], cpf[ 7 ], \
                                      cpf[ 8 ] )

print "CNPJ: %d%d.%d%d%d.%d%d%d.%d%d%d%d" % ( cnpj[ 0 ], cnpj[ 1 ], cnpj[ 2 ], \
                                              cnpj[ 3 ], cnpj[ 4 ], cnpj[ 5 ], \
                                              cnpj[ 6 ], cnpj[ 7 ], cnpj[ 8 ], \
                                              cnpj[ 9 ], cnpj[ 10 ], cnpj[ 11 ])

print "Titulo Eleitoral: %d%d%d%d%d%d%d%d%d%d" % ( te[ 0 ], te[ 1 ], te[ 2 ], \
                                                   te[ 3 ], te[ 4 ], te[ 5 ], \
                                                   te[ 6 ], te[ 7 ], te[ 8 ], \
                                                   te[ 9 ] )