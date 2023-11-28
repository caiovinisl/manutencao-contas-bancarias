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
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            relogio_logico += 1

            # Cadastro
            if data == "2":
                # Realizando cadastro do cliente com RG (número de identidade)
                rg = client_socket.recv(1024).decode()
                senha = client_socket.recv(1024).decode()

                # Verifica se nao existe cadastro com RG
                if(rg not in clientes):
                    # Inicializando a conta do cliente com saldo zero
                    clientes[rg] = {"rg": rg, "senha": senha, "saldo": 0}

                    resposta = f"Conta criada com sucesso!. Relógio lógico: {relogio_logico}"
                else:
                    resposta = f"ERRO: Já existe uma conta com esse RG!. Relógio lógico: {relogio_logico}"

                client_socket.send(resposta.encode())

            if data == "1":
                # Realizando autenticação do cliente com RG (número de identidade)
                rg = client_socket.recv(1024).decode()
                senha = client_socket.recv(1024).decode()

                # Verifica se o RG está cadastrado
                if(rg in clientes):
                    # Verificando se senha está correta
                    if(senha == clientes[rg]['senha']):
                        resposta = "OK"
                        client_socket.send(resposta.encode())
                        resposta = f"Login realizado com sucesso. Relógio lógico: {relogio_logico}"
                        client_socket.send(resposta.encode())
                        while True:
                            data = client_socket.recv(1024).decode()
                            if not data:
                                break

                            relogio_logico += 1

                            # Processamento das operações bancárias
                            if data == "1":
                                resposta = (
                                    f"Saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                                )
                            elif data == "2":
                                amount = int(client_socket.recv(1024).decode())
                                if amount > 0:
                                    clientes[rg]["saldo"] += amount
                                    resposta = f"Depósito de {amount} realizado com sucesso. Novo saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                                else:
                                    resposta = f"Valor de depósito inválido. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                            elif data == "3":
                                amount = int(client_socket.recv(1024).decode())
                                if amount <= clientes[rg]["saldo"]:
                                    clientes[rg]["saldo"] -= amount
                                    resposta = f"Retirada de {amount} realizada com sucesso. Novo saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                                else:
                                    resposta = f"Saldo insuficiente para realizar a retirada. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                            elif data == "4":
                                amount = int(client_socket.recv(1024).decode())
                                dest_rg = client_socket.recv(1024).decode()
                                if dest_rg in clientes and amount <= clientes[rg]["saldo"]:
                                    clientes[rg]["saldo"] -= amount
                                    clientes[dest_rg]["saldo"] += amount
                                    resposta = f"Transferência de {amount} realizada para RG {dest_rg} com sucesso. Novo saldo: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                                elif dest_rg not in clientes:
                                    resposta = f"Conta com RG {dest_rg} não existe. Transferência não realizada. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                                else:
                                    resposta = f"Saldo insuficiente para realizar a transferência. Saldo atual: {clientes[rg]['saldo']}. Relógio lógico: {relogio_logico}"
                            elif data == "5":
                                resposta = f"Fazendo logoff. Relógio lógico: {relogio_logico}"
                                client_socket.send(resposta.encode())
                                break
                            else:
                                resposta = f"Operação inválida. Relógio lógico: {relogio_logico}"

                            client_socket.send(resposta.encode())
                    else:
                        resposta = "ERRO"
                        client_socket.send(resposta.encode())
                        resposta = f"Senha incorreta! Relógio lógico: {relogio_logico}"
                        client_socket.send(resposta.encode())
                else:
                    resposta = "ERRO"
                    client_socket.send(resposta.encode())
                    resposta = f"Conta não existe. Relógio lógico: {relogio_logico}"
                    client_socket.send(resposta.encode())

    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        #if rg in clientes:
            #del clientes[rg]
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
