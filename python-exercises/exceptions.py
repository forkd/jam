class Example:
    def __init__(self): self.a = "Attribute"
    def __str__(self): return self.a

def printer(p): print p

example = Example()

printer("String")
printer(5)
print(example)

exit(0)

while True:
    try:
        name = raw_input("Enter with your name: ")
        assert 3 <= len(name) <= 31
    
    except AssertionError:
        print "Name length must be between 3 and 31 chars."
    
    else:
        break
    
print name