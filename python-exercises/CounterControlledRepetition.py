# Calcula a media de notas de determinado grupo de alunos.

# Lendo quantos estudantes compoem a classe
grupo = int( raw_input( "Entre com o numero de estudantes da classe (-1 sai): "\
                         ) )

# Verificando se o usuario solicitou a saida do programa.
if grupo == -1 :
    print "Nenhum resultado somado." # Mensagem de saida para o usuario
    exit() # Sai do programa

i = 1    # Variavel de controle da iteracao
soma = 0 # Armazena a soma das notas dos alunos

# Le as notas de todos os alunos da classe, somando cada resultado.
while i <= grupo :
    # Le a nota de um aluno e a soma com o montante.
    soma += int( raw_input( "Entre com a nota no aluno %2d: " % i ) )
    
    i += 1 # Incrementa a variavel de controle

# Imprime o resultado para o usuario.
print "A media foi de %.2f." % ( float( soma ) / grupo )