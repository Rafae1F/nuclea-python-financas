import unittest
from unittest.mock import patch
from main import main, ordens


class TestOrdem(unittest.TestCase):

    def test_ordem(self):
        inputs = ["2", "519.403.168-80", "Itaú Unibanco", "ITUB4", 23.84, 500, "01/08/2023", "sim", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        ordem_esperada = {
            "nome": "Itaú Unibanco",
            "ticket": "ITUB4",
            "valor_compra": 23.84,
            "quantidade_compra": 500,
            "data_compra": "01/08/2023"
        }

        self.assertIn(ordem_esperada, ordens)


if __name__ == '__main__':
    main()
