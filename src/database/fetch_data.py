import pandas as pd
from sqlalchemy import create_engine
from src.database.connect_db import connect_to_db

def fetch_data(query):
    conn = connect_to_db()
    if conn:
        try:
            df = pd.read_sql(query, conn)
            print("Dados carregados com sucesso.")
            print(df.head())
            return df
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        finally:
            conn.close()
            print("Conexão encerrada.")
    return None