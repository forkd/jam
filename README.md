# Jam
A bunch of small or deprecated codes.  There is no guarantee these pieces of code will work.  In fact, most of them should not work.  And it's ok.  :)


-----
## Windows Registry Fixer
A simple and obsolete system to edit Windows Registry.  Windows Registry Fixer (WRF) is a Python module which implements many Windows registry keys, to be used to generate a .reg file with some handful setups to sysadmins.

### GTK WRF (GWRF)
It's just a GTK interface to WRF, capable to automate the script generation.  Please note that all options are implemented with checkbuttons and some must be configurated through text boxes.  In this last case some rules must be followed:

1. "Cached logons count": only integer numbers are allowed.
2. "SRV comment", "Logon prompt", "Legal notice": strings are allowed.
3. "Exclude profile directories": paths must be separated by semicolons.
4. "Disallow run", "Restrict run": program names must be separated by semicolons, with no spaces between them.
5. "Wallpaper image and style", "Logon wallpaper and style": the first parameter sets the "tiled" property --0 or 1--; the second parameter is wallpaper path --must be a bitmap image (.bmp)--; the last parameter sets the wallpaper style --(0) centered, (1) side-by-side, (2) extended--; do not use spaces between semicolons and program names.
6. "Change special directories path": directory must be set followed by a semicolon and the new path.
7. "About" button: opens a window with developer information.
8. "Help" button: opens your default browser with Google Code URL.
9. "Apply" button: creates the wrf.reg file according to all parameters.

## Note
I wrote this piece of software as my final paper at [UFLA](http://repositorio.ufla.br/jspui/handle/1/5549) back in 2009.  It has been available at [Google Code](https://code.google.com/p/windowsregistryfixer) since then, but I decided to make a mirror at GitHub, because I publish all of my codes here now.

To run WRF, just type `$ ./gwrf.py` --remember to give it execution permissions.


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
