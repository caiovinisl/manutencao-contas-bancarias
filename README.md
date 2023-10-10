# manutencao-contas-bancarias
Prática de Implementação: Sistema Distribuído Simples para Manutenção de Contas Bancárias Fundamentos de Sistemas Distribuídos.

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/caiovinisl/manutencao-contas-bancarias?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/caiovinisl/manutencao-contas-bancarias">
  
  <a href="https://github.com/caiovinisl/metodos-hashing/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/caiovinisl/manutencao-contas-bancarias">
  </a>
   
   <a href="https://github.com/caiovinisl/metodos-hashing/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/caiovinisl/manutencao-contas-bancarias?style=social">
  </a>
  
 
</p>

<h4 align="center"> 
	🚧 Manutenção de Contas Bancárias 🚧
</h4>

<p align="center">
	<img alt="Status Concluído" src="https://img.shields.io/badge/STATUS-CONCLU%C3%8DDO-brightgreen">
</p>

<p align="center">
 <a href="#-sobre-o-projeto">Sobre</a> •
 <a href="#-funcionalidades">Funcionalidades</a> •
 <a href="#-como-executar-o-projeto">Como executar</a> • 
 <a href="#-tecnologias">Tecnologias</a>
</p>

## 💻 Sobre o projeto

📄 Sistema Distribuído Simples para Manutenção de Contas Bancárias.

### Detalhamento
Implementar um sistema rudimentar bancário de transações financeiras, para saque, depósito e transferência de fundos entre contas bancárias. Os processos clientes e o servidor devem manter seus relógios lógicos atualizados (iniciados com valor 0) e exibir em tela cada mudança de valor dos respectivos relógios.

1 - As operações de transações financeiras devem estar implementadas no lado do servidor, mantendo contas de clientes.

2 – Os clientes devem se conectar ao servidor e solicitar as requisições desejadas, ou seja, que tipo de operações financeiras (saldo, retirada e transferência, entre contas). Cada ciente do banco terá uma conta-corrente vinculada a um número de RG e respectivo nome do cliente.

![image](https://github.com/caiovinisl/manutencao-contas-bancarias/assets/31699879/ce4fd071-95f7-4264-b6c6-70e7c3e37c12)

### Restrições
1 - O programa pode ser implementado em linguagens para programação desktop em rede, como Python, Java, C, C++ ou C#. Obs.: De preferência em Python.

2 - A comunicação entre os processos deve ser implementada usado sockets.

3 - Todo o programa deve estar devidamente comentado, de modo a facilitar o entendimento do código.

4 Entregar documentação do projeto, contendo: descrição da solução, exemplo de utilização e cópia impressa do código.

---

## ⚙️ Funcionalidades

- [ ] Servidor
  - [ ] 
- [ ] Proxy
  - [ ] 
- [ ] Cliente
  - [ ] 

---

## 🛣️ Como executar o projeto

#### 🎲 Rodando a aplicação

```bash

# Clone este repositório
$ git clone https://github.com/caiovinisl/manutencao-contas-bancarias.git

# Acesse a pasta do projeto no terminal/cmd
$ cd manutencao-contas-bancarias

# Certifique-se de executar primeiro o proxy
$ python proxy.py

# Depois execute o servidor
$ python server.py

# Em seguida, execute o cliente
$ python client.py

```

## 🛠 Tecnologias

- **[Python](https://www.python.org/)**

---
