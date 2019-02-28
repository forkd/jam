#!/bin/bash
#
#
# DIRECTORY STRUCTURE
# ./root-ca
#       /conf
#               will store configuration files for the CA.
#       /certs
#               certificate storage.  New certificates will be placed 
#               here as ther are issued.
#       /db
#               used for the certificate database (index) and the files 
#               that hold the next certificate and CRL serial numbers.
#               OpenSSL will create some additional files as needed.
#       /private
#               will store the private keys, one for the CA and the other 
#               for the OCSP responder.  It's important that no other user 
#               has access to it.  (in fact, if you're going to be serious 
#               about the CA, the machine on which the root material is 
#               stored  should have only a minimal number of user 
#               accounts.)
# TODO
#   - This file should be rewriten as a Makefile.  Then, user will build 
#     a CA by typing ``make''.
#


##
# GLOBAL VARIABLES
#
NAME="root-ca"  # change it ONLY if you know what you're doing! 
DOMAIN="pearljam.com"

# root-ca.cnf: root_ca_dn variables
ORGANIZATION_NAME="Grunge Inc."
ORGANIZATIONAL_UNIT_NAME="Pearl Jam"
COMMON_NAME="Eddie Vedder"
COUNTRY_NAME="US"
STATE_PROVINCE_NAME="WA"
LOCALITY_NAME="Seattle"
EMAIL_ADDRESS="eddie@$DOMAIN"



##
# FUNCTIONS
#
function build_structure() {
    echo -n "Building up CA structure... "

    mkdir -p "$NAME"/{certs,private,conf,new,crl}
    chmod 0700 "$NAME"/private
    touch "$NAME"/index
    openssl rand -hex 16 > "$NAME"/serial
    echo 1001 > "$NAME"/crlnumber

    cat root-ca.cnf |
    sed "s/__NAME__/$NAME/" |
    sed "s/__DOMAIN__/$DOMAIN/" |

    sed "s/__ORGANIZATION_NAME__/$ORGANIZATION_NAME/" |
    sed "s/__ORGANIZATIONAL_UNIT_NAME__/$ORGANIZATIONAL_UNIT_NAME/" |
    sed "s/__COMMON_NAME__/$COMMON_NAME/" |
    sed "s/__COUNTRY_NAME__/$COUNTRY_NAME/" |
    sed "s/__STATE_PROVINCE_NAME__/$STATE_PROVINCE_NAME/" |
    sed "s/__LOCALITY_NAME__/$LOCALITY_NAME/" |
    sed "s/__EMAIL_ADDRESS__/$EMAIL_ADDRESS/" > "$NAME"/conf/"$NAME".cnf

    echo "done."
}

function gen_root_ca() {
    echo "Will now generate root CA.  Follow the OpenSSL steps."
    openssl req -x509 \
            -config conf/root-ca.cnf \
            -newkey rsa \
            -out private/"$NAME".pem \
            -outform PEM

    # NO NEED?
    #openssl ca -selfsign \
            #-config conf/root-ca.cnf \
            #-in "$NAME".pem \
            #-out "$NAME".crt \
            #-extensions ca_ext
} 


##
# MAIN
#
build_structure
cd "$NAME"
gen_root_ca
        
