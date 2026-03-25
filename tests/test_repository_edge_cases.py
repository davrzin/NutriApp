import csv
import tempfile
import unittest
from pathlib import Path

from user_repository_csv import UserRepositoryCsv


class TestRepositoryEdgeCases(unittest.TestCase):
    def test_csv_vazio_retorna_sem_usuarios(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = Path(tmp) / "vazio.csv"
            arquivo.write_text("", encoding="utf-8")

            repo = UserRepositoryCsv(str(arquivo))
            usuarios = repo.carregar_usuarios()

            self.assertEqual(usuarios, {})

    def test_csv_com_colunas_faltantes(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = Path(tmp) / "faltando_colunas.csv"
            with open(arquivo, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["email", "senha"])
                writer.writerow(["a@a.com", "123"])

            repo = UserRepositoryCsv(str(arquivo))
            usuario = repo.buscar_usuario("a@a.com")

            self.assertIsNotNone(usuario)
            assert usuario is not None
            self.assertEqual(usuario.nome, "")
            self.assertEqual(usuario.meta.calorias, 0)

    def test_csv_com_valores_invalidos_numericos(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = Path(tmp) / "invalidos.csv"
            with open(arquivo, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "email",
                    "senha",
                    "nome",
                    "sexo",
                    "idade",
                    "peso",
                    "altura",
                    "objetivo",
                    "nivel_fisico",
                    "meta_calorias",
                    "meta_proteinas",
                    "meta_carboidratos",
                    "meta_lipideos",
                    "meta_fibras",
                    "meta_agua_ml",
                    "diario_calorias",
                    "diario_proteinas",
                    "diario_carboidratos",
                    "diario_lipideos",
                    "diario_fibras",
                    "diario_agua_ml",
                ])
                writer.writerow([
                    "a@a.com",
                    "123",
                    "A",
                    "Masculino",
                    "x",
                    "y",
                    "z",
                    "Manter Peso",
                    "Moderada",
                    "nanx",
                    "-",
                    "abc",
                    "1,2",
                    "erro",
                    "xpto",
                    "err",
                    "err",
                    "err",
                    "err",
                    "err",
                    "err",
                ])

            repo = UserRepositoryCsv(str(arquivo))
            usuario = repo.buscar_usuario("a@a.com")

            self.assertIsNotNone(usuario)
            assert usuario is not None
            self.assertEqual(usuario.idade, 0)
            self.assertEqual(usuario.peso, 0.0)
            self.assertEqual(usuario.meta.carboidratos, 0.0)
            self.assertEqual(usuario.diario.calorias, 0.0)

    def test_salvamentos_sequenciais_persistem(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = Path(tmp) / "sequencial.csv"
            repo = UserRepositoryCsv(str(arquivo))
            repo.garantir_arquivo()

            repo.atualizar_agua_diaria("nao_existe@x.com", 250)
            usuarios = repo.carregar_usuarios()
            self.assertEqual(len(usuarios), 0)


if __name__ == "__main__":
    unittest.main()
