def zero_999(numb, flag=1):
    """Returns a string that represents the numb variable in ordinal or
    cardinal notation.
    
    numb must be between 0 and 999. flag must be 0 for ordinal notation or
    greater than zero for cardinal notation.
    
    """
    # Constants
    ZERO_NINETEEN = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis",
                     "sete", "oito", "nove", "dez", "onze", "doze", "treze",
                     "catorze", "quinze", "dezesseis", "dezessete", 
                     "dezoito", "dezenove"]
    TWENTY_NINETY_NINE = ["vinte", "trinta", "quarenta", "cinquenta", 
                          "sessenta", "setenta", "oitenta", "noventa"]
    TWO_NINE_HUNDRED = ["duzentos", "trezentos", "quatrocentos", "quinhentos", 
                        "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    ZERO_NINETH = ["zero", "primeiro", "segundo", "terceiro", "quarto", 
                   "quinto", "sexto", "setimo", "oitavo", "nono"]
    TENTH_NINETYTH = ["decimo", "vigesimo", "trigesimo", "quadragesimo", 
                      "quinquagesimo", "sexagesimo", "septuagesimo", 
                      "octogesimo", "nonagesimo"]
    ONE_NINE_HUNDREDTH = ["centesimo", "ducentesimo", "trecentesimo", 
                          "quadringentesimo", "quingentesimo", "sexcentesimo", 
                          "septingentesimo", "octingentesimo", 
                          "noningentesimo"]
    
    str = ""  # String that'll be returned.
    
    if flag:  # Cardinal
        if not numb:  # Catch 0
            str = ''.join([str,ZERO_NINETEEN[numb]])
        
        else:  # Catch 1..999
            while numb:
                if 1 <= numb <= 19:
                    str = ''.join([str, ZERO_NINETEEN[numb]])
                    break
                
                elif 20 <= numb <= 99:
                    str = ''.join([str, TWENTY_NINETY_NINE[numb / 10 - 2]])
                    numb %= 10
                    if numb:
                        str = ''.join([str, " e "])
                
                elif numb == 100:
                    str = ''.join([str, "cem"])
                    numb %= 100
                
                elif 101 <= numb <= 199:
                    str = ''.join([str, "cento e "])
                    numb %= 100
                
                elif 200 <= numb <= 999:
                    str = ''.join([str, TWO_NINE_HUNDRED[numb / 100 - 2]])
                    numb %= 100
                    if numb:
                        str = ''.join([str, " e "])
        
    else:  # Ordinal
        if not numb:  # Catch 0
            str = ''.join([str,ZERO_NINETH[numb]])
        
        else:  # Catch 1..999
            while numb:
                if 1 <= numb <= 9:
                    str = ''.join([str, ZERO_NINETH[numb]])
                    break
                
                elif 10 <= numb <= 99:
                    str = ''.join([str, TENTH_NINETYTH[numb / 10 - 1]])
                    numb %= 10
                    if numb:
                        str = ''.join([str, ' '])
                
                elif 100 <= numb <= 999:
                    str = ''.join([str, ONE_NINE_HUNDREDTH[numb / 100 - 1]])
                    numb %= 100
                    if numb:
                        str = ''.join([str, ' '])
    
    return str

def int2str(numb, flag=1):
    
    # Constants
    CARDINAL_MULTIPLIERS = ["mil", "milhao", "milhoes", "bilhao", "bilhoes"]
    ORDINAL_MULTIPLIERS = ["milesimo", "milionesimo", "bilionesimo"]
    
    str = ""  # Will be returned by the function.
    
    if flag:  # Cardinal
        while numb:
            if 0 <= numb <= 999:
                str = ''.join([str, zero_999(numb)])
                break
            
            elif 1000 <= numb <= 1999:
                str = ''.join([str, CARDINAL_MULTIPLIERS[0]])
                numb %= 1000
                
                # Separators
                if numb:
                    str = ''.join([str, ' '])
                    if (1 <= numb <= 99) or (not numb % 100):
                        str = ''.join([str, "e "])
            
            elif 2000 <= numb <= 999999:
                str = ''.join([str, zero_999(numb / 1000), ' ',
                               CARDINAL_MULTIPLIERS[0]])
                numb %= 1000
                
                # Separators
                if (101 <= numb <= 999) and (numb % 100):
                    str = ''.join([str,' '])
                
                elif numb:
                    str = ''.join([str," e "])
            
            elif 1000000 <= numb <= 1999999:
                str = ''.join([str, zero_999(1), ' ', 
                               CARDINAL_MULTIPLIERS[1]])
                numb %= 1000000
                
                # Separators
                if numb:
                    str = ''.join([str,' '])
                    if (1 <= numb <= 99) or (not numb % 1000):
                        str = ''.join([str, " e "])
                    elif
    else:  # Ordinal
        str = "Ordinal"
    
    return str

# Main
print int2str(110100)