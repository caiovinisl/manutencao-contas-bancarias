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

        # Aguarda a resposta do servidor
        response = client_socket.recv(1024).decode()
        print(f"Resposta do servidor: {response}")


if __name__ == "__main__":
    main()
