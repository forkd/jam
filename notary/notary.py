#!/usr/bin/env python3
# notary.py
#
# AUTHOR: José Lopes de Oliveira Júnior <forkd@tuta.io>
# LICENSE: GPLv3+
##


import os
import shutil
import fileinput
import subprocess
import argparse
from getpass import getpass



##
# FUNCTIONS
#

mkdir = lambda x: os.makedirs(x, exist_ok=True)

def builder(target, name, flag):
    '''Build a structure for root or intermediate CA.
    flag must be 'root' or 'inter'.

    '''

    for d in ['certs', 'crl', 'newcerts', 'private']:
        # try/except: directory exists and has write permissions?
        mkdir('{0}/{1}/{2}'.format(target, name, d))

    os.chmod('{0}/{1}/private'.format(target, name), 0o700)
    open('{0}/{1}/index.txt'.format(target, name), 'w').close()

    with open('{0}/{1}/serial'.format(target, name), 'w') as f:
        f.write(str(os.popen('openssl rand -hex 16').read()))


    shutil.copy2('cnf/{0}-openssl.cnf'.format(flag),
                 '{0}/{1}/openssl.cnf'.format(target, name))
    os.chdir('{0}/{1}'.format(target, name))

def mkroot(target='/tmp', name='root'):
    '''Create a root certificate authority structure.'''
    passwd = getpass('Enter password for root\'s private key: ')
    install_dir = os.getcwd()
    builder(target, name, 'root')

    with fileinput.input('openssl.cnf', inplace=True) as f:
        for line in f:
            print(line.replace('{{name}}', name).replace('{{path}}',
                  '{0}/{1}'.format(target, name)), end='')

    # create private key
    subprocess.call(['openssl', 'genrsa', '-aes256', '-out',
                     'private/{0}.key.pem'.format(name), '-passout',
                     'pass:{0}'.format(passwd), '4096'], shell=False,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chmod('private/{0}.key.pem'.format(name), 0o400)

    # create root certificate
    subprocess.call(['openssl', 'req', '-batch', '-config', 'openssl.cnf',
                     '-key', 'private/{0}.key.pem'.format(name), '-passin',
                     'pass:' + passwd, '-new', '-x509', '-days', '7300',
                     '-sha256', '-extensions', 'v3_ca', '-out',
                     'certs/{0}.cert.pem'.format(name)], shell=False,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chmod('certs/{0}.cert.pem'.format(name), 0o444)

    os.chdir(install_dir)

    print('''
    Root certificate created.  Run the command below to verify it:
    $ openssl x509 -noout -text -in {0}/{1}/certs/{1}.cert.pem
    '''.format(target, name))

def mkinter(target, name, root):
    '''Create an intermediate certificate authority structure.
    root: path to root CA.

    '''

    passwd = getpass('Enter password for intermediate\'s private key: ')
    install_dir = os.getcwd()
    builder(target, name, 'inter')

    with fileinput.input('openssl.cnf', inplace=True) as f:
        for line in f:
            print(line.replace('{{name}}', name).replace('{{path}}',
                  '{0}/{1}'.format(target, name)).replace('{{uri_crl}}',
                  'https://domain/crl').replace('{{uri_ocsp}}',
                  'https://ocsp.domain'), end='')

    # create private key
    subprocess.call(['openssl', 'genrsa', '-aes256', '-out',
                     'private/{0}.key.pem'.format(name), '-passout',
                     'pass:{0}'.format(passwd), '4096'], shell=False,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chmod('private/{0}.key.pem'.format(name), 0o400)

    # intermediate CA sign request
    subprocess.call(['openssl', 'req', '-batch', '-config', 'openssl.cnf',
                     '-new', 'sha256', '-key', 'private/{0}.key.pem',
                     '-out', 'csr/{0}.csr.pem'], shell=False,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # create intermediate certificate
    subprocess.call(['openssl', 'ca', '-batch', '-config',
                     '{0}/openssl.cnf'.format(root), '-extensions',
                     'v3_intermediate_ca', '-days', '3650', '-notext',
                     '-md', 'sha256', '-in', 'csr/{0}.csr.pem'.format(name),
                     '-out', 'certs/{0}.cert.pem'.format(name)], shell=False,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chmod('certs/{0}.cert.pem'.format(name), 0o444)

    # create chain file
    with open('certs/{0}-chain.cert.pem'.format(name), 'w') as f:
        f.write(open('certs/{0}.cert.pem'.format(name)).read() +
            open('{0}/certs/{1}.cert.pem'.format(root,
                os.path.basename(os.path.normpath(root)))).read())

    os.chdir(install_dir)

    print('''
    Intermediate certificate created.  Run the command below to verify it:
    $ openssl x509 -noout -text -in {0}/{1}/certs/{1}.cert.pem
    '''.format(target, name))

def mkcrl(target):
    '''Create a new version for a CA's certificate revocation list.'''
    count = 0
    while (os.path.exists('crl/{0}.crl.pem'.format(count))): count += 1

    subprocess.call(['openssl', 'ca', '-config',
                     '{0}/openssl.cnf'.format(target), '-gencrl', '-out',
                     '{0}/crl/{1}.crl.pem'.format(target, count)])#, shell=False,                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print('''
    Certificate revocation list created.  Run the command below to verify it:
    $ openssl crl -in {0}/crl/{1}.crl.pem -noout -text
    '''.format(target, count))

##
# MAIN
#
parser = argparse.ArgumentParser(description='Notary')
parser.add_argument('--create', '-c',
    choices=['root', 'inter'],
    help='create a root or intermediate CA')
parser.add_argument('--name', '-n',
    help='structure name')
parser.add_argument('--target', '-t',
    default='/tmp',
    metavar='PATH',
    help='destination path')
parser.add_argument('--root', '-r',
    default='/tmp/root',
    metavar='PATH',
    help='root CA path')
parser.add_argument('--inter', '-i',
    default='/tmp/inter',
    metavar='PATH',
    help='intermediate CA path')
parser.add_argument('--issue', '-s',
    choices=['user', 'server'],
    help='will issue a certificate')
parser.add_argument('--id', '-d',
    metavar='ID',
    help='certificate id')
parser.add_argument('--revoke', '-k',
    metavar='ID',
    help='revoke a certificate')
parser.add_argument('--crl', '-l',
    action='store_true',
    help='issue a new certificate revocation list')

args = parser.parse_args()

if (args.create):
    if (args.create == 'root'): mkroot(args.target, args.name)
    else: mkinter(args.target, args.name, args.root)

elif (args.crl):
    mkcrl(args.target)

else:
    print('Will not create.\n' + str(args))
