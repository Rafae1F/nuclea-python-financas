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
        print("Inserindo ordem no banco de dados...")
        self.insert('ordem', ordem)
        print(ordem)

    def select_ordem_banco_de_dados(self, cliente_id):
        print("Buscando carteira no banco de dados: ")
        carteira_selecionada = self.select_all('ordem', {'cliente_id': cliente_id})
        return carteira_selecionada

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

    def update_cliente_banco_de_dados(self, cpf, novos_dados):
        print("Atualizando dados no banco de dados...")
        update_query = """
                    UPDATE cliente
                    SET nome = %s, cpf = %s, rg = %s, data_nascimento = %s,
                        cep = %s, logradouro = %s, numero = %s, complemento = %s,
                        bairro = %s, cidade = %s, estado = %s, ddd = %s
                    WHERE cpf = %s;
                """
        values = (
            novos_dados['nome'],
            novos_dados['cpf'],
            novos_dados['rg'],
            novos_dados['data_nascimento'],
            novos_dados['endereco']['CEP'],
            novos_dados['endereco']['Logradouro'],
            novos_dados['endereco']['Numero'],
            novos_dados['endereco']['Complemento'],
            novos_dados['endereco']['Bairro'],
            novos_dados['endereco']['Cidade'],
            novos_dados['endereco']['Estado'],
            novos_dados['endereco']['DDD'],
            cpf,
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def select_cliente_banco_de_dados(self, cpf):
        print("Buscando cliente no banco de dados: ")
        cliente_selecionado = self.select('cliente', {'cpf': cpf})
        return cliente_selecionado

    def delete_cliente_banco_de_dados(self, cpf):
        print("Removendo cliente da base de dados.")
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
            select_coluna_linha = (dict(zip(columns, row)))
            select_linha = row
            print(select_linha)
            return select_coluna_linha

    def select_all(self, tabela_nome, conditions):
        condition_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        select_query = f"SELECT * FROM {tabela_nome} WHERE {condition_str}"
        self.cursor.execute(select_query, list(conditions.values()))
        rows = self.cursor.fetchall()
        if rows:
            columns = [desc[0] for desc in self.cursor.description]
            results = []
            for row in rows:
                result_dict = dict(zip(columns, row))
                results.append(result_dict)
            return results
        else:
            return []

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
