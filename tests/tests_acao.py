import unittest
from unittest.mock import patch
from main import main, acoes


class TestStringMethods(unittest.TestCase):

    def test_acao(self):
        inputs = ["2", "Itaú Unibanco", "ITUB4", 23.84, 500, "01/08/2023", "sim", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        acao_esperada = {
            "nome": "Itaú Unibanco",
            "ticket": "ITUB4",
            "valor_compra": 23.84,
            "quantidade_compra": 500,
            "data_compra": "01/08/2023"
        }

        self.assertIn(acao_esperada, acoes)


if __name__ == '__main__':
    main()
