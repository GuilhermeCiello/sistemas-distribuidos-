const mysql = require('mysql2/promise');
const { palavraAleatoria } = require('./palavras');


const dbConfig = {
  host: 'mysql-container',
  user: 'root',
  password: 'senha123',
  database: 'meuapp'
};

let ultimoStatus = 0;

async function verificarStatus() {
  try {
    const connection = await mysql.createConnection(dbConfig);
    

    const [rows] = await connection.execute('SELECT id FROM status');
    const statusAtual = rows[0].id;
    
    console.log(`Status atual: ${statusAtual}, Último conhecido: ${ultimoStatus}`);
    
  
    if (statusAtual > ultimoStatus) {
      console.log('Mudança detectada! Criando eventos...');
      
  
      for (let i = ultimoStatus + 1; i <= statusAtual; i++) {
        
        await new Promise(resolve => setTimeout(resolve, 150));
        
     
        const palavra = palavraAleatoria();
        
    
        await connection.execute('INSERT INTO eventos (id, valor) VALUES (?, ?)', [i, palavra]);
        
        console.log(`Evento criado: ID=${i}, Palavra="${palavra}"`);
      }
      
      ultimoStatus = statusAtual;
    }
    
    await connection.end();
    
  } catch (error) {
    console.error('Erro no monitor:', error.message);
  }
}

async function iniciar() {
  console.log('Monitor iniciado. Verificando mudanças a cada 2 segundos...');

  try {
    const connection = await mysql.createConnection(dbConfig);
    const [rows] = await connection.execute('SELECT id FROM status');
    ultimoStatus = rows[0].id;
    await connection.end();
    console.log(`Status inicial: ${ultimoStatus}`);
  } catch (error) {
    console.error('Erro ao buscar status inicial:', error.message);
  }
  
  setInterval(verificarStatus, 2000);
}

iniciar();