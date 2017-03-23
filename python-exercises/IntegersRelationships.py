# Pede dois inteiros ao usuario e entao os compara, retornando os resultados.

print "Entre com 2 inteiros e eu lhe direi a relacao entre eles."

# Le o primeiro inteiro do usuario, convertendo-o para integer.
n1 = int( raw_input( "Entre com o 1o inteiro: " ) )

# Idem ao n1.
n2 = int( raw_input( "Entre com o 2o inteiro: " ) )

if n1 == n2 :
    print "%d eh igual a %d." % ( n1, n2 )

if n1 != n2 :
    print "%d eh diferente de %d." % ( n1, n2 )

if n1 < n2 :
    print "%d eh menor que %d." % ( n1, n2 )

if n1 > n2 :
    print "%d eh maior que %d." % (n1, n2 )

if n1 <= n2 :
    print "%d eh menor ou igual a %d." % ( n1, n2 )

if n1 >= n2 :
    print "%d eh maior ou igual a %d." % ( n1, n2 )