# Exemplos de formatacao e criacao de strings.

print "This is a string with \"double quotes.\"" 
print 'This is another string with "double quotes."' 
print 'This is a string with \'single quotes.\'' 
print "This is another string with 'single quotes.'" 
print """This string has "double quotes" and 'single quotes'. 
You can even do multiple lines.""" 
print '''This string also has "double" and 'single' quotes.'''

inteiro = 11
print "Inteiro:", inteiro
print "Inteiro: %d" % inteiro
print "Inteiro %x\n" % inteiro

real = 3.141517
print "Real:", real
print "Real padrao: %f" % real
print "Real exponencial: %e\n" % real

print "Inteiro justificado a direita  ( %8d )" % inteiro
print "Inteiro justificado a esquerda ( %-8d )" % inteiro

str = "String formatada"
print "Forcando 8 digitos num inteiro: %.8d" % inteiro
print "5 Digitos depois do ponto num real: %.9f" % real
print "15 e 5 caracteres permitidos numa string:"
print "(%.16s) (%.6s)" % ( str, str )