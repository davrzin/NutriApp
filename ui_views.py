import customtkinter as ctk
from CTkListbox import CTkListbox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import RIGHT
from PIL import Image
from pathlib import Path


class BaseView:
    def __init__(self, janela):
        self.janela = janela

    def clear(self):
        for widget in self.janela.winfo_children():
            widget.destroy()


def _logo_path() -> Path | None:
    base_dir = Path(__file__).resolve().parent
    for nome in ("ico.ico", "log.png", "logo.png"):
        caminho = base_dir / nome
        if caminho.exists():
            return caminho
    return None


def filter_food_options(opcoes: list[str], texto: str) -> list[str]:
    texto = texto.lower().strip()
    if not texto:
        return opcoes
    return [item for item in opcoes if texto in item.lower()]


class LoginView(BaseView):
    def render(self, on_login, on_open_register):
        self.clear()
        self.janela.title("NutriAPP")

        logo = _logo_path()
        if logo:
            self._login_image = ctk.CTkImage(
                light_image=Image.open(logo),
                dark_image=Image.open(logo),
                size=(340, 400),
            )

            image_button = ctk.CTkButton(self.janela, text="", image=self._login_image, hover=False, fg_color="white")
            image_button.place(x=0, y=-10)
        else:
            ctk.CTkLabel(
                self.janela,
                text="NutriAPP",
                font=("arial bold", 42),
                text_color="white",
                width=350,
            ).place(x=0, y=160)

        frame = ctk.CTkFrame(self.janela, width=350, height=400)
        frame.pack(side=RIGHT)

        ctk.CTkLabel(frame, text="Sistema de Login", font=("arial bold", 30), width=300).place(x=25, y=5)
        ctk.CTkLabel(frame, text="Email:", font=("arial bold", 18), width=300).place(x=25, y=85)

        email_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Digite seu Email",
            font=("arial bold", 14),
            width=300,
            corner_radius=20,
        )
        email_entry.place(x=25, y=120)

        ctk.CTkLabel(frame, text="Senha:", font=("arial bold", 18), width=300).place(x=25, y=157)

        senha_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Digite sua Senha",
            font=("arial bold", 14),
            show="*",
            width=300,
            corner_radius=20,
        )
        senha_entry.place(x=25, y=190)

        ctk.CTkButton(
            frame,
            text="Login",
            width=250,
            command=lambda: on_login(email_entry.get(), senha_entry.get()),
            font=("arial bold", 15),
        ).place(x=50, y=275)

        ctk.CTkButton(
            frame,
            text="Cadastrar novo Usuário",
            width=250,
            command=on_open_register,
            font=("arial bold", 15),
        ).place(x=50, y=325)


