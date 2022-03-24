# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:38:51 2022

@author: user_lc4_39
"""

#Importar o módulo socket

import socket

# Criar um socket UDP para IPv4
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Os dados devem ser codificados em vetores de bytes
dados = str.encode("Oi do cliente")
# Endereço e porta do servidor
endereco = ('localhost', 5000)

# Enviar uma mensagem
socketCliente.sendto(dados, endereco)
