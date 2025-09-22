from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
port = 3000


db_config = {
    'host': 'mysql-container',  
    'user': 'root',
    'password': 'senha123',
    'database': 'meuapp',
}

# Função para abrir conexão
def get_connection():
    return mysql.connector.connect(**db_config)


@app.route('/', methods=['GET'])
def get_registros():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id FROM status")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        if rows:
            quantidade = rows[0]['id']
        else:
            quantidade = 0

        return jsonify({'registros': quantidade})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<int:id>', methods=['GET'])
def get_evento(id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT valor FROM eventos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return jsonify({'id': id, 'valor': row['valor']})
        else:
            return jsonify({'error': 'Registro não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/incrementar', methods=['POST'])
def incrementar():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE status SET id = id + 1")
        conn.commit()
        cursor.execute("SELECT id FROM status")
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row: 
            return jsonify({'novo_id': row[0]})
        else:
            return jsonify({'error': 'Nenhum registro encontrado'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/incrementar-async', methods=['POST'])
def incrementar_async():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE status SET id = id + 1")
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Incremento realizado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
