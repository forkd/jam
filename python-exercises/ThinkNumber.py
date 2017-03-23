raw_input("Pense num numero.")

raw_input("Multiplique o numero por 3.")
first = raw_input("Eh [p]ar ou [i]mpar? ")
if first == 'p' or first == 'P':
    raw_input("Divida este novo numero por 2.")
else:
    raw_input("Some 1 e divida este novo numero por 2.")
    
raw_input("Multiplique o numero por 3.")
second = raw_input("Eh [p]ar ou [i]mpar? ")
if second == 'p' or second == 'P':
    raw_input("Divida este novo numero por 2.")
else:
    raw_input("Some 1 e divida este novo numero por 2.")

quociente = int(raw_input("Divida o resultado por 9 e considere o quociente \
inteiro. Digite-o: "))

if first == 'p' or first == 'P':
    if second == 'p' or second == 'P':
        print "Voce pensou em %d." % (quociente * 4)
        
    else:
        print "Voce pensou em %d." % (quociente * 4 + 2)

else:
    if second == 'p' or second == 'P':
        print "Voce pensou em %d." % (quociente * 4 + 1)
    else:
        print "Voce pensou em %d." % (quociente * 4 + 3)