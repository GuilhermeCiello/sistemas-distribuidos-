# Guia de Execução do Trabalho

## Pré-requisitos
- Ter o **Docker** instalado.
- Baixar ou clonar o repositório

## Passo a passo

### 1. Navegar até a pasta da API
```bash
cd /caminho/para/api
```
### 2. Subir os containers com Docker Compose]

docker-compose up -d

### 3. Verificar se os containers estão rodando
```bash
docker ps
```
### 4. Testar os endpoints no PowerShell
```bash
Invoke-RestMethod -Uri "http://localhost:3000/incrementar" -Method Post
Invoke-RestMethod -Uri "http://localhost:3000/1" -Method Get

Invoke-RestMethod -Uri "http://localhost:3001/incrementar" -Method Post
Invoke-RestMethod -Uri "http://localhost:3001/1" -Method Get
```
### 5. Verificar geração de palavras aleatórias

Opção 1: Via logs do monitor
```bash
docker-compose logs -f monitor
```
Opção 2: Diretamente no banco de dados
```bash
docker-compose exec mysql-container mysql -u root -p senha123 -e "USE meuapp; SELECT * FROM eventos;"
```
