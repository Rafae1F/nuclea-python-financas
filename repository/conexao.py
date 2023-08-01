import psycopg2
import os


def retorna_parametros_conexao_banco_de_dados():
    parametros_conexao = {
        "user": os.getenv('user'),
        "password": os.getenv('password'),
        "host": os.getenv('host'),
        "port": os.getenv('port'),
        "database": os.getenv('database')
    }

    return parametros_conexao


def conexao_postgres():
    connection = psycopg2.connect(**retorna_parametros_conexao_banco_de_dados())
    cursor = connection.cursor()
    return cursor, connection


def seleciona_cliente_banco_de_dados():
    print("Buscando clientes no banco de dados: ")
    select_query = "SELECT * FROM CLIENTE"
    cursor, connection = conexao_postgres()
    cursor.execute(select_query)
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)


print("Execucao banco de dados")
seleciona_cliente_banco_de_dados()
