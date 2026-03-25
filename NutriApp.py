import customtkinter as ctk
from tkinter import messagebox

from app_domain import Usuario
from services import NutritionService
from app_infra import UserRepositoryCsv
from meal_service import FoodCatalog, MealPlanner
from app_presentation import LoginView, CadastroView, DashboardView, FoodsView
from app_application import ApplicationError, CadastroUseCase, LoginUseCase


class AppController:
    _ERROR_MESSAGES = {
        "login.campos_obrigatorios": "Todos os campos são obrigatórios.\nPor favor, preencha todos os campos.",
        "login.email_nao_encontrado": "Email não encontrado.",
        "login.senha_incorreta": "Senha incorreta.",
        "cadastro.payload_invalido": "Dados de cadastro inválidos. Tente novamente.",
        "cadastro.email_obrigatorio": "O campo 'Email' deve ser preenchido",
        "cadastro.email_invalido": "O email é Inválido.\nSeu email deve conter: @, .br ou .com\nEx: davi@gmail.com",
        "cadastro.email_duplicado": "Email já cadastrado.",
        "cadastro.senha_obrigatoria": "O campo 'Senha' deve ser preenchido",
        "cadastro.senha_invalida": (
            "A senha é inválida. Tente novamente.\n"
            "Sua senha deve conter: Pelo menos 8 digitos, 1 letra maiúscula, 1 letra minúscula e 1 número\n"
            "Ex: Aa123456"
        ),
        "cadastro.nome_obrigatorio": "O campo 'Nome' deve ser preenchido",
        "cadastro.sexo_obrigatorio": "O campo 'Sexo' deve ser preenchido",
        "cadastro.idade_obrigatoria": "O campo 'Idade' deve ser preenchido",
        "cadastro.idade_invalida": "Por favor, insira uma idade válida maior que 12 anos(número inteiro positivo).",
        "cadastro.peso_obrigatorio": "O campo 'Peso' deve ser preenchido",
        "cadastro.peso_invalido": "Por favor, insira um peso válido (número positivo em Kg).",
        "cadastro.altura_obrigatoria": "O campo 'Altura' deve ser preenchido",
        "cadastro.altura_invalida": (
            "Por favor, insira uma altura válida maior que 100 cm e menor/igual que 251/igual cm\n"
            "(número positivo em centimetros)\nEx: 180"
        ),
        "cadastro.objetivo_obrigatorio": "O campo 'Objetivo' deve ser preenchido",
        "cadastro.nivel_fisico_obrigatorio": "O campo 'Nivel de Atividade Física' deve ser preenchido",
    }

    def __init__(self, janela):
        self.janela = janela
        self.repo = UserRepositoryCsv("dados.csv")
        self.catalogo = FoodCatalog()
        self.planejador = MealPlanner(self.catalogo)
        self.login_use_case = LoginUseCase(self.repo)
        self.cadastro_use_case = CadastroUseCase(self.repo, NutritionService)
        self.usuario_logado: Usuario | None = None

    def iniciar(self):
        self.repo.garantir_arquivo()
        self.mostrar_login()

    def mostrar_mensagem(self, titulo, conteudo):
        messagebox.showinfo(titulo, conteudo)

    def _message_for_error(self, code: str) -> str:
        return self._ERROR_MESSAGES.get(code, "Ocorreu um erro inesperado.")

    def _obter_usuario_logado(self) -> Usuario:
        if self.usuario_logado is None:
            raise RuntimeError("Nenhum usuário está logado.")
        return self.usuario_logado

    def _calcular_percentuais(self):
        usuario_logado = self._obter_usuario_logado()
        calorias = usuario_logado.diario.calorias
        proteinas = usuario_logado.diario.proteinas
        carboidratos = usuario_logado.diario.carboidratos
        lipideos = usuario_logado.diario.lipideos
        fibras = usuario_logado.diario.fibras
        agua = usuario_logado.diario.agua_ml
        agua_meta = usuario_logado.meta.agua_ml or 1

        cardapio = self.planejador.generate(usuario_logado)
        calorias_meta = 0
        proteinas_meta = 0
        carboidratos_meta = 0
        lipideos_meta = 0
        fibras_meta = 0

        for refeicao in cardapio.values():
            totais = refeicao["Total de Macronutrientes"]
            calorias_meta += totais["calorias"]
            proteinas_meta += totais["proteinas"]
            carboidratos_meta += totais["carboidratos"]
            lipideos_meta += totais["gorduras"]
            fibras_meta += totais["fibras"]

        def percentual(valor_atual, valor_meta):
            if float(valor_meta) == 0:
                return 0
            return float(valor_atual) / float(valor_meta) * 100

        return (
            percentual(calorias, calorias_meta),
            percentual(proteinas, proteinas_meta),
            percentual(carboidratos, carboidratos_meta),
            percentual(lipideos, lipideos_meta),
            percentual(fibras, fibras_meta),
            percentual(agua, agua_meta),
        )

    def mostrar_login(self):
        LoginView(self.janela).render(self._acao_login, self.mostrar_cadastro)

    def mostrar_cadastro(self):
        CadastroView(self.janela).render(self._acao_cadastro, self.mostrar_login)

    def mostrar_dashboard(self):
        DashboardView(self.janela).render(
            self._calcular_percentuais(),
            self.mostrar_lista_alimentos,
            self._acao_logout,
            self.mostrar_mensagem,
        )

    def _acao_logout(self):
        self.usuario_logado = None
        self.mostrar_login()

    def mostrar_lista_alimentos(self):
        usuario_dados = self._obter_usuario_logado()

        meal_texts = {
            "Café da manhã": self.planejador.meal_text(usuario_dados, "Café da manhã"),
            "Almoço": self.planejador.meal_text(usuario_dados, "Almoço"),
            "Lanche": self.planejador.meal_text(usuario_dados, "Lanche"),
            "Janta": self.planejador.meal_text(usuario_dados, "Janta"),
        }

        opcoes = list(self.catalogo.get_all().keys()) + list(self.planejador.generate(usuario_dados).keys())

        FoodsView(self.janela).render(
            meal_texts,
            opcoes,
            self._acao_selecionar_alimento,
            self.mostrar_dashboard,
            self._acao_adicionar_agua,
        )

    def _acao_login(self, email_digitado, senha_digitada):
        try:
            self.usuario_logado = self.login_use_case.executar(email_digitado, senha_digitada)
            self.mostrar_dashboard()
        except ApplicationError as erro:
            self.mostrar_mensagem("Erro", self._message_for_error(erro.code))

    def _acao_cadastro(self, data):
        try:
            self.cadastro_use_case.executar(data)
            self.mostrar_mensagem("Sucesso", "Cadastro Concluido")
            self.mostrar_login()
        except ApplicationError as erro:
            self.mostrar_mensagem("Erro", self._message_for_error(erro.code))

    def _acao_adicionar_agua(self):
        usuario_logado = self._obter_usuario_logado()
        email = usuario_logado.email
        self.repo.atualizar_agua_diaria(email, 250)
        self.usuario_logado = self.repo.buscar_usuario(email)
        self.mostrar_mensagem("Sucesso", "250 ml's de Água Adicionados!(1 copo)")

    def _acao_selecionar_alimento(self, opcao_selecionada):
        if opcao_selecionada == "Nenhum resultado encontrado":
            return

        usuario_logado = self._obter_usuario_logado()
        email = usuario_logado.email
        usuario_dados = usuario_logado

        cardapio_base = self.catalogo.get_all()
        if opcao_selecionada in cardapio_base:
            macros = cardapio_base[opcao_selecionada].copy()
            macros.pop("porcao", None)
        else:
            macros = self.planejador.generate(usuario_dados)[opcao_selecionada]["Total de Macronutrientes"]

        self.repo.atualizar_macros_diarios(
            email,
            macros.get("calorias", 0),
            macros.get("proteinas", 0),
            macros.get("carboidratos", 0),
            macros.get("gorduras", 0),
            macros.get("fibras", 0),
        )
        self.usuario_logado = self.repo.buscar_usuario(email)
        self.mostrar_mensagem("Sucesso", "Calorias e Macro-Nutrientes Atualizados!")


# Inicialização do app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.geometry("700x400")
janela.title("NutriAPP")
janela.resizable(False, False)

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela // 2) - (700 // 2)
posicao_y = (altura_tela // 2) - (400 // 2)
janela.geometry(f"700x400+{posicao_x}+{posicao_y}")

app = AppController(janela)
app.iniciar()

janela.mainloop()
