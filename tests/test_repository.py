import tempfile
import unittest
from pathlib import Path

from app_domain import MetaNutricional, RegistroDiario, Usuario
from user_repository_csv import UserRepositoryCsv


def usuario_exemplo(email="repo@email.com"):
    return Usuario(
        email=email,
        senha="Aa123456",
        nome="Repo",
        sexo="Feminino",
        idade=30,
        peso=60.0,
        altura=165.0,
        objetivo="Manter Peso",
        nivel_fisico="Sedentário",
        meta=MetaNutricional(1800, 80, 200, 60, 25, 2100),
        diario=RegistroDiario(),
    )


class TestUserRepositoryCsv(unittest.TestCase):
    def test_salvar_e_buscar_usuario(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = Path(tmp) / "dados_teste.csv"
            repo = UserRepositoryCsv(str(arquivo))
            repo.garantir_arquivo()

            usuario = usuario_exemplo()
            repo.salvar_usuario(usuario)

            encontrado = repo.buscar_usuario(usuario.email)
            self.assertIsNotNone(encontrado)
            assert encontrado is not None
            self.assertEqual(encontrado.email, usuario.email)
            self.assertEqual(encontrado.meta.calorias, 1800)

    def test_atualizar_agua_e_macros_diarios(self):
        with tempfile.TemporaryDirectory() as tmp:
            arquivo = Path(tmp) / "dados_teste.csv"
            repo = UserRepositoryCsv(str(arquivo))
            repo.garantir_arquivo()

            usuario = usuario_exemplo()
            repo.salvar_usuario(usuario)

            repo.atualizar_agua_diaria(usuario.email, 250)
            repo.atualizar_macros_diarios(usuario.email, 100, 10, 20, 5, 3)

            atualizado = repo.buscar_usuario(usuario.email)
            self.assertIsNotNone(atualizado)
            assert atualizado is not None
            self.assertEqual(atualizado.diario.agua_ml, 250)
            self.assertEqual(atualizado.diario.calorias, 100)
            self.assertEqual(atualizado.diario.proteinas, 10)
            self.assertEqual(atualizado.diario.carboidratos, 20)
            self.assertEqual(atualizado.diario.lipideos, 5)
            self.assertEqual(atualizado.diario.fibras, 3)


if __name__ == "__main__":
    unittest.main()
