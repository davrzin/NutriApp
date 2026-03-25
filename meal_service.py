class FoodCatalog:
    def __init__(self):
        self._items = {
            "Arroz": {"porcao": "1 colher de sopa", "calorias": 60, "carboidratos": 3, "proteinas": 0.3,
                      "gorduras": 1.6 / 16, "fibras": 3.5 / 16},
            "Feijão": {"porcao": "1 concha pequena", "calorias": 330 / 2, "carboidratos": 40 / 2, "proteinas": 15 / 2,
                       "gorduras": 1 / 2, "fibras": 15 / 2},
            "Frango Grelhado": {"porcao": "100 g", "calorias": 200, "carboidratos": 0, "proteinas": 31, "gorduras": 3.6,
                                "fibras": 0},
            "Maçã": {"porcao": "1 unidade média", "calorias": 52, "carboidratos": 14, "proteinas": 0.3, "gorduras": 0.2,
                     "fibras": 2.4},
            "Ovo Cozido": {"porcao": "1 ovo médio", "calorias": 68, "carboidratos": 0.6, "proteinas": 5.5, "gorduras": 4.8,
                           "fibras": 0},
            "Banana": {"porcao": "1 banana média", "calorias": 145, "carboidratos": 27, "proteinas": 1.3, "gorduras": 0.3,
                       "fibras": 3.1},
            "Batata Doce": {"porcao": "1 xícara cozida", "calorias": 180, "carboidratos": 41, "proteinas": 4,
                            "gorduras": 0.2, "fibras": 6.3},
            "Salmão Grelhado": {"porcao": "100 g", "calorias": 206, "carboidratos": 0, "proteinas": 25, "gorduras": 13,
                                "fibras": 0},
            "Espinafre Cozido": {"porcao": "1 xícara", "calorias": 41, "carboidratos": 7, "proteinas": 5, "gorduras": 1,
                                 "fibras": 4},
            "Abacate": {"porcao": "0.5 abacate", "calorias": 120, "carboidratos": 8.5, "proteinas": 2, "gorduras": 10.5,
                        "fibras": 6.7},
            "Tomate": {"porcao": "1 tomate médio", "calorias": 22, "carboidratos": 5, "proteinas": 1, "gorduras": 0.2,
                       "fibras": 1.5},
            "Cenoura": {"porcao": "1 cenoura média", "calorias": 25, "carboidratos": 6, "proteinas": 0.6, "gorduras": 0.1,
                        "fibras": 2},
            "Iogurte Natural": {"porcao": "1 xícara", "calorias": 150, "carboidratos": 17, "proteinas": 10, "gorduras": 8,
                                "fibras": 0},
            "Pão Integral": {"porcao": "2 fatias", "calorias": 160, "carboidratos": 28, "proteinas": 6, "gorduras": 2,
                             "fibras": 4},
            "Brócolis Cozidos": {"porcao": "1 xícara", "calorias": 55, "carboidratos": 11, "proteinas": 4, "gorduras": 0.6,
                                 "fibras": 5},
            "Carne Moída": {"porcao": "100 g", "calorias": 250, "carboidratos": 0, "proteinas": 26, "gorduras": 17,
                            "fibras": 0},
            "Laranja": {"porcao": "1 laranja média", "calorias": 62, "carboidratos": 15, "proteinas": 1.2, "gorduras": 0.2,
                        "fibras": 3.1},
            "Leite": {"porcao": "1 xícara", "calorias": 103, "carboidratos": 12, "proteinas": 8, "gorduras": 3.5,
                      "fibras": 0},
            "Atum em Água": {"porcao": "1 lata", "calorias": 100, "carboidratos": 0, "proteinas": 22, "gorduras": 1,
                             "fibras": 0},
            "Abóbora Cozida": {"porcao": "1 xícara", "calorias": 49, "carboidratos": 12, "proteinas": 2, "gorduras": 0.2,
                               "fibras": 3},
            "Ovo Frito": {"porcao": "1 ovo", "calorias": 90 / 2, "carboidratos": 1 / 2, "proteinas": 6 / 2,
                          "gorduras": 7 / 2, "fibras": 0},
            "Macarrão Cozido": {"porcao": "1 xícara", "calorias": 200 / 16, "carboidratos": 42 / 16, "proteinas": 7 / 16,
                                "gorduras": 1.3 / 16, "fibras": 2.5 / 16},
            "Pão Francês": {"porcao": "1 unidade", "calorias": 135 / 8, "carboidratos": 27 / 8, "proteinas": 4 / 8,
                            "gorduras": 1 / 8, "fibras": 1 / 8},
            "Castanha-do-Pará": {"porcao": "3 unidades", "calorias": 200 / 3, "carboidratos": 4 / 3,
                                 "proteinas": 4 / 3, "gorduras": 10, "fibras": 2 / 3},
            "Amendoim": {"porcao": "30 g", "calorias": 170 / 4, "carboidratos": 5 / 4,
                         "proteinas": 7 / 4, "gorduras": 14 / 4, "fibras": 2 / 4},
            "Pirão": {"porcao": "1 concha pequena", "calorias": 100 / 2, "carboidratos": 20 / 2, "proteinas": 2 / 2,
                      "gorduras": 1 / 2, "fibras": 0},
            "Purê de Batata": {"porcao": "0.5 xícara", "calorias": 100 / 8, "carboidratos": 26 / 8, "proteinas": 1 / 8,
                               "gorduras": 0 / 8, "fibras": 2 / 8},
            "Jerimum": {"porcao": "1 xícara cozida", "calorias": 50 / 8, "carboidratos": 12 / 8, "proteinas": 1 / 8,
                        "gorduras": 0 / 8, "fibras": 2 / 8},
            "Farinha": {"porcao": "1 colher de sopa", "calorias": 30 / 16, "carboidratos": 6 / 16, "proteinas": 1 / 16,
                        "gorduras": 0 / 16, "fibras": 0 / 16},
            "Biscoito Maisena": {"porcao": "4 biscoitos", "calorias": 160 / 4, "carboidratos": 24 / 4, "proteinas": 2 / 4,
                                 "gorduras": 6 / 4, "fibras": 0 / 4},
        }

    def get_all(self):
        return {nome: dados.copy() for nome, dados in self._items.items()}


