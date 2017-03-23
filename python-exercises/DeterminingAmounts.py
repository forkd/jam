# Calcula o lucro de 5% ao ano, ao longo de um determinado periodo, para uma
# +quantia determinada.

# Le a quantia inicial.
qini = float( raw_input( "Entre com a quantia inicial: " ) )

# Le o tempo de investimento, somando 1, para controle do laco for.
anos = int( raw_input( "Entre com o tempo em anos do investimento: " ) ) + 1

# Le a porcentagem de interesse por ano.
irt = float( raw_input( "Entre com a taxa anual de interesse: " ) )

# Imprime o cabecalho da saida.
print "Ano %21s" % "Montante"

# Para agilizar a execucao do laco for, a expressao
#    montante = qini * ( 1.0 + irt ) ** ano
# pode ser reduzida com o auxilio de uma variavel que armazena a parte
# +constante da expressao: (1.0 + irt).
spd = 1.0 + irt

# Varia de 1 ate anos - 1, calculando e imprimindo o novo saldo.
for ano in range ( 1, anos ) :
    montante = qini * spd ** ano # Calcula o montante
    print "%4d%21.2f" % ( ano, montante )  # Imprime para o usuario