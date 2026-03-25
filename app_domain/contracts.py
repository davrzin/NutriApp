from __future__ import annotations

from typing import Protocol

from .models import Usuario


class UserRepository(Protocol):
	def garantir_arquivo(self) -> None:
		...

	def carregar_usuarios(self) -> dict[str, Usuario]:
		...

	def buscar_usuario(self, email: str) -> Usuario | None:
		...

	def salvar_usuario(self, usuario: Usuario) -> None:
		...

	def atualizar_agua_diaria(self, email_usuario_logado: str, incremento: int) -> None:
		...

	def atualizar_macros_diarios(
		self,
		email_usuario_logado: str,
		calorias_alteracoes: float,
		proteinas_alteracoes: float,
		carboidratos_alteracoes: float,
		lipideos_alteracoes: float,
		fibras_alteracoes: float,
	) -> None:
		...


__all__ = ["UserRepository"]
