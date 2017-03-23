class Coordinate:
    def __init__(self):
        self.x = -1
        self.y = -1
    
    def set_x(self, new_x):
        if not new_x < 0:
            self.x = new_x
        else:
            raise ValueError, "Less than zero is not allowed: %d" % new_x
    
    def set_y(self, new_y):
        if not new_y < 0:
            self.y = new_y
        else:
            raise ValueError, "Less than zero is not allowed: %d" % new_y

class Token:
    
    types = ["general class command", 
             "non-structured command", 
             "iteration command",
             "object manipulation command", 
             "register manipulation command", 
             "conditional command",
             "unit command",
             "numerical constant",
             "variables declaration",
             "delimiter",
             "command block delimiter",
             "command delimiter",
             "commentary delimiter",
             "parameters delimiter",
             "id",
             "operation anulator id",
             "ASCII char id",
             "hexadecimal number id",
             "indicador de faixa de valores",
             "pointers manipulation",
             "arithmetical operator",
             "assignment operator",
             "boolean operator",
             "logical operator",
             "relational operator",
             "low level programming",
             "invalid character",
             "invalid id"]
    
    # The reserved words of the Pascal language.
    RESWORDS = [# Command block delimiters - 0..1
                "begin", "end",  
                # Variables declaration - 2..18
                "var", "string", "function", "procedure", "const", "type", 
                "array","record", "set", "file", "uses", "program", "unit", 
                "label","packed","library", "exports", 
                # Iteration commands - 19..24
                "for", "to", "downto", "repeat", "until", "while", 
                # Conditional commands - 25..28
                "if", "then", "else", "case", 
                # Boolean operators - 29..32
                "not", "and", "or", "xor",
                # Arithmetical operators - 33..34
                "mod", "div", 
                # Relational operator - 35
                "in", 
                # Logical operators - 36..37
                "shl", "shr",
                # Pointers manipulation - 38
                "nil", 
                # Miscelaneous commands - 39..40
                "of", "do", 
                # Unit commands - 41..42
                "implementation", "interface", 
                # Register manipulation commands - 43
                "with", 
                # Non-structured command - 44
                "goto", 
                # Objects manipulation commands - 45..48
                "constructor", "destructor", "inherited", "object", 
                # Low level programming - 49..50
                "asm", "inline"]
    
    def __init__(self):
        self.name = ""
        self.type = ""
        self.value = -1
        self.coordinate = Coordinate()