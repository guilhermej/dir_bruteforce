#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests

arquivo = open('/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt')

linhas = arquivo.readlines()

url = 'http://g1.com.br/'

for linha in linhas:
    codigo = 404
    if linha[0] != "#":
        resposta = requests.get(url+linha)
        codigo = resposta.status_code
    if codigo != 404 and codigo != 403:
        print url+linha, codigo