class MealPlanner:
    def __init__(self, catalog):
        self.catalog = catalog

    @staticmethod
    def _metas_usuario(usuario):
        if hasattr(usuario, "meta") and hasattr(usuario, "email"):
            return {
                "Meta Calorica": usuario.meta.calorias,
                "Proteinas": usuario.meta.proteinas,
                "Carboidrato": usuario.meta.carboidratos,
                "Lipideos": usuario.meta.lipideos,
                "Fibras": usuario.meta.fibras,
            }

        email = usuario["Email"]
        return {
            "Meta Calorica": float(usuario["Meta Calorica " + email]),
            "Proteinas": float(usuario["Proteinas " + email]),
            "Carboidrato": float(usuario["Carboidrato " + email]),
            "Lipideos": float(usuario["Lipideos " + email]),
            "Fibras": float(usuario["Fibras " + email]),
        }

    @staticmethod
    def _sum_macros(refeicao):
        totais = {"calorias": 0, "carboidratos": 0, "proteinas": 0, "gorduras": 0, "fibras": 0}
        for alimento, dados in refeicao.items():
            if alimento == "Total de Macronutrientes":
                continue
            for macro in totais:
                totais[macro] += dados[macro]
        return totais

    @staticmethod
    def _increase_food_quantity(food, factor):
        food_updated = food.copy()

        if "porcao" in food_updated:
            parts = food_updated["porcao"].split()
            unidade = " ".join(parts[1:])
            quantidade = float(parts[0])
            food_updated["porcao"] = f"{quantidade * factor} {unidade}".strip()

        for chave in list(food_updated.keys()):
            if chave != "porcao":
                food_updated[chave] *= factor

        return food_updated

    def _increase_until_target(self, food, macro, target, approximate_excess):
        if food[macro] >= target:
            return food

        factor = target // food[macro]
        if factor > 6:
            factor = 5
        if approximate_excess:
            factor += 1

        return self._increase_food_quantity(food, factor)

    @staticmethod
    def _sum_plan_macros(plan):
        total = {"calorias": 0, "carboidratos": 0, "proteinas": 0, "gorduras": 0, "fibras": 0}
        for refeicao in plan.values():
            macro_refeicao = refeicao["Total de Macronutrientes"]
            for macro in total:
                total[macro] += macro_refeicao[macro]
        return total

    def generate_with_foods(self, usuario, foods):
        metas_usuario = self._metas_usuario(usuario)

        meta_cafe = {}
        meta_almoco = {}
        meta_lanche = {}
        meta_janta = {}

        for macro in metas_usuario:
            valor = float(metas_usuario[macro])
            meta_cafe[macro] = valor * 0.1
            meta_almoco[macro] = valor * 0.5
            meta_janta[macro] = valor * 0.3
            meta_lanche[macro] = valor * 0.1

        cafe = {
            "Ovo Frito": foods["Ovo Frito"],
            "Pão Francês": foods["Pão Francês"],
        }
        cafe["Total de Macronutrientes"] = self._sum_macros(cafe)

        if cafe["Total de Macronutrientes"]["proteinas"] <= meta_cafe["Proteinas"] * 0.8:
            cafe["Ovo Frito"] = self._increase_until_target(cafe["Ovo Frito"], "proteinas", meta_cafe["Proteinas"], False)
        cafe["Total de Macronutrientes"] = self._sum_macros(cafe)

        if cafe["Total de Macronutrientes"]["carboidratos"] <= meta_cafe["Carboidrato"] * 0.8:
            cafe["Pão Francês"] = self._increase_until_target(cafe["Pão Francês"], "carboidratos", meta_cafe["Carboidrato"], False)
        cafe["Total de Macronutrientes"] = self._sum_macros(cafe)

        almoco = {
            "Feijão": foods["Feijão"],
            "Arroz": foods["Arroz"],
            "Frango Grelhado": foods["Frango Grelhado"],
        }
        almoco["Total de Macronutrientes"] = self._sum_macros(almoco)

        if almoco["Total de Macronutrientes"]["proteinas"] <= meta_almoco["Proteinas"]:
            almoco["Frango Grelhado"] = self._increase_until_target(almoco["Frango Grelhado"], "proteinas", meta_almoco["Proteinas"], False)
        almoco["Total de Macronutrientes"] = self._sum_macros(almoco)

        if almoco["Total de Macronutrientes"]["proteinas"] <= meta_almoco["Proteinas"]:
            almoco["Feijão"] = self._increase_food_quantity(almoco["Feijão"], 2)
        if almoco["Total de Macronutrientes"]["proteinas"] <= meta_almoco["Proteinas"]:
            almoco["Feijão"] = self._increase_food_quantity(foods["Feijão"], 3)

        almoco["Total de Macronutrientes"] = self._sum_macros(almoco)

        if almoco["Total de Macronutrientes"]["carboidratos"] <= meta_almoco["Carboidrato"] * 0.9:
            almoco["Arroz"] = self._increase_until_target(almoco["Arroz"], "carboidratos", meta_almoco["Carboidrato"], False)
        almoco["Total de Macronutrientes"] = self._sum_macros(almoco)

        janta = {
            "Carne Moída": foods["Carne Moída"],
            "Batata Doce": foods["Batata Doce"],
        }
        janta["Total de Macronutrientes"] = self._sum_macros(janta)

        if janta["Total de Macronutrientes"]["proteinas"] <= meta_janta["Proteinas"]:
            janta["Carne Moída"] = self._increase_until_target(janta["Carne Moída"], "proteinas", meta_janta["Proteinas"], False)
        janta["Total de Macronutrientes"] = self._sum_macros(janta)

        if janta["Total de Macronutrientes"]["carboidratos"] <= meta_janta["Carboidrato"]:
            janta["Batata Doce"] = self._increase_until_target(janta["Batata Doce"], "carboidratos", meta_janta["Carboidrato"], False)
        janta["Total de Macronutrientes"] = self._sum_macros(janta)

        lanche = {
            "Biscoito Maisena": foods["Biscoito Maisena"],
            "Banana": foods["Banana"],
            "Castanha-do-Pará": foods["Castanha-do-Pará"],
        }
        lanche["Total de Macronutrientes"] = self._sum_macros(lanche)

        plano = {
            "Café da manhã": cafe,
            "Almoço": almoco,
            "Lanche": lanche,
            "Janta": janta,
        }

        meta_lipideo_usuario = float(metas_usuario["Lipideos"])
        gordura_total = self._sum_plan_macros(plano)["gorduras"]

        if meta_lipideo_usuario > gordura_total:
            lanche["Castanha-do-Pará"] = self._increase_until_target(
                lanche["Castanha-do-Pará"],
                "gorduras",
                meta_lipideo_usuario - gordura_total,
                False,
            )
        lanche["Total de Macronutrientes"] = self._sum_macros(lanche)
        plano["Lanche"] = lanche

        return plano

    def generate(self, usuario):
        return self.generate_with_foods(usuario, self.catalog.get_all())

    def meal_text(self, usuario, meal_name):
        plan = self.generate(usuario)
        refeicao = plan[meal_name]

        alimentos = [nome for nome in refeicao.keys() if nome != "Total de Macronutrientes"]
        texto = ""
        for alimento in alimentos:
            texto += f"{alimento}: {refeicao[alimento]['porcao']}\n"

        texto += "\n"

        for macro, valor in refeicao["Total de Macronutrientes"].items():
            texto += f"{macro}: {valor:.1f}\n"

        substituicoes = {
            "calorias": "Calorias",
            "proteinas": "Proteínas",
            "carboidratos": "Carboidratos",
            "gorduras": "Lipídeos",
            "fibras": "Fíbras",
        }

        for original, novo in substituicoes.items():
            texto = texto.replace(original, novo)

        return texto
