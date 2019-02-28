# Jam
A bunch of small or deprecated codes.  There is no guarantee these pieces of code will work.  In fact, most of them should not work.  And it's ok.  :)

-----
## Notary
The purpose of this project is to set-up a simple Certificate Authority (CA) using OpenSSL to easily issue digital certificates to test applications such as digital signature services.

Each CA created with Notary has a structure like this:

```
CA
  /certs
  /crl
  /newcerts
  /private
  /index.txt
  /openssl.cnf
  /serial
```

Where `certs` stores issued certificates, `crl` has all versions of certificate revocation lists (CRLs) issued by that particular CA, `newcerts` has no use at this moment, `private` stores the private keys generated, `index.txt` is something like a database for issued certificates, and `serial` is a database for certificate serial numbers.

### Setting up a Root CA
The example below will create a root CA named `FOO` in /tmp.

```shell
$ notary.py --create root --name FOO --target /tmp
```

Note that you'll be asked to insert a password for the CA's private key.  Do not forget it!

### Setting up an Intermediate CA
An intermediate CA needs a root CA to be associated with.  The command below creates an intermediate CA named `BAR` issued by the root CA `FOO`.

```shell
$ notary.py --create inter --name BAR --root /tmp/FOO --target /tmp
```

You'll be asked to type the root CA's private key password and to define a password for this intermediate CA.  Remember it!

### Issuing a CRL
The example below will issue a CRL for `BAR` CA.

```shell
$ notary.py --crl --target /tmp/BAR
```

It'll require the password for `BAR` CA private key.


-----
## License
All files are released under MIT license.  Third party softwares have their own licenses.
