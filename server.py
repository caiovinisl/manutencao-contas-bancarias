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

    try:
        # Simulando autenticação do cliente com RG (número de identidade)
        rg = client_socket.recv(1024).decode()

        # Inicializando a conta de novos cliente com saldo zero
        if rg not in clientes:
            clientes[rg] = {"rg": rg, "saldo": 0}

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            # Incrementa relogio logico
            relogio_logico += 1

            # Processamento das operações bancárias
            if data == "1":
                # Responde 
                resposta = (
                    f"Saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                )
            elif data == "2":
                amount = int(client_socket.recv(1024).decode())
                if amount <= clientes[rg]["saldo"]:
                    clientes[rg]["saldo"] -= amount
                    resposta = f"Retirada de {amount} realizada com sucesso. Novo saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                else:
                    resposta = f"Saldo insuficiente para realizar a retirada. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"

            elif data == "3":
                amount = int(client_socket.recv(1024).decode())
                clientes[rg]["saldo"] += amount
                resposta = f"Deposito de {amount} realizada com sucesso. Novo saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                
            elif data == "4":
                amount = int(client_socket.recv(1024).decode())
                print(amount)
                dest_rg = client_socket.recv(1024).decode()
                print(dest_rg)
                if dest_rg in clientes and amount <= clientes[rg]["saldo"]:
                    clientes[rg]["saldo"] -= amount
                    clientes[dest_rg]["saldo"] += amount
                    resposta = f"Transferência de {amount} realizada para RG {dest_rg} com sucesso. Novo saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                elif dest_rg not in clientes:
                    resposta = f"Conta com RG {dest_rg} não existe. Transferência não realizada. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                else:
                    resposta = f"Saldo insuficiente para realizar a transferência. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
            else:
                resposta = "Operação inválida. Relógio lógico: {relogio_logico}"

            client_socket.send(resposta.encode())

    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        print(f"Conexão encerrada com {address}")
        client_socket.close()


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print("Servidor bancário iniciado. Aguardando conexões...")

    while True:
        client_socket, address = servidor.accept()
        print(f"Nova conexão de {address}")

        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, address)
        )
        client_thread.start()


if __name__ == "__main__":
    main()
