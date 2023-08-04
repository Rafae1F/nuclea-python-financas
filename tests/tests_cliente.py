import unittest
from faker import Factory
from unittest.mock import patch
from main import main, clientes
from validate_docbr import CPF


class TestCliente(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Factory.create('pt_BR')
        return fake.name()

    def gera_cpf(self):
        cpf = CPF()
        cpf_gerado = cpf.generate()
        return cpf_gerado

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = self.gera_cpf()
        inputs = ["1", "1", nome, cpf, "12.345.678-x", "12/02/2001", "05003-060", "42", "apto 100", "sim", "sim", "5",
                  "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "12.345.678-x",
            "data_nascimento": "12/02/2001",
            'endereco': {
                'CEP': '05003-060',
                'Logradouro': 'Rua Higino Pellegrini',
                'Numero': '42',
                'Complemento': 'apto 100',
                'Bairro': 'Água Branca',
                'Cidade': 'São Paulo',
                'Estado': 'SP',
                'DDD': '11'
            }
        }

        self.assertIn(cliente_esperado, clientes)


if __name__ == '__main__':
    main()
