import unittest
from unittest.mock import patch
from main import main, ordens


class TestOrdem(unittest.TestCase):

    def test_ordem(self):
        inputs = ["2", "746.197.580-35", "Itaú Unibanco", "ITUB4", 27.88, 500, "05/08/2023", "sim", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        ordem_esperada = {
            "nome": "ITAÚ UNIBANCO",
            "ticket": "ITUB4",
            "valor_compra": 27.88,
            "quantidade_compra": 500,
            "data_compra": "05/08/2023",
            "cliente_id": 15
        }

        self.assertIn(ordem_esperada, ordens)


if __name__ == '__main__':
    main()
