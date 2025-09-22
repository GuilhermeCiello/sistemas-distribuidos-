Para executar o trabalho é necessário ter o Docker instalado, baixar a pasta API e navegar até ela:
cd /caminho/para/api

após isso executar o docker compose para gerenciar os containers
docker-compose up -d

depois que eles estiverem em funcionamento executar o comando para ver se estão rodando corretamente
 docker ps

após isso no terminal do powershell executar os comandos para testar get e post

Invoke-RestMethod -Uri "http://localhost:3000/incrementar" -Method Post
Invoke-RestMethod -Uri "http://localhost:3000/1" -Method Get

Invoke-RestMethod -Uri "http://localhost:3001/incrementar" -Method Post
Invoke-RestMethod -Uri "http://localhost:3001/1" -Method Get

para verificar a geração de palavras aleatórias no banco de dados pode-se abrir outro terminal e verificar os logs 
docker-compose logs -f monitor

ou verificar diretamente no banco de dados
docker-compose exec mysql-container mysql -u root -p senha123 -e "USE meuapp; SELECT * FROM eventos;"
