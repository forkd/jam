# Gera um numero aleatorio entre 1 e 1000 e pede que o usuario o adivinhe em
# +ate' 10 chances.

import random # Modulo de numeros aleatorios

# Gera um numero aleatorio entre 1 e 1000
num = random.randrange( 1, 1001 )

count = 0 # Conta quantas o numero de tentativas
gameStatus = 0 # Estado do jogo: 0 - Em jogo; -1 - Derrota; 1 - Vitoria

# Itera ate' que se completem todas as tentativas ou que o jogador acerte o
# +numero.
for count in range( 1, 11 ) :
    # Le a resposta do usuario
    res = int( raw_input( "Tentativa %d/10. O numero eh: " % count ) )
    
    if res == num : # Verifica se o usuario acertou
        gameStatus = 1 # Acertou! Estado de acerto
        break # Termina a iteracao
    
    elif res < num : # Usuario digitou um numero muito pequeno
        print "Errado. Dica: O numero esta entre %d e 1000!" % ( res + 1 )
    
    else : # Usuario digitou um numero muito grande
        print "Errado. Dica: O numero esta entre 1 e %d!" % ( res -1 )

if not gameStatus : # Se o usuario nao acertou, entao perdeu o jogo
    gameStatus = -1

print # Solta uma linha para imprimir o resultado.

if gameStatus == -1 :
    print "Voce perdeu. O numero era %d." % num

elif 6 <= count <= 10 :
    print "Voce conseguiu, mas pode melhorar!"

elif 2 <= count <= 5 :
    print "Voce eh um otimo jogador!"

else:
    print "Parabens! Voce conseguiu na primeira tentativa!"