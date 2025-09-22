const express = require('express');
const mysql = require('mysql2/promise');

const app = express();
const port = 3000;

// Configuração do banco
const dbConfig = {
  host: 'mysql-container',
  user: 'root',
  password: 'senha123',
  database: 'meuapp'
};


app.use(express.json());


app.get('/', async (req, res) => {
  try {
    const connection = await mysql.createConnection(dbConfig);
    const [rows] = await connection.execute('SELECT id FROM status');
    await connection.end();
    
    const quantidade = rows[0].id;
    res.json({ registros: quantidade });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});


app.get('/:id', async (req, res) => {
  try {
    const connection = await mysql.createConnection(dbConfig);
    const [rows] = await connection.execute('SELECT valor FROM eventos WHERE id = ?', [req.params.id]);
    await connection.end();
    
    if (rows.length === 0) {
      res.status(404).json({ error: 'Registro não encontrado' });
    } else {
      res.json({ id: req.params.id, valor: rows[0].valor });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/incrementar', async (req, res) => {
  try {
    const connection = await mysql.createConnection(dbConfig);
    await connection.execute('UPDATE status SET id = id + 1');
    const [rows] = await connection.execute('SELECT id FROM status');
    await connection.end();
    
    res.json({ novo_id: rows[0].id });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Rota POST /incrementar-async - incrementa o status (sem retorno imediato)
app.post('/incrementar-async', async (req, res) => {
  try {
    const connection = await mysql.createConnection(dbConfig);
    await connection.execute('UPDATE status SET id = id + 1');
    await connection.end();
    

    res.json({ message: 'Incremento realizado' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, '0.0.0.0', () => {
  console.log('App rodando na porta ' + port);
});
