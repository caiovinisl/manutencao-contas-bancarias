import socket

HOST = "localhost"
PORT = 8081


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Solicita o número de RG ao usuário para autenticação
    while True:
        # Menu de Login
        print("Login")
        print("1. Realizar Login")
        print("2. Cadastrar conta")
        print("3. Encerrar Conexão")
        loginChoice = input("Escolha a operação: ")

        if loginChoice == "3":
            client_socket.close()
            break

        # Envia a escolha de login ou cadastro
        client_socket.send(loginChoice.encode())

        if loginChoice == "2":

            rg = input("Digite o seu RG: ")
            senha = input("Digite sua senha:")
            client_socket.send(senha.encode())
            client_socket.send(rg.encode())

        if loginChoice == "1":
            # Envia User e senha para logar
            rg = input("Digite o RG da conta: ")
            senha = input("Digite sua senha:")
            client_socket.send(senha.encode())
            client_socket.send(rg.encode())

            loginStatus = client_socket.recv(1024).decode()
            if(loginStatus == "OK"):
                response = client_socket.recv(1024).decode()
                print(f"Resposta do servidor: {response}")
                # Cliente Logado
                while True:
                    # Menu de operações bancárias para o cliente
                    print("Menu:")
                    print("1. Consultar saldo")
                    print("2. Realizar depósito")
                    print("3. Realizar retirada")
                    print("4. Realizar transferência")
                    print("5. Sair")
                    choice = input("Escolha a operação: ")

                    if choice == "5":
                        client_socket.send(choice.encode())
                        break

                    # Envia a escolha do cliente para o servidor
                    client_socket.send(choice.encode())

                    if choice == "2":
                        # Solicita o valor a ser depositado
                        amount = input("Digite o valor: ")
                        client_socket.send(amount.encode())

                    if choice == "3":
                        # Solicita o valor a ser retirado
                        amount = input("Digite o valor: ")
                        client_socket.send(amount.encode())

                    elif choice == "4":
                        # Solicita o valor e o número de RG da conta de destino
                        amount = input("Digite o valor: ")
                        dest_rg = input("Digite o número de RG da conta de destino: ")
                        client_socket.send(amount.encode())
                        client_socket.send(dest_rg.encode())

                    # Aguarda a resposta do servidor após login
                    response = client_socket.recv(1024).decode()
                    print(f"Resposta do servidor: {response}")

        # Aguarda a resposta do servidor antes do login
        response = client_socket.recv(1024).decode()
        print(f"Resposta do servidor: {response}")


if __name__ == "__main__":
    main()
