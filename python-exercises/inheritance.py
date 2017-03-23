class A:
    def __init__(self):
        self.a = 9

class B (A):
    def __init__(self):
        A.__init__(self)
        self.b = 8

class C(B):
    def __init__(self):
        B.__init__(self)
        self.c = 7

print issubclass(C,A)
print B.__bases__
print C.__bases__
z = C()
print z.a, z.b, z.c