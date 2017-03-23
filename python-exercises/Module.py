# Obtem o modulo de determinada sequencia numerica.

def modulus10 ( list ) :
    sum = 0 # Armazena o somatorio geral do produto de cada item da lista, por
            # +um ou por dois, dependendo do indice.
    
    # Itera do inicio ao final da lista, calculando de acordo com o indice (par
    # +ou impar).
    for index in range( len( list ) ) :
        # Caso o indice seja par, o item e' adicionado ao somatorio diretamente.
        # +Caso seja impar, o indice e' multiplicado por 2. Se o resultado for
        # +maior que 9, e' realizada a prova dos nove com o mesmo e este resul-
        # +tado e' adicionado ao somatorio geral.
        if index % 2 : # Indice par
            sum += list[ index ]
        
        else : # Indice impar
            if list[ index ] > 4 : # Resultado maior que 9
                sum += ( list[ index ] * 2 ) - 9
            
            else : # Resultado menor que 9
                sum += list[ index ] * 2
    print sum
    # Com o somatorio gerado, deve-se dividi-lo por 10 e guardar o resto da di-
    # +visao (modulo 10).
    mod = sum % 10
    
    # Se o modulo 10 do somatorio for diferente de 0, retorna-se quanto falta
    # +para que o resultado seja igual a 10. Caso contrario, retorna-se 0.
    if mod :
        return 10 - mod
    
    else :
        return mod

def modulus11 ( list, maxMult = 10 ) :
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

#print module10( [ 1, 8, 7, 8, 1, 2, 0 ] )
#print module10( [ 2, 6, 1, 5, 3, 3 ] )
#print module11( [ 2, 6, 1, 5, 3, 3 ] )
#print module11( [ 0,6,6,4,4,3,1,5,6 ] )
#print module11( [ 0,6,6,4,4,3,1,5,6,9 ], 11 )
#print module11( [ 3,7,8,4,5,2,4,3,8 ] )
#print module11( [ 3,7,8,4,5,2,4,3,8,9 ], 11 )
#print module11( [ 1,3,5,8,4,3,8,1,6,1 ], 11 )
#print module11( [1,1,1,1,1,1,1,1,1,1],11)

#print modulus11([0,2,0,2,0,1,0,6,9])
#print modulus11([2,0,2,0,1,0,6,9])

print modulus11([0,2,0,2,0,5,0,0,1])