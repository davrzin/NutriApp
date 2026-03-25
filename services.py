import re
from app_domain import MetaNutricional


class CadastroValidator:
    @staticmethod
    def validar_email(email_input):
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao_email, email_input))

    @staticmethod
    def validar_senha(senha_input):
        # Pelo menos 8 caracteres, 1 maiuscula, 1 minuscula e 1 numero.
        padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
        return bool(re.match(padrao_senha, senha_input))

    @staticmethod
    def validar_idade(input_idade):
        try:
            return int(input_idade) >= 12
        except ValueError:
            return False

    @staticmethod
    def validar_altura(input_altura):
        try:
            return 251 >= int(input_altura) >= 100
        except ValueError:
            return False

    @staticmethod
    def validar_peso(input_peso):
        try:
            return float(input_peso) > 0
        except ValueError:
            return False


class NutritionService:
    @staticmethod
    def normalizar_nivel_fisico(nivel_fisico):
        mapa = {
            "Sedentário": "Sedentário",
            "Moderada": "Moderada",
            "Intensa": "Intensa",
            "Intesa": "Intensa",
        }
        return mapa.get(nivel_fisico, "Intensa")

    @staticmethod
    def calcular_tmb(sexo, idade, peso, altura):
        if sexo == "Masculino":
            return 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
        return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

    @classmethod
    def calorias_ajustadas(cls, sexo, idade, peso, altura, nivel_fisico):
        tmb = cls.calcular_tmb(sexo, idade, peso, altura)
        nivel_fisico = cls.normalizar_nivel_fisico(nivel_fisico)

        fatores = {
            "Sedentário": 1.2,
            "Moderada": 1.55,
            "Intensa": 1.725,
        }
        return tmb * fatores[nivel_fisico]

    @classmethod
    def calorias_objetivo(cls, sexo, idade, peso, altura, objetivo, nivel_fisico):
        calorias_ajustadas = cls.calorias_ajustadas(sexo, idade, peso, altura, nivel_fisico)
        fatores_objetivo = {
            "Perder Peso": 0.85,
            "Manter Peso": 1.0,
            "Ganhar Peso": 1.15,
        }
        return calorias_ajustadas * fatores_objetivo.get(objetivo, 1.0)

    @classmethod
    def calcular_macronutrientes_meta(cls, sexo, idade, peso, altura, objetivo, nivel_fisico):
        nivel_fisico = cls.normalizar_nivel_fisico(nivel_fisico)
        meta_calorica = cls.calorias_objetivo(sexo, idade, peso, altura, objetivo, nivel_fisico)

        calorias_carboidrato = 4
        calorias_lipideos = 9

        distribuicao = {
            "Sedentário": {"proteina_por_kg": 0.8, "carbo": 0.45, "lipideo": 0.25, "fibras": 25},
            "Moderada": {"proteina_por_kg": 1.5, "carbo": 0.50, "lipideo": 0.30, "fibras": 30},
            "Intensa": {"proteina_por_kg": 2.0, "carbo": 0.55, "lipideo": 0.35, "fibras": 35},
        }
        plano = distribuicao[nivel_fisico]

        gramas_proteinas = peso * plano["proteina_por_kg"]
        gramas_carboidrato = plano["carbo"] * meta_calorica / calorias_carboidrato
        gramas_lipideos = plano["lipideo"] * meta_calorica / calorias_lipideos
        gramas_fibras = plano["fibras"]
        ml_agua = peso * 35

        return meta_calorica, gramas_proteinas, gramas_carboidrato, gramas_lipideos, gramas_fibras, ml_agua

    @classmethod
    def calcular_meta_usuario(cls, sexo, idade, peso, altura, objetivo, nivel_fisico) -> MetaNutricional:
        meta_calorica, gramas_proteinas, gramas_carboidrato, gramas_lipideos, gramas_fibras, ml_agua = (
            cls.calcular_macronutrientes_meta(sexo, idade, peso, altura, objetivo, nivel_fisico)
        )
        return MetaNutricional(
            calorias=meta_calorica,
            proteinas=gramas_proteinas,
            carboidratos=gramas_carboidrato,
            lipideos=gramas_lipideos,
            fibras=gramas_fibras,
            agua_ml=ml_agua,
        )
