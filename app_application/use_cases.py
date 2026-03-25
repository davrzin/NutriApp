from __future__ import annotations

from dataclasses import dataclass

from app_domain.contracts import UserRepository
from app_domain.models import RegistroDiario, Usuario
from services import CadastroValidator

from .errors import ApplicationError


@dataclass(frozen=True)
class CadastroInput:
	email: str
	senha: str
	nome: str
	sexo: str
	idade: str
	peso: str
	altura: str
	objetivo: str
	nivel_fisico: str

	@classmethod
	def from_dict(cls, data: dict[str, str]) -> "CadastroInput":
		campos = (
			"email",
			"senha",
			"nome",
			"sexo",
			"idade",
			"peso",
			"altura",
			"objetivo",
			"nivel_fisico",
		)
		faltantes = [campo for campo in campos if campo not in data]
		if faltantes:
			raise ApplicationError("cadastro.payload_invalido")

		return cls(
			email=data["email"],
			senha=data["senha"],
			nome=data["nome"],
			sexo=data["sexo"],
			idade=data["idade"],
			peso=data["peso"],
			altura=data["altura"],
			objetivo=data["objetivo"],
			nivel_fisico=data["nivel_fisico"],
		)


class LoginUseCase:
	def __init__(self, repo: UserRepository):
		self.repo = repo

	def executar(self, email: str, senha: str) -> Usuario:
		if not (email and senha):
			raise ApplicationError("login.campos_obrigatorios")

		usuario = self.repo.buscar_usuario(email)
		if usuario is None:
			raise ApplicationError("login.email_nao_encontrado")
		if usuario.senha != senha:
			raise ApplicationError("login.senha_incorreta")
		return usuario


class CadastroUseCase:
	def __init__(self, repo: UserRepository, nutrition_service):
		self.repo = repo
		self.nutrition_service = nutrition_service

	def validar(self, data: CadastroInput, usuarios: dict[str, Usuario]) -> str | None:
		if not data.email:
			return "cadastro.email_obrigatorio"
		if not CadastroValidator.validar_email(data.email):
			return "cadastro.email_invalido"
		if data.email in usuarios:
			return "cadastro.email_duplicado"
		if not data.senha:
			return "cadastro.senha_obrigatoria"
		if not CadastroValidator.validar_senha(data.senha):
			return "cadastro.senha_invalida"
		if not data.nome:
			return "cadastro.nome_obrigatorio"
		if (not data.sexo) or data.sexo.startswith("Selecione"):
			return "cadastro.sexo_obrigatorio"
		if not data.idade:
			return "cadastro.idade_obrigatoria"
		if not CadastroValidator.validar_idade(data.idade):
			return "cadastro.idade_invalida"
		if not data.peso:
			return "cadastro.peso_obrigatorio"
		if not CadastroValidator.validar_peso(data.peso):
			return "cadastro.peso_invalido"
		if not data.altura:
			return "cadastro.altura_obrigatoria"
		if not CadastroValidator.validar_altura(data.altura):
			return "cadastro.altura_invalida"
		if (not data.objetivo) or data.objetivo.startswith("Selecione"):
			return "cadastro.objetivo_obrigatorio"
		if (not data.nivel_fisico) or data.nivel_fisico.startswith("Selecione"):
			return "cadastro.nivel_fisico_obrigatorio"
		return None

	def criar_usuario(self, data: CadastroInput) -> Usuario:
		idade = int(data.idade)
		peso = float(data.peso)
		altura = float(data.altura)
		nivel_fisico = self.nutrition_service.normalizar_nivel_fisico(data.nivel_fisico)

		meta = self.nutrition_service.calcular_meta_usuario(
			data.sexo,
			idade,
			peso,
			altura,
			data.objetivo,
			nivel_fisico,
		)

		return Usuario(
			email=data.email,
			senha=data.senha,
			nome=data.nome,
			sexo=data.sexo,
			idade=idade,
			peso=peso,
			altura=altura,
			objetivo=data.objetivo,
			nivel_fisico=nivel_fisico,
			meta=meta,
			diario=RegistroDiario(),
		)

	def executar(self, data_bruta: dict[str, str]) -> Usuario:
		data = CadastroInput.from_dict(data_bruta)
		usuarios = self.repo.carregar_usuarios()
		erro = self.validar(data, usuarios)
		if erro:
			raise ApplicationError(erro)

		usuario = self.criar_usuario(data)
		self.repo.salvar_usuario(usuario)
		return usuario


__all__ = ["CadastroInput", "CadastroUseCase", "LoginUseCase"]
