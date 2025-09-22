## 📋 Containers em Execução

Você deverá ver containers como:
- `mysql-container`
- `flask-app`
- `node-app`
- `monitor-python`
- `monitor-js`

---

## 🧪 Testando a API Flask

No **PowerShell**, execute os comandos abaixo:

👉 **Incrementar contador**
```powershell
Invoke-RestMethod -Uri "http://localhost:3000/incrementar" -Method Post
