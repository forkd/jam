def gcd(n1, n2):
    if not n2: return n1
    
    while n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    
    return n1


a = int(raw_input("Entre com o primeiro numero: "))
b = int(raw_input("Entre com o segundo numero : "))

if a > b:
    mdc = gcd(a,b)
else:
    mdc = gcd(b,a)

print "MDC de %d e %d = %d" % (a, b, mdc)

if mdc == 1:
    print "Os numeros sao primos entre si!"