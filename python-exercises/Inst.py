from Class import Person

person = Person()

person._name = "j"
person._cpf = [0,6,6,4,4,3,1,5,6,9,0]

print person.print_name()
print person.print_cpf()
print Person.__dict__
