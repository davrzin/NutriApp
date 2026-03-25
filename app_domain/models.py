from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"


class Objetivo(Enum):
    GANHAR_PESO = "Ganhar Peso"
    PERDER_PESO = "Perder Peso"
    MANTER_PESO = "Manter Peso"


class NivelAtividade(Enum):
    SEDENTARIO = "Sedentário"
    MODERADA = "Moderada"
    INTENSA = "Intensa"

    @classmethod
    def from_text(cls, valor: str) -> "NivelAtividade":
        mapa = {
            "Sedentário": cls.SEDENTARIO,
            "Moderada": cls.MODERADA,
            "Intensa": cls.INTENSA,
            "Intesa": cls.INTENSA,
        }
        return mapa.get(valor, cls.INTENSA)


@dataclass(frozen=True)
class MetaNutricional:
    calorias: float
    proteinas: float
    carboidratos: float
    lipideos: float
    fibras: float
    agua_ml: float


@dataclass
class RegistroDiario:
    calorias: float = 0.0
    proteinas: float = 0.0
    carboidratos: float = 0.0
    lipideos: float = 0.0
    fibras: float = 0.0
    agua_ml: float = 0.0


@dataclass
class Usuario:
    email: str
    senha: str
    nome: str
    sexo: str
    idade: int
    peso: float
    altura: float
    objetivo: str
    nivel_fisico: str
    meta: MetaNutricional
    diario: RegistroDiario


@dataclass(frozen=True)
class Alimento:
    porcao: str
    calorias: float
    carboidratos: float
    proteinas: float
    gorduras: float
    fibras: float


__all__ = [
    "Alimento",
    "MetaNutricional",
    "NivelAtividade",
    "Objetivo",
    "RegistroDiario",
    "Sexo",
    "Usuario",
]
