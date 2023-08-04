import psycopg2
import os


class BancoDeDados:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert_ordem_banco_de_dados(self, ordem):
        ordem_data = ordem
        ordem_data.pop('banco_de_dados', None)
        self.insert('ordem', ordem_data)

    def insert_cliente_banco_de_dados(self, cliente):
        print("Inserindo cliente no banco de dados... ")
        insert_query = """
                        INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, numero, complemento,
        	            bairro, cidade, estado, ddd)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['endereco']['CEP'],
            cliente['endereco']['Logradouro'],
            cliente['endereco']['Numero'],
            cliente['endereco']['Complemento'],
            cliente['endereco']['Bairro'],
            cliente['endereco']['Cidade'],
            cliente['endereco']['Estado'],
            cliente['endereco']['DDD']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select_cliente_banco_de_dados(self, conditions):
        print("Selecionando cliente no banco de dados: ")
        condition = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        select_query = f"SELECT * FROM cliente where {condition}"
        self.cursor.execute(select_query, list(conditions.values()))
        clientes = self.cursor.fetchall()
        if clientes:
            for cliente in clientes:
                print(cliente)
                print("Cliente encontrado!")
            return clientes
        else:
            print("Documento não encontrado na base de dados.")

    def update_cliente_banco_de_dados(self, cliente):
        if not cliente.cpf:
            raise ValueError("CPF é obrigatório para atualizar o cliente.")
        cliente_data = cliente.__dict__
        if cliente.endereco:
            endereco = cliente_data.pop('endereco')
            cliente_data.update(endereco.__dict__)
        self.update('cliente', {'cpf': cliente.cpf}, cliente_data)

    def delete_cliente_banco_de_dados(self, cpf):
        self.delete('cliente', {'cpf': cpf})

    def insert(self, tabela_nome, data):
        insert_query = f"INSERT INTO {tabela_nome} ({', '.join(data.keys())}) VALUES %s"
        insert_query = self.cursor.mogrify(insert_query, (tuple(data.values()),)).decode()
        self.cursor.execute(insert_query)
        self.connection.commit()

    def select(self, tabela_nome, conditions):
        condition_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        select_query = f"SELECT * FROM {tabela_nome} WHERE {condition_str}"
        self.cursor.execute(select_query, list(conditions.values()))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        else:
            return None

    def update(self, tabela_nome, conditions, data):
        set_str = ', '.join([f"{key} = %s" for key in data.keys()])
        condition_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        update_query = f"UPDATE {tabela_nome} SET {set_str} WHERE {condition_str}"
        self.cursor.execute(update_query, list(data.values()) + list(conditions.values()))
        self.connection.commit()

    def delete(self, tabela_nome, conditions):
        condition_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        delete_query = f"DELETE FROM {tabela_nome} WHERE {condition_str}"
        self.cursor.execute(delete_query, list(conditions.values()))
        self.connection.commit()

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }
        return parametros_conexao


conexao = BancoDeDados()