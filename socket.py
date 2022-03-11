import socket

socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

endereco = ("localhost",5000)

socketServer.bind(endereco)

while True:
    mensagem = socketServer.recvfrom(1024)
    
    print("Recebido:", str(mensagem[0]), "de", mensagem[1])