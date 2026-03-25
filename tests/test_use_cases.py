import unittest

from app_application import ApplicationError, CadastroUseCase, LoginUseCase
from app_domain import MetaNutricional, RegistroDiario, Usuario
from services import NutritionService


class FakeRepo:
    def __init__(self):
        self.usuarios = {}

    def garantir_arquivo(self):
        return None

    def carregar_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, email):
        return self.usuarios.get(email)

    def salvar_usuario(self, usuario):
        self.usuarios[usuario.email] = usuario

    def atualizar_agua_diaria(self, email_usuario_logado, incremento):
        return None

    def atualizar_macros_diarios(
        self,
        email_usuario_logado,
        calorias_alteracoes,
        proteinas_alteracoes,
        carboidratos_alteracoes,
        lipideos_alteracoes,
        fibras_alteracoes,
    ):
        return None


def usuario_exemplo(email="davi@email.com", senha="Aa123456"):
    return Usuario(
        email=email,
        senha=senha,
        nome="Davi",
        sexo="Masculino",
        idade=24,
        peso=78.0,
        altura=178.0,
        objetivo="Manter Peso",
        nivel_fisico="Moderada",
        meta=MetaNutricional(2200, 120, 250, 70, 30, 2700),
        diario=RegistroDiario(),
    )


class TestLoginUseCase(unittest.TestCase):
    def test_login_com_sucesso(self):
        repo = FakeRepo()
        repo.salvar_usuario(usuario_exemplo())

        caso = LoginUseCase(repo)
        usuario = caso.executar("davi@email.com", "Aa123456")

        self.assertEqual(usuario.email, "davi@email.com")

    def test_login_sem_campos(self):
        caso = LoginUseCase(FakeRepo())
        with self.assertRaises(ApplicationError):
            caso.executar("", "")

    def test_login_senha_incorreta(self):
        repo = FakeRepo()
        repo.salvar_usuario(usuario_exemplo())

        caso = LoginUseCase(repo)
        with self.assertRaises(ApplicationError):
            caso.executar("davi@email.com", "senha_errada")


class TestCadastroUseCase(unittest.TestCase):
    def test_cadastro_salva_usuario(self):
        repo = FakeRepo()
        caso = CadastroUseCase(repo, NutritionService)

        data = {
            "email": "novo@email.com",
            "senha": "Aa123456",
            "nome": "Novo",
            "sexo": "Masculino",
            "idade": "21",
            "peso": "75",
            "altura": "180",
            "objetivo": "Manter Peso",
            "nivel_fisico": "Moderada",
        }

        usuario = caso.executar(data)

        self.assertEqual(usuario.email, "novo@email.com")
        self.assertIn("novo@email.com", repo.usuarios)

    def test_cadastro_email_duplicado(self):
        repo = FakeRepo()
        repo.salvar_usuario(usuario_exemplo(email="dup@email.com"))
        caso = CadastroUseCase(repo, NutritionService)

        data = {
            "email": "dup@email.com",
            "senha": "Aa123456",
            "nome": "Novo",
            "sexo": "Masculino",
            "idade": "21",
            "peso": "75",
            "altura": "180",
            "objetivo": "Manter Peso",
            "nivel_fisico": "Moderada",
        }

        with self.assertRaises(ApplicationError):
            caso.executar(data)

    def test_cadastro_payload_invalido(self):
        repo = FakeRepo()
        caso = CadastroUseCase(repo, NutritionService)

        data = {
            "email": "novo@email.com",
            "senha": "Aa123456",
        }

        with self.assertRaises(ApplicationError) as erro:
            caso.executar(data)

        self.assertEqual(erro.exception.code, "cadastro.payload_invalido")


if __name__ == "__main__":
    unittest.main()