class CadastroView(BaseView):
    def render(self, on_submit, on_back):
        self.clear()
        self.janela.title("Cadastro de Novo Usuário")

        ctk.CTkLabel(self.janela, text="Email:", width=240, font=("arial bold", 15)).place(x=50, y=10)
        email_entry = ctk.CTkEntry(self.janela, placeholder_text="Digite seu Email", width=240, font=("arial bold", 15), corner_radius=20)
        email_entry.place(x=50, y=40)

        ctk.CTkLabel(self.janela, text="Nome:", width=240, font=("arial bold", 15)).place(x=50, y=80)
        nome_entry = ctk.CTkEntry(self.janela, placeholder_text="Digite seu nome", width=240, font=("arial bold", 15), corner_radius=20)
        nome_entry.place(x=50, y=110)

        ctk.CTkLabel(self.janela, text="Idade:", width=240, font=("arial bold", 15)).place(x=50, y=150)
        idade_entry = ctk.CTkEntry(self.janela, placeholder_text="Digite sua Idade", width=240, font=("arial bold", 15), corner_radius=20)
        idade_entry.place(x=50, y=180)

        ctk.CTkLabel(self.janela, text="Altura:", width=240, font=("arial bold", 15)).place(x=50, y=220)
        altura_entry = ctk.CTkEntry(self.janela, placeholder_text="Digite sua Altura", width=240, font=("arial bold", 15), corner_radius=20)
        altura_entry.place(x=50, y=250)

        ctk.CTkLabel(self.janela, text="Senha:", width=240, font=("arial bold", 15)).place(x=400, y=10)
        senha_entry = ctk.CTkEntry(self.janela, placeholder_text="Digite sua Senha", show="*", width=240, font=("arial bold", 15), corner_radius=20)
        senha_entry.place(x=400, y=40)

        ctk.CTkLabel(self.janela, text="Sexo:", font=("arial bold", 15), width=240).place(x=400, y=80)
        sexo_var = ctk.StringVar(value="Selecione seu Sexo:")
        sexo_menu = ctk.CTkOptionMenu(
            self.janela,
            variable=sexo_var,
            values=["Masculino", "Feminino"],
            font=("arial bold", 15),
            width=240,
            dropdown_font=("arial bold", 15),
            state="readonly",
            corner_radius=20,
            fg_color="teal",
            button_color="teal",
        )
        sexo_menu.place(x=400, y=110)

        ctk.CTkLabel(self.janela, text="Peso:", width=240, font=("arial bold", 15)).place(x=400, y=150)
        peso_entry = ctk.CTkEntry(self.janela, placeholder_text="Digite seu Peso", width=240, font=("arial bold", 15), corner_radius=20)
        peso_entry.place(x=400, y=180)

        ctk.CTkLabel(self.janela, text="Objetivo:", font=("arial bold", 15), width=240).place(x=400, y=220)
        objetivo_var = ctk.StringVar(value="Selecione seu Objetivo:")
        objetivo_menu = ctk.CTkOptionMenu(
            self.janela,
            variable=objetivo_var,
            values=["Ganhar Peso", "Perder Peso", "Manter Peso"],
            font=("arial bold", 15),
            width=240,
            dropdown_font=("arial bold", 15),
            state="readonly",
            corner_radius=20,
            fg_color="teal",
            button_color="teal",
        )
        objetivo_menu.place(x=400, y=250)

        ctk.CTkLabel(self.janela, text="Nível de Atividade Fisica:", font=("arial bold", 15), width=240).place(x=220, y=290)
        nivel_var = ctk.StringVar(value="Selecione seu Nivel de Atividade:")
        nivel_menu = ctk.CTkOptionMenu(
            self.janela,
            variable=nivel_var,
            values=["Sedentário", "Moderada", "Intensa"],
            font=("arial bold", 15),
            width=266,
            dropdown_font=("arial bold", 15),
            state="readonly",
            corner_radius=20,
            fg_color="teal",
            button_color="teal",
        )
        nivel_menu.place(x=207, y=320)

        def submit():
            data = {
                "email": email_entry.get(),
                "senha": senha_entry.get(),
                "nome": nome_entry.get(),
                "sexo": sexo_menu.get(),
                "idade": idade_entry.get(),
                "peso": peso_entry.get(),
                "altura": altura_entry.get(),
                "objetivo": objetivo_menu.get(),
                "nivel_fisico": nivel_menu.get(),
            }
            on_submit(data)

        ctk.CTkButton(self.janela, text="Cadastrar", width=240, command=submit, font=("arial bold", 15)).place(x=220, y=365)
        ctk.CTkButton(self.janela, text="Voltar", width=25, command=on_back, font=("arial bold", 15)).place(x=0, y=0)


