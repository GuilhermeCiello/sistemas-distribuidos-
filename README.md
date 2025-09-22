# Visão Geral do Sistema
Este projeto implementa um sistema distribuído com duas APIs independentes (Python Flask e Node.js) que compartilham um mesmo banco de dados MySQL, acompanhado por um sistema de monitoramento que detecta mudanças automaticamente.

## Fluxo de Funcionamento:
1. Usuário faz requisição para qualquer API (Python ou Node.js)
2. API processa e atualiza o banco de dados MySQL
3. Monitor detecta mudanças no banco automaticamente
4. Monitor cria registros com palavras aleatórias
5. Usuário pode consultar os dados criados

## Tecnologias Utilizadas
1. Docker e Docker Compose
Função: Containerização e orquestração

Como é usado:

* Isola cada serviço em containers separados

* Gerencia redes e volumes entre containers

* Facilita deploy e reprodução do ambiente

2. MySQL
Função: Banco de dados relacional

Como é usado:

* Armazena dados das APIs (tabelas status e eventos)

* Permite comunicação entre os diferentes serviços

3. Python Flask
Função: API REST em Python

Bibliotecas:

* Flask: Framework web

* mysql-connector-python: Conexão com MySQL

* Porta: 3000

4. Node.js + Express
Função: API REST em JavaScript

Bibliotecas:

* Express: Framework web

* mysql2: Driver MySQL com suporte a Promises

* Porta: 3001

5. Monitoramento (Python/JavaScript)
Função: Observar mudanças no banco e criar eventos

Funcionamento:

* Verifica a tabela status a cada 2 segundos

* Detecta novas submissões e cria registros na tabela eventos

* Gera palavras aleatórias automaticamente

## Como usar

1. Primeiramente é necessário possuir o docker instalado, após isso clonar o repositório:
2. Executar o sistema
```
# Subir todos os containers
docker-compose up -d


# Verificar status dos containers
docker-compose ps

```
3. Testar o sistema

Python - Porta 3000
```
# Incrementar contador
Invoke-RestMethod -Uri "http://localhost:3000/incrementar" -Method Post

# Buscar evento específico
Invoke-RestMethod -Uri "http://localhost:3000/1" -Method Get

```
Node.js - Porta 3001
```
# Incrementar contador
Invoke-RestMethod -Uri "http://localhost:3001/incrementar" -Method Post

# Buscar evento específico
Invoke-RestMethod -Uri "http://localhost:3001/1" -Method Get
```

4. Monitorar o Sistema

Ver logs dos monitores
```
# Monitor Python
docker-compose logs -f monitor-python

# Monitor JavaScript
docker-compose logs -f monitor-js
``` 
Ver dados diretamente no banco

```
# Acessar o banco de dados
docker-compose exec mysql-container mysql -u root -p

# No MySQL, executar:
USE meuapp;
SELECT * FROM status;
SELECT * FROM eventos;
```
5. Parar o Sistema
```
# Parar todos os containers
docker-compose down

# Parar e remover volumes
docker-compose down -v
```
