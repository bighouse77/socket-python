# Importando o módulo que possibilita abrir conexões
import socket, json

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
    
    # Deserialização do formato JSON para objeto Python
    obj = json.loads(mensagem[0])
    
    print(obj)
    
    print(obj['ra'], "do aluno", obj['nome'])
    
    obj['nota'] = obj['nota'] + 1
    
    print("Nota após assistir o congresso:", obj['nota'])
    
