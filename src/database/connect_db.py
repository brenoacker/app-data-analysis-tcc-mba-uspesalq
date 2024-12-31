import psycopg2

DB_CONFIG = {
    'dbname': 'db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5434'  # Ajuste a porta se necessário
}

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
        print("Conexão bem-sucedida ao banco de dados.")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None