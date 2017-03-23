# Autor
#    Jose Lopes de Oliveira Junior
#
# Creditos
#    Baseado no livro Python: How to Program, 1a. edicao.
#
# Data
#    2008/09/14
#
# Descricao
#    Simula um jogo de Craps.
#    Regras:
#    - Sao rolados 2 dados de 6 faces e os resultados sao somados.
#    - Se a soma for 7 ou 11, no primeiro lance, o jogador ganha.
#    - Se a soma for 2, 3 ou 12 (Craps), a casa ganha.
#    - Se der qualquer outro resultado no primeiro lance, a soma vira a pontua-
#      +cao do jogador. Entao os dados devem ser jogados novamente ate que:
#      - O jogador consiga igualar a sua pontuacao, vencendo o jogo ou...
#      - Que a soma de 7, quando o jogador perde.
#
# Sistema de Desenvolvimento/Testes
#    OS X 10.5.4 (Leopard), com interpretador Python v2.5.
################################################################################

import random # Modulo de geracao de numeros aleatorios.

# Executa a rolagem dos dados, imprimindo o resultado de cada dado na tela e\
# +retornando a soma dos resultados.
def rollDice () :
    # Rola os dois dados e soma os resultados
    die1 = random.randrange( 1, 7 )
    die2 = random.randrange( 1, 7 )
    workSum = die1 + die2
    
    # Imprime os dados na tela
    print "O jogador rolou %d + %d = %2d ---" % ( die1, die2, workSum ),
    
    # Aguarda que o jogador pressione <Enter> para continuar
    raw_input( "Pressione <Enter> para continuar..." )
    
    return workSum # Retorna a soma dos resultados obtidos

# Corpo principal do programa.

# Executa a primeira rolagem e guarda o resultado.
sum = rollDice()

# Processa o resultado
if sum == 4 or sum == 5 or sum == 6 or sum == 8 or sum == 9 or sum == 10 :
     playerPoint = sum # Anota a pontuacao obtida pelo jogador
     # Define o estado do jogo: -1: Casa; 0 = Continua; 1 = Jogador
     gameStatus = 0

elif sum == 7 or sum == 11 :
    gameStatus = 1 # Jogador ganha

else :
    gameStatus = -1 # Casa ganha

# Itera ate que o jogador ou a casa ganhem.
while not gameStatus :
    sum = rollDice() # Rola os dados e anota o resultado
    
    # Processa o resultado
    if sum == playerPoint:
        gameStatus = 1 # Jogador vence
    
    elif sum == 7 :
        gameStatus = -1 # Casa vence

# Verifica o resultado final e imprime a mensagem adequada na tela.
if gameStatus == 1 :
    print "Parabens! Voce venceu! :-)"

else :
    print "A casa venceu. :-("