class DashboardView(BaseView):
    def render(self, valores_percentuais, on_open_foods, on_logout, on_meta_alert):
        self.clear()
        self.janela.title("Informações Nutricionais")

        figura = Figure(figsize=(6.8, 3.3), tight_layout=True)
        eixo = figura.add_subplot(111)
        grafico = FigureCanvasTkAgg(figura, master=self.janela)
        grafico.get_tk_widget().grid(row=0, column=2, rowspan=7, padx=10, pady=10)

        for spine in eixo.spines.values():
            spine.set_edgecolor("white")
        for tick_label in eixo.get_yticklabels():
            tick_label.set_color("white")

        categorias = ["Calorias", "Proteínas", "Carboidratos", "Lipídios", "Fíbras", "Água"]
        barras = eixo.bar(categorias, valores_percentuais, color=["red", "green", "blue", "orange", "purple", "cyan"])
        _ = barras

        eixo.set_facecolor("#2C2C2C")
        figura.set_facecolor("#2C2C2C")
        eixo.set_ylim(0, 100)
        eixo.set_yticks(range(0, 101, 20))
        eixo.set_yticklabels([f"{i}%" for i in range(0, 101, 20)])
        eixo.set_xticks(range(len(categorias)))

        cores_categorias = ["red", "green", "blue", "orange", "purple", "cyan"]
        for tick, cor in zip(eixo.get_xticklabels(), cores_categorias):
            tick.set_color(cor)

        eixo.set_xticklabels(categorias, rotation=45, ha="right")

        for categoria, valor in zip(categorias, valores_percentuais):
            if valor == 100:
                on_meta_alert("Aviso", f"Você bateu a Meta Diária de {categoria}")
            elif valor > 100:
                on_meta_alert("Aviso", f"Você ultrapassou a Meta Diária de {categoria}")

        ctk.CTkButton(
            self.janela,
            text="LISTA DE ALIMENTOS",
            width=300,
            command=on_open_foods,
            font=("arial bold", 15),
        ).place(x=375, y=350)

        ctk.CTkButton(
            self.janela,
            text="LOGOUT",
            width=300,
            command=on_logout,
            font=("arial bold", 15),
        ).place(x=25, y=350)


class FoodsView(BaseView):
    def render(self, meal_texts, all_options, on_select_option, on_back, on_add_water):
        self.clear()

        tabview = ctk.CTkTabview(
            self.janela,
            width=550,
            height=300,
            corner_radius=35,
            border_width=3,
            segmented_button_unselected_hover_color="teal",
        )
        tabview.pack(pady=22)

        opcoes_tabs = ["Café da Manhã", "Almoço", "Lanche", "Janta"]
        for opcao in opcoes_tabs:
            tabview.add(opcao)
            tabview.tab(opcao).grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(tabview.tab("Café da Manhã"), text=meal_texts["Café da manhã"], font=("arial bold", 16)).pack()
        ctk.CTkLabel(tabview.tab("Almoço"), text=meal_texts["Almoço"], font=("arial bold", 16)).pack()
        ctk.CTkLabel(tabview.tab("Lanche"), text=meal_texts["Lanche"], font=("arial bold", 16)).pack()
        ctk.CTkLabel(tabview.tab("Janta"), text=meal_texts["Janta"], font=("arial bold", 16)).pack()

        ctk.CTkButton(self.janela, text="Voltar", width=25, command=on_back, font=("arial bold", 15)).place(x=0, y=0)
        ctk.CTkButton(self.janela, text="Atualiziar Água", width=240, command=on_add_water, font=("arial bold", 15)).place(x=221, y=340)

        entrada = ctk.CTkEntry(self.janela, placeholder_text="Digite um Alimento", width=240, font=("arial bold", 15), corner_radius=20)
        entrada.place(x=50, y=0)

        opcoes = sorted(all_options)

        def criar_listbox(itens):
            lb = CTkListbox(self.janela, command=on_select_option, width=213, font=("arial bold", 15))
            for item in itens:
                lb.insert("end", item)
            return lb

        listbox = criar_listbox(opcoes)

        def atualizar_listbox(opcoes_filtradas):
            nonlocal listbox
            if listbox.winfo_exists():
                listbox.destroy()

            itens = opcoes_filtradas if opcoes_filtradas else ["Nenhum resultado encontrado"]
            listbox = criar_listbox(itens)
            listbox.place(x=50, y=40)

        def filtrar(_event):
            filtradas = filter_food_options(opcoes, entrada.get())
            atualizar_listbox(filtradas)

        def ocultar(_event):
            if listbox.winfo_exists():
                listbox.place_forget()

        entrada.bind("<KeyRelease>", filtrar)
        self.janela.bind("<Button-1>", ocultar)
