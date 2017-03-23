# Analisa o escopo de variaveis numa funcao.

x = 1 # Variavel global

# Altera o valor da variavel local x, sem alterar a variavel global
def a(): 
   x = 25 

   print "\nlocal x in a is", x, "after entering a" 
   x += 1 
   print "local x in a is", x, "before exiting a" 

# Altera o valor da variavel global x
def b(): 
   global x 

   print "\nglobal x is", x, "on entering b" 
   x *= 10 
   print "global x is", x, "on exiting b" 

print "global x is", x 

x = 7 
print "global x is", x 

a() 
b() 
a() 
b() 

print "\nglobal x is", x