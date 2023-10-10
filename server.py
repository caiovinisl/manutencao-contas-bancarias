import socket
import threading

HOST = "localhost"
PORT = 8081

# Dicionário para armazenar informações do cliente (RG como chave e dados da conta como valor)
clientes = {}

# Relógio lógico do servidor
relogio_logico = 0


def handle_client(client_socket, address):
    global relogio_logico

    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            relogio_logico += 1

            # Processamento das operações bancárias
            if data == "1":
                resposta = f"Saldo: {clientes[client_socket]['saldo']}. Relógio lógico: {relogio_logico}"
            elif data == "2":
                # Simulação de uma retirada fixa de 100 para fins de exemplo
                clientes[client_socket]["saldo"] -= 100
                resposta = f"Retirada realizada com sucesso. Novo saldo: {clientes[client_socket]['saldo']}. Relógio lógico: {relogio_logico}"
            elif data == "3":
                # Simulação de uma transferência fixa de 50 para fins de exemplo
                clientes[client_socket]["saldo"] += 50
                resposta = f"Transferência realizada com sucesso. Novo saldo: {clientes[client_socket]['saldo']}. Relógio lógico: {relogio_logico}"
            else:
                resposta = "Operação inválida. Relógio lógico: {relogio_logico}"

            client_socket.send(resposta.encode())

        except Exception as e:
            print(f"Erro: {str(e)}")
            break

    print(f"Conexão encerrada com {address}")
    del clientes[client_socket]
    client_socket.close()


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print("Servidor bancário iniciado. Aguardando conexões...")

    while True:
        client_socket, address = servidor.accept()
        print(f"Nova conexão de {address}")

        # Simulando autenticação do cliente com RG (número de identidade)
        rg = client_socket.recv(1024).decode()

        # Inicializando a conta do cliente com saldo zero
        clientes[client_socket] = {"rg": rg, "saldo": 0}

        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, address)
        )
        client_thread.start()


if __name__ == "__main__":
    main()
