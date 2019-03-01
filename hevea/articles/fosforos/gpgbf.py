#!/usr/bin/python
#gpgbf.py


import subprocess as su
import itertools as it
import string as st
import sys


class BruteForce(object):
    """Attacks a GnuPG symmetrically-encrypted file.

    Author: Jose' Lopes de Oliveira Jr. <jlojunior@gmail.com>
    License: GPLv3+

    """
    def __init__(self, f):
        """Builds up the object.
        
        Keyword arguments:
        f -- a GnuPG symmetrically-encrypted file

        """
        try:
            with open(f) as aux: self.f = f
        except IOError:
            print('ERROR: Cannot access file {0}'.format(f))
            exit(1)

        self.command = 'echo {0} |gpg --batch --passphrase-fd 0\
                                      --output=/tmp/{1}\
                                      {1} 2> /dev/null'

    def gen_passwds(self, charset, ml):
        """Creates an iteration according to parameters.

        Keyword arguments:
        charset -- the charset used to build iteration
        ml (maxlength) -- results will have from 1 to ml chars

        Returns a list with the generated iterations.
        Author: Rafael Alencar <rafael-labs.com>

        """
        return (''.join(candidate)
                for candidate in
                    it.chain.from_iterable(it.product(charset,
                                                      repeat=i)
                                           for i in range(1,
                                                          ml + 1)))

    def attack(self):
        """Do the attack itself."""
        for passwd in self.gen_passwds(st.ascii_lowercase + 
                                      '0123456789', 6):
            try:
                print('Trying: {0}'.format(passwd))
                su.check_output(self.command.format(passwd,
                                                    self.f),
                                        shell=True)
            # When the file cannot be decrypted --bad
            # password--, an exception is raised:
            # subprocess.CalledProcessError.
            except: pass
            else:
                print('YIPPEE KI-YAY! This is the password!')
                su.call(['rm', '-rf', '/tmp/{0}'.format(self.f)])
                return 0

        print('Unable to determine password. :(')
        return 1


##
# MAIN
#
if __name__ == '__main__':
    exit(BruteForce(sys.argv[1]).attack())
