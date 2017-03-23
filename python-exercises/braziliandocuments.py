from modulus import *

# CPF
def check_cpf(cpf):
    
    if cpf[9] == mod11(cpf[:9], 10) and cpf[10] == mod11(cpf[:10], 11):
        return True
    
    else:
        return False

def generate_cpf(cpf):
    
    cpf.append(mod11(cpf, 10))
    cpf.append(mod11(cpf, 11))
    
    return cpf

def format_cpf(cpf, flag=0):
    if not flag:
        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % (cpf[0], cpf[1], cpf[2], cpf[3], 
                                              cpf[4], cpf[5], cpf[6], cpf[7], 
                                              cpf[8], cpf[9], cpf[10])
    
    else:
        return "%d%d%d%d%d%d%d%d%d%d%d" % (cpf[0], cpf[1], cpf[2], cpf[3], 
                                           cpf[4], cpf[5], cpf[6], cpf[7], 
                                           cpf[8], cpf[9], cpf[10])

# CNPJ
def check_cnpj(cnpj):
    
    if cnpj[12] == mod11(cnpj[:12], 9) and cnpj[13] == mod11(cnpj[:13], 9):
        return True
    
    else:
        return False

def generate_cnpj(cnpj):
    
    cnpj.append(mod11(cnpj, 9))
    cnpj.append(mod11(cnpj, 9))
    
    return cnpj

def format_cnpj(cnpj, flag=0):
    if not flag:
        return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % (cnpj[0], cnpj[1], 
                                                     cnpj[2], cnpj[3],
                                                     cnpj[4], cnpj[5], 
                                                     cnpj[6], cnpj[7], 
                                                     cnpj[8], cnpj[9], 
                                                     cnpj[10], cnpj[11], 
                                                     cnpj[12], cnpj[13])
    
    else:
        return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % (cnpj[0], cnpj[1], 
                                                 cnpj[2], cnpj[3],
                                                 cnpj[4], cnpj[5], 
                                                 cnpj[6], cnpj[7], 
                                                 cnpj[8], cnpj[9], 
                                                 cnpj[10], cnpj[11], 
                                                 cnpj[12], cnpj[13])

# Titulo Eleitoral
def check_te(te):
    
    if te[10] == mod11(te[:8], 9) and te[11] == mod11(te[8:11], 9):
        return True
    
    else:
        return False
    
def generate_te(te):
    
    te.append(mod11(te[:8], 9))
    te.append(mod11(te[8:11], 9))
    
    return te

def format_te(te, flag=0):
    if not flag:
        return "%d%d%d%d%d%d%d%d%d%d-%d%d" % (te[0], te[1], te[2], te[3], 
                                              te[5], te[6], te[6], te[7],
                                              te[8], te[9], te[10], te[11])
    
    else:
        return "%d%d%d%d%d%d%d%d%d%d%d%d" % (te[0], te[1], te[2], te[3], 
                                             te[5], te[6], te[6], te[7],
                                             te[8], te[9], te[10], te[11])

# Main

#cpf = [0,6,6,4,4,3,1,5,6]
#print check_cpf(generate_cpf(cpf))
#print format_cpf(generate_cpf(cpf), 1)

#cnpj = [1,8,7,8,1,2,0,3,0,0,0,1]
#print check_cnpj(generate_cnpj(cnpj))
#print format_cnpj(generate_cnpj(cnpj))

te = [1,4,7,6,8,3,1,5,0,2]
print check_te(generate_te(te))
print format_te(generate_te(te))