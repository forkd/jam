#!/usr/bin/env python

# ZIP CODE
# AUTHOR: Jose Mauro da Silva Sandy - http://informacaocomdiversao.blogspot.com
#
# CONTACT: jmsandy _at_ gmail _dot_ com
#
# DATE: 2008-12-08
#
# More information about ZIP CODE, visit:
# http://www.correios.com.br/servicos/cep/cep_estrutura.cfm
################################################################################

import easygui

def verify_zip(zip_code):
  """ Receiving one zip-code for validate.
      Return one list with adress of zip-code or -1, otherwise.

  """

  # Opening the file responsible to save information the CEP
  file_cep = open(r'/Users/zezim/cep.txt', 'r')

  # Receive and format the zip-code for validation
  find_cep = '"' + str(zip_code) + ' "'
  lines = file_cep.readlines()

  # Receiving the line to line the file
  for line in lines:
    line_dic = line.split(',')

    # Comparing the zip-code
    if(line_dic[2] == find_cep):
      file_cep.close()

      return line_dic

  else:
    file_cep.close()

    return "-1"

# Verifying if the module is been executed like principal code or module
if("__main__" == __name__):
  zip_chosen = easygui.integerbox(msg="Enter the Zip-Code(Only Digits)", \
  title="ZIP-CODE",default="", argLowerBound=0, argUpperBound=99999999)

  # Verify if the desire's user is validate zip-code
  if(zip_chosen):
    adress = verify_zip(zip_chosen)

    if(adress!="-1"):
      answer = 'RUA:    ', adress[5].replace('"',''), '\n', 'BAIRRO: ', \
      adress[1].replace('"',''), '\n', 'CIDADE: ', adress[3].replace('"',''),\
      '-', adress[9].replace('"','')

      easygui.codebox(msg="Information", title="Adress", text=answer)

    else:
      easygui.msgbox("Zip code invalid.")   

