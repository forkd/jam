# Recebe do usuario os resultados dos testes de um dado numero de alunos,
# +indicando se cada um passou ou nao num exame de licenciatura. Caso tenha
# +passado, o usuario indica o numero 1. Caso tenha falhado, e' indicado o
# +numero 2. Ao final, o programa conta quantos resultados de aprovados/repro-
# +vados, exibindo-os na tela.

# Le o nemro de alunos de grupo.
grupo = int( raw_input( "Entre com o numero de alunos do grupo (<1 sai): " ) )

# Verifica se o usuario solicitou a saida do programa
if grupo < 1 :
    print "Saida solicitada pelo usuario."
    exit()

apr = 0 # Conta o numero de alunos aprovados
rep = 0 # Conta o numero de alunos resprovados
res = 0 # Armazena cada resposta do usuario dentro do laco while
i = 1   # Contra a iteracao do laco while

# Itera de 1 ate o numero total do grupo, lendo e contando o numero de apro-
# +vacoes e reprovacoes de alunos.
while i <= grupo :
    # Le a resposta do usuario
    res = int( raw_input( "Situacao do aluno %d - \
(1) Aprovado ou (2) Reprovado: " % i ) )
    
    # Analisa a resposta, atualizando a variavel correta
    if res == 1 :
        apr += 1
        i += 1
        
    elif res == 2 :
        rep += 1
        i += 1
        
    else :
        print "Resultado invalido. Digite novamente."

# Imprimindo o resultado para o usuario.
print "Numero de alunos aprovados :", apr
print "Numero de alunos reprovados:", rep

# Mostra uma mensagem, de acordo com o numero de aprovacoes/reprovacoes.
if apr > rep :
    print "Parabens! O numero de aprovacoes foi maior que o de reprovacoes!"

elif apr < rep :
    print "Precisamos melhorar! O numero de aprovacoes foi menor que o de \
reprovacoes."

else :
    print "Podemos melhorar! O numero de aprovacoes foi igual ao de \
reprovacoes."