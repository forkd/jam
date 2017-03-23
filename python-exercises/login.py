# http://www.python.org/doc/2.5.2/lib/module-crypt.html

import crypt, getpass, pwd

def login():
    username = raw_input('Python login: ')
    cryptedpasswd = pwd.getpwnam(username)[1]
    
    if cryptedpasswd:
        if cryptedpasswd == 'x' or cryptedpasswd == '*': 
            raise "Sorry, currently no support for shadow passwords"
        
        cleartext = getpass.getpass()
        
        return crypt.crypt(cleartext, cryptedpasswd) == cryptedpasswd
    
    else:
        return 1

login()