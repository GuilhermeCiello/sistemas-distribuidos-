# 🖥️ Sistemas Distribuídos

## 📂 Estrutura do Projeto
O projeto contém os seguintes serviços:

- **MySQL** (Banco de dados)  
- **Flask App** (API em Python)  
- **Node App** (API em Node.js)  
- **Monitor Python** (processo que roda monitoramento em Python)  
- **Monitor JS** (processo que roda monitoramento em Node.js)  

---

## ⚙️ Como Rodar o Projeto

### 1. Clone ou copie o repositório
```bash
git clone https://github.com/seu-repositorio/api.git
cd api

2. Suba os containers
docker-compose up -d

3. Verifique se os containers estão rodando
docker ps


Você deverá ver containers como:

mysql-container

flask-app

node-app

monitor-python

monitor-js

🧪 Testando a API Flask

No PowerShell, execute os comandos abaixo:

👉 Incrementar contador

Invoke-RestMethod -Uri "http://localhost:3000/incrementar" -Method Post


👉 Consultar contador

Invoke-RestMethod -Uri "http://localhost:3000/1" -Method Get
