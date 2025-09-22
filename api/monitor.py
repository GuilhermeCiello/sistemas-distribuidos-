import mysql.connector
import time
import asyncio
from palavras import palavra_aleatoria


db_config = {
    'host': 'mysql-container',
    'user': 'root',
    'password': 'senha123',
    'database': 'meuapp'
}

ultimo_status = 0

async def verificar_status():
    global ultimo_status
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
      
        cursor.execute('SELECT id FROM status')
        rows = cursor.fetchall()
        status_atual = rows[0][0] if rows else 0
        
        print(f'Status atual: {status_atual}, Último conhecido: {ultimo_status}')
      
        if status_atual > ultimo_status:
            print('Mudança detectada! Criando eventos...')
            
       
            for i in range(ultimo_status + 1, status_atual + 1):
               
                await asyncio.sleep(0.15)
                
               
                palavra = palavra_aleatoria()
                
              
                cursor.execute('INSERT INTO eventos (id, valor) VALUES (%s, %s)', (i, palavra))
                conn.commit()
                
                print(f'Evento criado: ID={i}, Palavra="{palavra}"')
            
            ultimo_status = status_atual
        
        cursor.close()
        conn.close()
        
    except Exception as error:
        print(f'Erro no monitor: {error}')

async def iniciar():
    global ultimo_status
    print('Monitor iniciado. Verificando mudanças a cada 2 segundos...')
  
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM status')
        rows = cursor.fetchall()
        ultimo_status = rows[0][0] if rows else 0
        cursor.close()
        conn.close()
        print(f'Status inicial: {ultimo_status}')
    except Exception as error:
        print(f'Erro ao buscar status inicial: {error}')
   
    while True:
        await verificar_status()
        await asyncio.sleep(2)


if __name__ == '__main__':
    asyncio.run(iniciar())