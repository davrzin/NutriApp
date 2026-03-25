import unittest

from ui_views import filter_food_options


class TestUiFilter(unittest.TestCase):
    def test_filter_retorna_todos_quando_vazio(self):
        opcoes = ["Frango Grelhado", "Arroz", "Batata Doce"]
        self.assertEqual(filter_food_options(opcoes, ""), opcoes)

    def test_filter_por_contains_case_insensitive(self):
        opcoes = ["Frango Grelhado", "Arroz", "Batata Doce"]
        self.assertEqual(filter_food_options(opcoes, "fran"), ["Frango Grelhado"])
        self.assertEqual(filter_food_options(opcoes, "DOCE"), ["Batata Doce"])

    def test_filter_sem_resultado(self):
        opcoes = ["Frango Grelhado", "Arroz", "Batata Doce"]
        self.assertEqual(filter_food_options(opcoes, "peixe"), [])


if __name__ == "__main__":
    unittest.main()
