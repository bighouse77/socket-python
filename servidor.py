# Importando o módulo que possibilita abrir conexões
import socket

# Objeto que será o socket UDP para IPv4 do servidor
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular um IP e uma porta do socket
socketServidor.bind(('localhost', 5000))

print("Servidor inicial na porta 5000, escutando mensagens")

while True:
    # Receber possíveis pacotes de até 1024
    mensagem = socketServidor.recvfrom(1024)
    
    # O objeto é uma tupla (conteúdo, (IP, porta))
    print("Recebido", mensagem[0], "de", mensagem[1])
    
    if mensagem[0] == b"sair":
        break
    
socketServidor.close()
