import psycopg2
from data.db_connection import get_db_connection

def verificar_login(email, password):
    try:
        conn = get_db_connection()
        if conn is None:
            return False, None
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT nome FROM cliente_schema.cliente
            WHERE email = %s AND senha = %s
        ''', (email, password))
        
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if usuario:
            nome = usuario[0]
            print(f"Bem-vindo, {nome}!")
            return True, nome
        else:
            print("Email ou senha inválidos!")
            return False, None
    except Exception as e:
        print(f"Erro ao verificar login: {e}")
        return False, None