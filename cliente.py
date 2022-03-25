# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:38:51 2022

@author: user_lc4_39
"""

#Importar o módulo socket

import socket, json

# Criar um socket UDP para IPv4
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

objetoPython = {'nome': 'Mauricio', 'nota': 7.2, 'ra': 123}

#Serializar o objeto no formato json
dadoJson = json.dumps(objetoPython)

print('Após serialização: ', dadoJson)

# Os dados devem ser codificados em vetores de bytes
dados = str.encode(dadoJson)

# Endereço e porta do servidor
endereco = ('localhost', 5000)

# Enviar uma mensagem
socketCliente.sendto(dados, endereco)
    
