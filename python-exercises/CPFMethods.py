import random

# Gera a lista de numeros aleatorios, cujo tamanho e' passado por parametro.
# +Alem disso, a funcao recebe os valores que o menor e o maior itens podem
# +receber - o escopo inclui o menor e exclui o maior item!
def generateRandomList(list=[], size=9, minor=0, more=10):
    lenList = len(list)
    
    if lenList >= size:
        return list[:size]
    
    # Itera de 0 ate a quantidade passada pelo usuario.
    for index in range(size):        
        if lenList < size:
            # Gera um numero aleatorio e o insere na lista.
            list += [random.randrange(minor, more)]
            
            lenList += 1
        else :
            break
    
    return list

def module11 ( list, maxMult = 10 ) :
    mult = 2 # Variavel multiplicadora de cada item da lista
    sum = 0  # Armazena o somatorio geral do produto de cada item pela variavel
             # +multiplicadora
    
    # A iteracao mapeia a lista do ultimo ate' o primeiro item.
    for index in range( ( len( list ) - 1 ) , -1, -1 ) :
        sum += list[ index ] * mult # Multiplica o item pela variavel multipli-
                                    # +cadora, adicionando o resultado ao soma-
                                    # +torio.
        mult += 1 # Atualiza a variavel multiplicadora
        
        # Verifica se a variavel multiplicadora atingiu o seu valor maximo. Se
        # +tiver atingido, a mesma e' reiniciada.
        if mult > maxMult :
            mult = 2
    
    # O resultado do somatorio deve ser multiplicado por 10 e dividido por 11,
    # +onde o resto dessa divisao deve ser guardado (modulo 11).
    sum = ( sum * 10 ) % 11
    
    # Caso o resultado da expressao anterior seja 10, o digito menos significa-
    # +tivo e' retornado (0). Caso contrario, o resultado da expressao sera'
    # +retornado. Esta etapa pode variar de acordo com a necessidade de cada
    # +empresa. O Banco do Brasil, por exemplo, retorna o valor X em vez do di-
    # +gito menos significativo.
    if sum > 9 :
        return 0
    
    else :
        return sum

def checkDocument ( doc, minLength ):
    if len( doc ) < minLength :
        return -1
    
#    if not doc.isdigit() :
#        return -2
    
    return 0

def str2IntList ( string ):
    list = []
    
    for index in range( len( string ) ):
        list += [ int( string[ index ] ) ]
    
    return list

def generateCPF ( cpf, rf = 1 ):
    lenCPF = len( cpf )
    
    if lenCPF == 9 :
        cpf += [ module11( cpf ) ]
        cpf += [ module11( cpf, 11 ) ]
    
    elif lenCPF == 8 :
        cpf += [ rf ]
        cpf += [ module11( cpf ) ]
        cpf += [ module11( cpf, 11 ) ]
    
    elif not lenCPF :
        cpf = generateRandomList( 9 )
        cpf += [ module11( cpf ) ]
        cpf += [ module11( cpf, 11 ) ]
    
    else:
        cpf = []
    
    return cpf

def validateCPF ( cpf ):
    cpfAux = generateCPF( cpf[ 0 : 9 ] )
    
    if cpf == cpfAux :
        return 0
    
    else :
        return -1

def formatCPF ( cpf ):
    return ( "%d%d%d.%d%d%d.%d%d%d-%d%d" ) % ( cpf[ 0 ], cpf[ 1 ], cpf[ 2 ], \
                                               cpf[ 3 ], cpf[ 4 ], cpf[ 5 ], \
                                               cpf[ 6 ], cpf[ 7 ], cpf[ 8 ], \
                                               cpf[ 9 ], cpf[ 10 ], )

###################
for i in range( 10 ):
    print formatCPF( generateCPF( generateRandomList([0,6,6,4,4,3,1,5]) ) ),
    if i == 4 : print
exit( 0 )