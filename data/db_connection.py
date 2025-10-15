import psycopg2

def init_db():
    """Inicializa o banco de dados PostgreSQL e cria as tabelas playlist e usuarios se não existirem."""
    try:
        conn = psycopg2.connect(
            dbname="Loopify",
            user="postgres",  
            password="gui123reis13",  
            host="localhost",
            port="5433"
        )
        cursor = conn.cursor()
        
        # Criação da tabela playlist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS playlist (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                artista TEXT NOT NULL,
                data_inclusao TEXT NOT NULL,
                status TEXT NOT NULL,
                prazo_final TEXT,
                urgencia BOOLEAN NOT NULL
            )
        ''')
        
        # Criação da tabela usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="Loopify",
            user="postgres", 
            password="gui123reis13",
            host="localhost",
            port="5433"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None