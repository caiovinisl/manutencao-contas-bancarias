import socket

HOST = "localhost"
PORT = 8081


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Solicita o número de RG ao usuário para autenticação
    rg = input("Digite seu número de RG: ")
    client_socket.send(rg.encode())

    while True:
        # Menu de operações bancárias para o cliente
        print("Menu:")
        print("1. Consultar saldo")
        print("2. Realizar retirada")
        print("3. Realizar transferência")
        print("4. Sair")
        choice = input("Escolha a operação: ")

        if choice == "4":
            client_socket.close()
            break

        # Envia a escolha do cliente para o servidor
        client_socket.send(choice.encode())

        if choice == "2":
            # Solicita o valor a ser retirado
            amount = input("Digite o valor: ")
            client_socket.send(amount.encode())

        elif choice == "3":
            # Solicita o valor e o número de RG da conta de destino
            amount = input("Digite o valor: ")
            dest_rg = input("Digite o número de RG da conta de destino: ")
            client_socket.send(amount.encode())
            client_socket.send(dest_rg.encode())

        # Aguarda a resposta do servidor
        response = client_socket.recv(1024).decode()
        print(f"Resposta do servidor: {response}")


if __name__ == "__main__":
    main()
