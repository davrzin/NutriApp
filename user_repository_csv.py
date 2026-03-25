from __future__ import annotations

import csv
from pathlib import Path

from app_domain import MetaNutricional, RegistroDiario, Usuario


class UserRepositoryCsv:
    _CAMPOS_CSV = [
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
    ]

    def __init__(self, caminho_arquivo="dados.csv"):
        self.caminho_arquivo = caminho_arquivo

    @staticmethod
    def _to_int(value: str | None, default: int = 0) -> int:
        try:
            return int(float(value or default))
        except (TypeError, ValueError):
            return default

    @staticmethod
    def _to_float(value: str | None, default: float = 0.0) -> float:
        try:
            return float(value or default)
        except (TypeError, ValueError):
            return default

    def garantir_arquivo(self):
        caminho = Path(self.caminho_arquivo)
        if caminho.exists():
            return

        with open(self.caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=self._CAMPOS_CSV)
            writer.writeheader()

    def _usuario_from_row(self, row: dict[str, str]) -> Usuario:
        return Usuario(
            email=row["email"],
            senha=row.get("senha", ""),
            nome=row.get("nome", ""),
            sexo=row.get("sexo", "Masculino"),
            idade=self._to_int(row.get("idade")),
            peso=self._to_float(row.get("peso")),
            altura=self._to_float(row.get("altura")),
            objetivo=row.get("objetivo", "Manter Peso"),
            nivel_fisico=row.get("nivel_fisico", "Sedentário"),
            meta=MetaNutricional(
                calorias=self._to_float(row.get("meta_calorias")),
                proteinas=self._to_float(row.get("meta_proteinas")),
                carboidratos=self._to_float(row.get("meta_carboidratos")),
                lipideos=self._to_float(row.get("meta_lipideos")),
                fibras=self._to_float(row.get("meta_fibras")),
                agua_ml=self._to_float(row.get("meta_agua_ml")),
            ),
            diario=RegistroDiario(
                calorias=self._to_float(row.get("diario_calorias")),
                proteinas=self._to_float(row.get("diario_proteinas")),
                carboidratos=self._to_float(row.get("diario_carboidratos")),
                lipideos=self._to_float(row.get("diario_lipideos")),
                fibras=self._to_float(row.get("diario_fibras")),
                agua_ml=self._to_float(row.get("diario_agua_ml")),
            ),
        )

    def _usuario_to_row(self, usuario: Usuario) -> dict[str, str]:
        return {
            "email": usuario.email,
            "senha": usuario.senha,
            "nome": usuario.nome,
            "sexo": usuario.sexo,
            "idade": str(usuario.idade),
            "peso": str(usuario.peso),
            "altura": str(usuario.altura),
            "objetivo": usuario.objetivo,
            "nivel_fisico": usuario.nivel_fisico,
            "meta_calorias": str(usuario.meta.calorias),
            "meta_proteinas": str(usuario.meta.proteinas),
            "meta_carboidratos": str(usuario.meta.carboidratos),
            "meta_lipideos": str(usuario.meta.lipideos),
            "meta_fibras": str(usuario.meta.fibras),
            "meta_agua_ml": str(usuario.meta.agua_ml),
            "diario_calorias": str(usuario.diario.calorias),
            "diario_proteinas": str(usuario.diario.proteinas),
            "diario_carboidratos": str(usuario.diario.carboidratos),
            "diario_lipideos": str(usuario.diario.lipideos),
            "diario_fibras": str(usuario.diario.fibras),
            "diario_agua_ml": str(usuario.diario.agua_ml),
        }

    def carregar_usuarios(self) -> dict[str, Usuario]:
        usuarios: dict[str, Usuario] = {}
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8", newline="") as arquivo:
                leitor = csv.DictReader(arquivo)
                for row in leitor:
                    if not row.get("email"):
                        continue
                    usuario = self._usuario_from_row(row)
                    usuarios[usuario.email] = usuario
        except FileNotFoundError:
            return usuarios
        return usuarios

    def buscar_usuario(self, email: str) -> Usuario | None:
        return self.carregar_usuarios().get(email)

    def salvar_usuario(self, usuario: Usuario):
        usuarios = self.carregar_usuarios()
        usuarios[usuario.email] = usuario
        self._persistir_usuarios(usuarios)

    def _persistir_usuarios(self, usuarios: dict[str, Usuario]):
        with open(self.caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=self._CAMPOS_CSV)
            writer.writeheader()
            for usuario in usuarios.values():
                writer.writerow(self._usuario_to_row(usuario))

    def atualizar_agua_diaria(self, email_usuario_logado, incremento):
        usuarios = self.carregar_usuarios()
        usuario = usuarios.get(email_usuario_logado)
        if usuario is None:
            return
        usuario.diario.agua_ml += int(incremento)
        self._persistir_usuarios(usuarios)

    def atualizar_macros_diarios(
        self,
        email_usuario_logado,
        calorias_alteracoes,
        proteinas_alteracoes,
        carboidratos_alteracoes,
        lipideos_alteracoes,
        fibras_alteracoes,
    ):
        usuarios = self.carregar_usuarios()
        usuario = usuarios.get(email_usuario_logado)
        if usuario is None:
            return

        usuario.diario.calorias += calorias_alteracoes
        usuario.diario.proteinas += proteinas_alteracoes
        usuario.diario.carboidratos += carboidratos_alteracoes
        usuario.diario.lipideos += lipideos_alteracoes
        usuario.diario.fibras += fibras_alteracoes
        self._persistir_usuarios(usuarios)

    def buscar_metricas_usuario(self, email_usuario_logado):
        usuario = self.buscar_usuario(email_usuario_logado)
        if usuario is None:
            return {}

        email = usuario.email
        return {
            f"Meta Calorica {email}": str(usuario.meta.calorias),
            f"Proteinas {email}": str(usuario.meta.proteinas),
            f"Carboidrato {email}": str(usuario.meta.carboidratos),
            f"Lipideos {email}": str(usuario.meta.lipideos),
            f"Fibras {email}": str(usuario.meta.fibras),
            f"Agua {email}": str(usuario.meta.agua_ml),
            f"Meta Calorica Diaria {email}": str(usuario.diario.calorias),
            f"Proteinas Diarias {email}": str(usuario.diario.proteinas),
            f"Carboidrato Diarios {email}": str(usuario.diario.carboidratos),
            f"Lipideos Diarios {email}": str(usuario.diario.lipideos),
            f"Fibras Diarias {email}": str(usuario.diario.fibras),
            f"Agua Diaria {email}": str(usuario.diario.agua_ml),
        }
