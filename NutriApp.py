import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
from CTkListbox import *
from tkinter import *
from PIL import Image
import re

# FUÇÕES EM PYTHON 

def escrever_macronutrientes(email, sexo, idade, peso, altura, objetivo, nivelfisico): #FUNÇÃO PARA ESCREVER A QUANTIDADE DE MACRONUTRIENTES, CALORIAS E DE ÁGUA NO ARQUIVO TXT
    def calcular_tmb():
        if sexo == "Masculino":
            return 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
        else:
            return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

    def calorias_ajustadas():

        tmb = calcular_tmb()

        if nivelfisico == "Sedentário":
            return tmb * 1.2
        elif nivelfisico == "Moderada":
            return tmb * 1.55
        else:
            return tmb * 1.725

    def calorias_objetivo():

        caloriasAjustadas = calorias_ajustadas()

        if objetivo == "Perder Peso":
            return caloriasAjustadas * 0.85
        elif objetivo == "Manter Peso":
            return caloriasAjustadas
        else:
            return caloriasAjustadas * 1.15

    def macronutrientes():

        meta_calorica = calorias_objetivo()

        calorias_carboidrato = 4
        calorias_lipideos = 9

        if nivelfisico == "Sedentário":
            gramas_proteinas = peso * 0.8
            gramas_carboidrato = (45 / 100) * meta_calorica / calorias_carboidrato
            gramas_lipideos = (25 / 100) * meta_calorica / calorias_lipideos
            gramas_fibras = 25

        elif nivelfisico == "Moderada":
            gramas_proteinas = peso * 1.5
            gramas_carboidrato = (50 / 100) * meta_calorica / calorias_carboidrato
            gramas_lipideos = (30 / 100) * meta_calorica / calorias_lipideos
            gramas_fibras = 30

        else:
            gramas_proteinas = peso * 2
            gramas_carboidrato = (55 / 100) * meta_calorica / calorias_carboidrato
            gramas_lipideos = (35 / 100) * meta_calorica / calorias_lipideos
            gramas_fibras = 35

        ml_agua = peso * 35

        return meta_calorica, gramas_proteinas, gramas_carboidrato, gramas_lipideos, gramas_fibras, ml_agua

    meta_calorica, gramas_proteinas, gramas_carboidrato, gramas_lipideos, gramas_fibras, ml_agua = macronutrientes()

    meta_calorica_diaria = proteinas_diarias = carboidratos_diarios = lipideos_diarios = fibras_diarias = agua_diaria = 0

    return (
        f"Meta Calorica {email}: {meta_calorica:.0f}\nProteinas {email}: {gramas_proteinas:.0f}\nCarboidrato {email}: {gramas_carboidrato:.0f}\nLipideos {email}: {gramas_lipideos:.0f}"
        f"\nFibras {email}: {gramas_fibras:.0f}\nAgua {email}: {ml_agua}\nMeta Calorica Diaria {email}: {meta_calorica_diaria}\nProteinas Diarias {email}: {proteinas_diarias}"
        f"\nCarboidrato Diarios {email}: {carboidratos_diarios}\nLipideos Diarios {email}: {lipideos_diarios}\nFibras Diarias {email}: {fibras_diarias}\nAgua Diaria {email}: {agua_diaria}")

def carregar_dados_usuarios(): #FUNÇÃO PARA CARREGAR OS DADOS DE TODOS OS USUÁRIOS EM FORMA DE DICIONÁRIO, CUJO A CHAVE É O EMAIL DO USUÁRIO
    dicionario_todos_usuarios = {}

    try:
        with open("dados.txt", "r") as arquivo:
            leitura_dados_usuario = arquivo.read()
            separação_cada_usuário = leitura_dados_usuario.split('\n\n')

            for usuario in separação_cada_usuário:
                dados_de_cada_usuário = {}
                separação_de_linhas_de_cada_usuário = usuario.split('\n')

                for linha in separação_de_linhas_de_cada_usuário:
                    if ':' in linha:
                        chave, valor = linha.split(': ')
                        dados_de_cada_usuário[chave] = valor

                if "Email" in dados_de_cada_usuário:
                    email = dados_de_cada_usuário["Email"]
                    dicionario_todos_usuarios[email] = dados_de_cada_usuário

    except FileNotFoundError:
        pass

    return dicionario_todos_usuarios

def cadastro(): #FUNÇÃO QUE CADASTRA O USUÁRIO NO ARQUIVO TXT
    dicionario_todos_usuarios = carregar_dados_usuarios()

    email = email_cadastro.get()
    if not (email):
        exibir_mensagem("Erro", "O campo 'Email' deve ser preenchido")

    else:
        if verifica_email(email) == True:

            if email in dicionario_todos_usuarios:
                exibir_mensagem("Erro", "Email já cadastrado.")

            else:
                senha = senha_cadastro.get()
                if not (senha):
                    exibir_mensagem("Erro", "O campo 'Senha' deve ser preenchido")

                else:
                    if verifica_senha(senha) == True:
                        nome = nome_cadastro.get()
                        if not (nome):
                            exibir_mensagem("Erro", "O campo 'Nome' deve ser preenchido")

                        else:
                            sexo = sexo_cadastro.get()
                            if not (sexo):
                                exibir_mensagem("Erro", "O campo 'Sexo' deve ser preenchido")

                            else:
                                idade = idade_cadastro.get()
                                if not (idade):
                                    exibir_mensagem("Erro", "O campo 'Idade' deve ser preenchido")

                                else:
                                    if verificar_idade(idade) == True:
                                        peso = peso_cadastro.get()
                                        if not (peso):
                                            exibir_mensagem("Erro", "O campo 'Peso' deve ser preenchido")

                                        else:
                                            if verificar_peso(peso) == True:
                                                altura = altura_cadastro.get()
                                                if not (altura):
                                                    exibir_mensagem("Erro", "O campo 'Altura' deve ser preenchido")

                                                else:
                                                    if verificar_altura(altura) == True:
                                                        objetivo = objetivo_cadastro.get()
                                                        if not (objetivo):
                                                            exibir_mensagem("Erro",
                                                                            "O campo 'Objetivo' deve ser preenchido")

                                                        else:
                                                            nivelfisico = nivelfisico_cadastro.get()
                                                            if not (nivelfisico):
                                                                exibir_mensagem("Erro",
                                                                                "O campo 'Nivel de Atividade Física' deve ser preenchido")

                                                            else:
                                                                idadeINT = int(idade_cadastro.get())
                                                                pesoFLOAT = float(peso_cadastro.get())
                                                                alturaFLOAT = float(altura_cadastro.get())

                                                                with open("dados.txt", "a") as arquivo:
                                                                    macronutrientes = escrever_macronutrientes(email,
                                                                                                               sexo,
                                                                                                               idadeINT,
                                                                                                               pesoFLOAT,
                                                                                                               alturaFLOAT,
                                                                                                               objetivo,
                                                                                                               nivelfisico)
                                                                    usuario = f"Email: {email}\nSenha: {senha}\nNome: {nome}\nSexo: {sexo}\nIdade: {idadeINT}\nPeso: {pesoFLOAT}\nAltura: {alturaFLOAT}\nObjetivo: {objetivo}\nNivel Fisico: {nivelfisico}\n{macronutrientes}\n\n"
                                                                    arquivo.write(usuario)

                                                                exibir_mensagem_abrir_login("Sucesso",
                                                                                            "Cadastro Concluido")

                                                    else:
                                                        exibir_mensagem("Erro",
                                                                        "Por favor, insira uma altura válida maior que 100 cm e menor/igual que 251/igual cm\n(número positivo em centimetros)\nEx: 180")
                                            else:
                                                exibir_mensagem("Erro",
                                                                "Por favor, insira um peso válido (número positivo em Kg).")
                                                                        
                                    else:
                                        exibir_mensagem("Erro",
                                                        "Por favor, insira uma idade válida maior que 12 anos(número inteiro positivo).")
                    
                    else:
                        exibir_mensagem("Erro",
                                        "A senha é inválida. Tente novamente.\nSua senha deve conter: Pelo menos 8 digitos, 1 letra maiúscula, 1 letra minúscula e 1 número\nEx: Aa123456")
        
        else:
            exibir_mensagem("Erro", "O email é Inválido.\nSeu email deve conter: @, .br ou .com\nEx: davi@gmail.com")

def fazer_login(): #FUNÇÃO QUE FAZ LOGIN NO APLICATIVO
    global dados_do_usuario_do_email_digitado

    dicionario_todos_usuarios = carregar_dados_usuarios()  # Chama a função para carregar o dicionário dos usuários que ja fizeram cadastro e atribui o dicionário com o nome dicionario_todos_usuarios

    email_digitado = email_login.get()
    senha_digitada = senha_login.get()

    if not (email_digitado and senha_digitada):
        exibir_mensagem("Erro", "Todos os campos são obrigatórios.\nPor favor, preencha todos os campos.")
        return

    else:

        if email_digitado in dicionario_todos_usuarios:  # verifica se já existe um email igual cadastrado

            dados_do_usuario_do_email_digitado = dicionario_todos_usuarios[email_digitado]

            if dados_do_usuario_do_email_digitado["Senha"] == senha_digitada:
                tela_dados()

            else:
                exibir_mensagem("Erro", "Senha incorreta.")

        else:   
            exibir_mensagem("Erro", "Email não encontrado.")

def atualizar_dados_agua(): #FUNÇÃO QUE ATUALIZA A QUANTIDADE DE AGUA INGERIDA NO ARQUIVO TXT
    chave = False
    ultima_alteracao = False
    email_usuario_logado = dados_do_usuario_do_email_digitado["Email"]
    agua_alteraçoes = 250

    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            if ":" in linha and (not (chave and ultima_alteracao)):
                chave, valor = linha.strip().split(": ")
                if chave == "Email" and valor == email_usuario_logado:
                    chave = True
                if chave == f"Agua Diaria {email_usuario_logado}":
                    linhas[i] = f"{chave}: {int(valor) + agua_alteraçoes}\n"
                    ultima_alteracao = True

    with open("dados.txt", "w") as arquivo:
        arquivo.writelines(linhas)
    exibir_mensagem("Sucesso", "250 ml's de Água Adicionados!(1 copo)")

def atualizar_dados_macros(calorias_alteraçoes, proteinas_alteraçoes, carboidratos_alteraçoes, lipideos_alteraçoes, #FUNÇÃO QUE ATUALIZA A QUANTIDADE DE MACRO E CALORIAS INGERIDAS NO ARQUIVO TXT
                           fibras_alteraçoes):
    chave = False
    ultima_alteracao = False
    email_usuario_logado = dados_do_usuario_do_email_digitado["Email"]

    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            if ":" in linha and (not (chave and ultima_alteracao)):
                chave, valor = linha.strip().split(": ")
                if chave == "Email" and valor == email_usuario_logado:
                    chave = True
                if chave == f"Meta Calorica Diaria {email_usuario_logado}":
                    linhas[i] = f"{chave}: {float(valor) + calorias_alteraçoes}\n"
                elif chave == f"Proteinas Diarias {email_usuario_logado}":
                    linhas[i] = f"{chave}: {float(valor) + proteinas_alteraçoes}\n"
                elif chave == f"Carboidrato Diarios {email_usuario_logado}":
                    linhas[i] = f"{chave}: {float(valor) + carboidratos_alteraçoes}\n"
                elif chave == f"Lipideos Diarios {email_usuario_logado}":
                    linhas[i] = f"{chave}: {float(valor) + lipideos_alteraçoes}\n"
                elif chave == f"Fibras Diarias {email_usuario_logado}":
                    linhas[i] = f"{chave}: {float(valor) + fibras_alteraçoes}\n"
                    ultima_alteracao = True

    # Escreve as modificações de volta no arquivo
    with open("dados.txt", "w") as arquivo:
        arquivo.writelines(linhas)
    exibir_mensagem("Sucesso", "Calorias e Macro-Nutrientes Atualizados!")

def verifica_email(email_input): #FUNÇÃO QUE VERIFICA SE O EMAIL FOI DIGITADO DA FORMA CORRETA NO CADASTRO
    # Define o padrão do email
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Verifica se o email corresponde ao padrão criado
    if re.match(padrao_email, email_input):
        return True
    else:
        return False

def verifica_senha(senha_input): #FUNÇÃO QUE VERIFICA SE A SENHA FOI DIGITADA DA FORMA CORRETA NO CADASTRO
    # Padrão senha: pelo menos 8 caracteres, pelo menos uma letra maiúscula, uma letra minúscula e um número.
    padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'

    # Verifica se a senha corresponde ao padrão
    if re.match(padrao_senha, senha_input):
        return True
    else:
        return False

def verificar_idade(input_idade): #FUNÇÃO QUE VERIFICA SE A IDADE FOI DIGITADA DA FORMA CORRETA NO CADASTRO
    try:
        # Tenta converter a entrada para um número inteiro
        idade = int(input_idade)

        if idade >= 12:
            return True
        else:
            return False
    except ValueError:
        return False

def verificar_altura(input_altura): #FUNÇÃO QUE VERIFICA SE A ALTURA FOI DIGITADO DA FORMA CORRETA NO CADASTRO

    try:
        if 251 >= int(input_altura) >= 100:
            return True
        else:
            return False
        
    except ValueError:
        return False

def verificar_peso(input_peso): #FUNÇÃO QUE VERIFICA SE O PESO FOI DIGITADO DA FORMA CORRETA NO CADASTRO
    try:
        # Tenta converter a entrada para um número decimal
        peso = float(input_peso)

        if peso > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def gera_cardapio(usuario, dicionarioAlimentos): #FUNÇÃO QUE RETORNA O CAFÉ, ALMOÇO, LANCHE E JANTA PARA CADA USUÁRIO
    metasUsuario = {}

    metasUsuario['Meta Calorica'] = usuario['Meta Calorica ' + usuario['Email']]
    metasUsuario['Proteinas'] = usuario['Proteinas ' + usuario['Email']]
    metasUsuario['Carboidrato'] = usuario['Proteinas ' + usuario['Email']]
    metasUsuario['Lipideos'] = usuario['Lipideos ' + usuario['Email']]
    metasUsuario['Fibras'] = usuario['Fibras ' + usuario['Email']]

    cardapio = {}
    dicionarioCafe = {}
    dicionarioAlmoco = {}
    dicionarioLanche = {}
    dicionarioJanta = {}

    def somaMacroNutrientes(dicionarioRefeicao):
        totalMacronutrientes = {"calorias": 0, "carboidratos": 0, "proteinas": 0, "gorduras": 0,
                                "fibras": 0}
        for alimento in dicionarioRefeicao:
            if str(alimento) != "Total de Macronutrientes":
                for macronutriente in totalMacronutrientes:
                    totalMacronutrientes[macronutriente] += dicionarioRefeicao[alimento][macronutriente]
        return totalMacronutrientes

    metaMacronutrientesCafe = {}
    metaMacronutrientesAlmoco = {}
    metaMacronutrientesLanche = {}
    metaMacronutrientesJanta = {}

    for metaMacronutrienteUsuario in metasUsuario.keys():
        metaMacronutrientesCafe[metaMacronutrienteUsuario] = float(metasUsuario[metaMacronutrienteUsuario]) * 0.1
        metaMacronutrientesAlmoco[metaMacronutrienteUsuario] = float(metasUsuario[metaMacronutrienteUsuario]) * 0.5
        metaMacronutrientesJanta[metaMacronutrienteUsuario] = float(metasUsuario[metaMacronutrienteUsuario]) * 0.3
        metaMacronutrientesLanche[metaMacronutrienteUsuario] = float(metasUsuario[metaMacronutrienteUsuario]) * 0.1

    def aumentaQuantidadeAlimento(alimento, fator_aumento):
        alimento_aumentado = alimento.copy()

        if 'porcao' in alimento_aumentado:
            # Extrair a quantidade e unidade da porção
            listaString = alimento_aumentado['porcao'].split()

            # unidade
            unidade = ""
            for i in range(1, len(listaString)):
                unidade += listaString[i] + " "

            # Converter a quantidade para um número
            quantidade = float(listaString[0])

            # Aumentar a quantidade
            quantidade_aumentada = quantidade * fator_aumento

            # Atualizar a chave 'porcao' no dicionário
            alimento_aumentado['porcao'] = f"{quantidade_aumentada} {unidade}"

        for chave, valor in alimento_aumentado.items():
            if chave != 'porcao':
                alimento_aumentado[chave] *= fator_aumento

        return alimento_aumentado

    def aumentaQuantidades(alimento, macronutriente, metaMacronutriente, aproxExcesso):
        if alimento[macronutriente] < metaMacronutriente:
            fator_aumento = (metaMacronutriente // alimento[macronutriente])
            if fator_aumento > 6:
                fator_aumento = 5
            if aproxExcesso:
                fator_aumento += 1
            return aumentaQuantidadeAlimento(alimento, fator_aumento)
        else:
            return alimento

    # cria cafe da manha e adapta cafe da manha

    dicionarioCafe["Ovo Frito"] = dicionarioAlimentos["Ovo Frito"]
    dicionarioCafe["Pão Francês"] = dicionarioAlimentos["Pão Francês"]
    dicionarioCafe["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioCafe)

    if dicionarioCafe["Total de Macronutrientes"]["proteinas"] <= metaMacronutrientesCafe["Proteinas"] * 0.8:
        dicionarioCafe["Ovo Frito"] = aumentaQuantidades(dicionarioCafe["Ovo Frito"], "proteinas",
                                                         metaMacronutrientesCafe["Proteinas"], False)

    dicionarioCafe["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioCafe)

    if dicionarioCafe["Total de Macronutrientes"]["carboidratos"] <= metaMacronutrientesCafe['Carboidrato'] * 0.8:
        dicionarioCafe["Pão Francês"] = aumentaQuantidades(dicionarioCafe["Pão Francês"], "carboidratos",
                                                           metaMacronutrientesCafe['Carboidrato'], False)
    dicionarioCafe["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioCafe)

    # cria almoco e adapta almoco
    dicionarioAlmoco["Feijão"] = dicionarioAlimentos["Feijão"]
    dicionarioAlmoco["Arroz"] = dicionarioAlimentos["Arroz"]
    dicionarioAlmoco["Frango Grelhado"] = dicionarioAlimentos["Frango Grelhado"]
    dicionarioAlmoco["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioAlmoco)

    if dicionarioAlmoco["Total de Macronutrientes"]["proteinas"] <= metaMacronutrientesAlmoco["Proteinas"]:
        dicionarioAlmoco["Frango Grelhado"] = aumentaQuantidades(dicionarioAlmoco["Frango Grelhado"], "proteinas",
                                                                 metaMacronutrientesAlmoco["Proteinas"], False)
    dicionarioAlmoco["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioAlmoco)

    if dicionarioAlmoco["Total de Macronutrientes"]["proteinas"] <= metaMacronutrientesAlmoco["Proteinas"]:
        dicionarioAlmoco["Feijão"] = aumentaQuantidadeAlimento(dicionarioAlmoco["Feijão"], 2)
    if dicionarioAlmoco["Total de Macronutrientes"]["proteinas"] <= metaMacronutrientesAlmoco["Proteinas"]:
        dicionarioAlmoco["Feijão"] = aumentaQuantidadeAlimento(dicionarioAlimentos["Feijão"], 3)

    dicionarioAlmoco["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioAlmoco)

    if dicionarioAlmoco["Total de Macronutrientes"]["carboidratos"] <= metaMacronutrientesAlmoco['Carboidrato'] * 0.9:
        dicionarioAlmoco["Arroz"] = aumentaQuantidades(dicionarioAlmoco["Arroz"], "carboidratos",
                                                       metaMacronutrientesAlmoco['Carboidrato'], False)
    dicionarioAlmoco["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioAlmoco)

    # cria janta e adapta janta
    dicionarioJanta["Carne Moída"] = dicionarioAlimentos["Carne Moída"]
    dicionarioJanta["Batata Doce"] = dicionarioAlimentos["Batata Doce"]
    dicionarioJanta["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioJanta)

    if dicionarioJanta["Total de Macronutrientes"]["proteinas"] <= metaMacronutrientesJanta["Proteinas"]:
        dicionarioJanta["Carne Moída"] = aumentaQuantidades(dicionarioJanta["Carne Moída"], "proteinas",
                                                            metaMacronutrientesJanta["Proteinas"], False)
    dicionarioJanta["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioJanta)

    if dicionarioJanta["Total de Macronutrientes"]["carboidratos"] <= metaMacronutrientesJanta['Carboidrato']:
        dicionarioJanta["Batata Doce"] = aumentaQuantidades(dicionarioJanta["Batata Doce"], "carboidratos",
                                                            metaMacronutrientesJanta['Carboidrato'], False)
    dicionarioJanta["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioJanta)

    # cria Lanche
    dicionarioLanche["Biscoito Maisena"] = dicionarioAlimentos["Biscoito Maisena"]
    dicionarioLanche["Banana"] = dicionarioAlimentos["Banana"]
    dicionarioLanche["Castanha-do-Pará"] = dicionarioAlimentos["Castanha-do-Pará"]
    dicionarioLanche["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioLanche)

    # cria dicionario de cardapio

    cardapio["Café da manhã"] = dicionarioCafe
    cardapio["Almoço"] = dicionarioAlmoco
    cardapio["Lanche"] = dicionarioLanche
    cardapio["Janta"] = dicionarioJanta

    def somaMacroNutrientesDois(cardapio):
        totalPlanjedo = {"calorias": 0, "carboidratos": 0, "proteinas": 0, "gorduras": 0,
                         "fibras": 0}

        for refeicao in cardapio.keys():
            macroRefeicao = cardapio[refeicao]["Total de Macronutrientes"]
            for macronutriente in totalPlanjedo.keys():
                totalPlanjedo[macronutriente] += macroRefeicao[macronutriente]

        return totalPlanjedo

    # adpta lanche

    metaLipideoUsuario = float(metasUsuario['Lipideos'])
    somaLipideoTotalCardapio = somaMacroNutrientesDois(cardapio)['gorduras']

    if metaLipideoUsuario > somaLipideoTotalCardapio:
        dicionarioLanche["Castanha-do-Pará"] = aumentaQuantidades(dicionarioLanche["Castanha-do-Pará"], "gorduras",
                                                                  metaLipideoUsuario - somaLipideoTotalCardapio, False)
    dicionarioLanche["Total de Macronutrientes"] = somaMacroNutrientes(dicionarioLanche)

    cardapio["Lanche"] = dicionarioLanche

    return cardapio

def função_retorna_cardapio(): #FUNÇÃO QUE RETORNA UM DICIONARIO DE ALIMENTOS PARA O USUÁRIO
    dicionarioAlimentos = {
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
                        "gorduras": 0.2,
                        "fibras": 6.3},
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
                      "gorduras": 7 / 2,
                      "fibras": 0},
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
                             "gorduras": 6 / 4, "fibras": 0 / 4}}
    return dicionarioAlimentos

def chamarMacros_telaDados(): #FUNÇÃO QUE MOSTRA OS MACROS, CALORIAS E ÁGUA IGERIDOS, QUE SE ENCONTRA NO ARQUIVO TXT, NA TELA DO USUÁRIO
    email_usuario_logado = dados_do_usuario_do_email_digitado["Email"]
    chave = False
    ultima_alteracao = False

    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            if ":" in linha and (not (chave and ultima_alteracao)):
                chave, valor = linha.strip().split(": ")
                if chave == "Email" and valor == email_usuario_logado:
                    chave = True
                if chave == f"Meta Calorica {email_usuario_logado}":
                    caloriasMeta = valor
                elif chave == f"Proteinas {email_usuario_logado}":
                    proteinasMeta = valor
                elif chave == f"Carboidrato {email_usuario_logado}":
                    carboidratosMeta = valor
                elif chave == f"Lipideos {email_usuario_logado}":
                    lipideosMeta = valor
                elif chave == f"Fibras {email_usuario_logado}":
                    fibrasMeta = valor
                elif chave == f"Agua {email_usuario_logado}":
                    aguaMeta = valor
                elif chave == f"Meta Calorica Diaria {email_usuario_logado}":
                    calorias = valor
                elif chave == f"Proteinas Diarias {email_usuario_logado}":
                    proteinas = valor
                elif chave == f"Carboidrato Diarios {email_usuario_logado}":
                    carboidratos = valor
                elif chave == f"Lipideos Diarios {email_usuario_logado}":
                    lipideos = valor
                elif chave == f"Fibras Diarias {email_usuario_logado}":
                    fibras = valor
                elif chave == f"Agua Diaria {email_usuario_logado}":
                    agua = valor
                    ultima_alteracao = True

    dicAlimentos = função_retorna_cardapio()
    cardapioRefeicao = gera_cardapio(dados_do_usuario_do_email_digitado, dicAlimentos)

    caloriasMeta, proteinasMeta, carboidratosMeta, lipideosMeta, fibrasMeta = 0, 0, 0, 0, 0

    for refeicao in cardapioRefeicao.keys():
        caloriasMeta += cardapioRefeicao[refeicao]["Total de Macronutrientes"]["calorias"]
        proteinasMeta += cardapioRefeicao[refeicao]["Total de Macronutrientes"]["proteinas"]
        carboidratosMeta += cardapioRefeicao[refeicao]["Total de Macronutrientes"]["carboidratos"]
        lipideosMeta += cardapioRefeicao[refeicao]["Total de Macronutrientes"]["gorduras"]
        fibrasMeta += cardapioRefeicao[refeicao]["Total de Macronutrientes"]["fibras"]

    calorias1 = float(calorias) / float(caloriasMeta) * 100
    proteinas1 = float(proteinas) / float(proteinasMeta) * 100
    carboidratos1 = float(carboidratos) / float(carboidratosMeta) * 100
    lipideos1 = float(lipideos) / float(lipideosMeta) * 100
    fibras1 = float(fibras) / float(fibrasMeta) * 100
    agua1 = float(agua) / float(aguaMeta) * 100

    return calorias1, proteinas1, carboidratos1, lipideos1, fibras1, agua1

# FUNÇÕES EM CUSTOMTKINTER

def barra_pesquisa(): #FUNÇÃO QUE CRIA A BARRA DE PESQUISA DOS ALIMENTOS NA TELA
    def mostrar_valor(opcao_selecionada):

        dados_todos_usuarios = carregar_dados_usuarios()

        email = dados_do_usuario_do_email_digitado["Email"]

        usuario_logado = dados_todos_usuarios[email]

        if opcao_selecionada != "Nenhum resultado encontrado":
            cardapio = função_retorna_cardapio()

            if opcao_selecionada in cardapio.keys():
                for alimento in cardapio.keys():
                    if alimento == opcao_selecionada:
                        macros_comida_selecionada = (cardapio[alimento])

                macros_comida_selecionada.pop('porcao', None)

            else:
                refeição = gera_cardapio(usuario_logado, cardapio)
                lista = refeição[opcao_selecionada]

                macros_comida_selecionada = lista["Total de Macronutrientes"]

            for categoria, macro in macros_comida_selecionada.items():
                if categoria == f'calorias':
                    calorias_alteraçoes = macro
                elif categoria == f'carboidratos':
                    carboidratos_alteraçoes = macro
                elif categoria == f'proteinas':
                    proteinas_alteraçoes = macro
                elif categoria == f'gorduras':
                    lipideos_alteraçoes = macro
                elif categoria == f'fibras':
                    fibras_alteraçoes = macro

            atualizar_dados_macros(calorias_alteraçoes, proteinas_alteraçoes, carboidratos_alteraçoes,
                                   lipideos_alteraçoes, fibras_alteraçoes)

    def mostrar_todas_opcoes():
        atualizar_listbox(todas_opcoes)

    def filtrar_listbox(event):

        texto_pesquisa = entrada.get().lower()
        if texto_pesquisa:
            opcoes_filtradas = [item for item in todas_opcoes if item.lower().startswith(texto_pesquisa)]
            atualizar_listbox(opcoes_filtradas)
            lista.place(x=50, y=40)  # Torna a listbox visível
        else:
            mostrar_todas_opcoes()
            lista.place(x=50, y=40)  # Torna a listbox visível

    def atualizar_listbox(opcoes):
        lista.delete(0, "end")
        if opcoes:
            for opcao in opcoes:
                lista.insert("end", opcao)
        else:
            lista.insert("end", "Nenhum resultado encontrado")

    def ocultar_listbox(event):
        if lista.winfo_exists():  # Verifica se o widget ainda existe antes de tentar ocultá-lo
            lista.place_forget()

    def chamar_barra_pesquisa_lista():
        global lista, entrada, todas_opcoes

        entrada = ctk.CTkEntry(janela, placeholder_text="Digite um Alimento", width=240, font=("arial bold", 15),
                               corner_radius=20)
        entrada.place(x=50, y=0)
        entrada.bind("<KeyRelease>", filtrar_listbox)

        lista = CTkListbox(janela, command=mostrar_valor, width=213, font=("arial bold", 15))

        dados_todos_usuarios = carregar_dados_usuarios()
        email = dados_do_usuario_do_email_digitado["Email"]
        usuario_logado = dados_todos_usuarios[email]

        cardapio = função_retorna_cardapio()
        reifeiçao = gera_cardapio(usuario_logado, cardapio)

        todas_opcoes_refeiçoes = list(reifeiçao.keys())

        todas_opcoes = list(cardapio.keys())

        for i in range(len(todas_opcoes_refeiçoes)):
            todas_opcoes.append(todas_opcoes_refeiçoes[i])

        todas_opcoes.sort()

        for opcao in todas_opcoes:
            lista.insert("end", opcao)

        # Adicione o evento para ocultar a lista ao clicar fora dela
        janela.bind("<Button-1>", ocultar_listbox)

    chamar_barra_pesquisa_lista()

def exibir_mensagem_abrir_login(titulo, conteudo): #FUNÇÃO QUE CRIA UMA MENSAGEM NA TELA DE CADASTRO E QUANDO O USUÁRIO CLICAR EM "OK" ELE SERÁ REDIRECIONADO PARA A TELA DE LOGIN
    messagebox.showinfo(titulo, conteudo)
    abrir_tela_login()

def exibir_mensagem(titulo, conteudo): #FUNÇÃO PARA EXIBIR MENSAGENS DE ALERTA NA TELA
    messagebox.showinfo(titulo, conteudo)

def abrir_tela_cadastro(): #FUNÇÃO QUE CRIA A TELA DE CADASTRO DO APP
    global email_cadastro, senha_cadastro, nome_cadastro, sexo_cadastro, idade_cadastro, peso_cadastro, altura_cadastro, objetivo_cadastro, nivelfisico_cadastro

    for widget in janela.winfo_children():
        widget.destroy()

    # lado esquerdo
    janela.title("Cadastro de Novo Usuário")

    titulo_email = ctk.CTkLabel(janela, text="Email:", width=240, font=("arial bold", 15))
    titulo_email.place(x=50, y=10)

    email_cadastro = ctk.CTkEntry(janela, placeholder_text="Digite seu Email", width=240, font=("arial bold", 15),
                                  corner_radius=20)
    email_cadastro.place(x=50, y=40)

    titulo_nome = ctk.CTkLabel(janela, text="Nome:", width=240, font=("arial bold", 15))
    titulo_nome.place(x=50, y=80)

    nome_cadastro = ctk.CTkEntry(janela, placeholder_text="Digite seu nome", width=240, font=("arial bold", 15),
                                 corner_radius=20)
    nome_cadastro.place(x=50, y=110)

    titulo_idade = ctk.CTkLabel(janela, text="Idade:", width=240, font=("arial bold", 15))
    titulo_idade.place(x=50, y=150)

    idade_cadastro = ctk.CTkEntry(janela, placeholder_text="Digite sua Idade", width=240, font=("arial bold", 15),
                                  corner_radius=20)
    idade_cadastro.place(x=50, y=180)

    titulo_altura = ctk.CTkLabel(janela, text="Altura:", width=240, font=("arial bold", 15))
    titulo_altura.place(x=50, y=220)

    altura_cadastro = ctk.CTkEntry(janela, placeholder_text="Digite sua Altura", width=240, font=("arial bold", 15),
                                   corner_radius=20)
    altura_cadastro.place(x=50, y=250)

    # lado direito

    titulo_senha = ctk.CTkLabel(janela, text="Senha:", width=240, font=("arial bold", 15))
    titulo_senha.place(x=400, y=10)

    senha_cadastro = ctk.CTkEntry(janela, placeholder_text="Digite sua Senha", show="*", width=240,
                                  font=("arial bold", 15), corner_radius=20)
    senha_cadastro.place(x=400, y=40)

    titulo_sexo = ctk.CTkLabel(janela, text="Sexo:", font=("arial bold", 15), width=240)
    titulo_sexo.place(x=400, y=80)

    mes_var = ctk.StringVar(value="Selecione seu Sexo:")

    opcoes_sexo = ["Masculino", "Feminino"]

    sexo_cadastro = ctk.CTkOptionMenu(janela, variable=mes_var, values=opcoes_sexo, font=("arial bold", 15), width=240,
                                      dropdown_font=("arial bold", 15), state='readonly', corner_radius=20,
                                      fg_color="teal", button_color="teal")
    sexo_cadastro.place(x=400, y=110)

    titulo_peso = ctk.CTkLabel(janela, text="Peso:", width=240, font=("arial bold", 15))
    titulo_peso.place(x=400, y=150)

    peso_cadastro = ctk.CTkEntry(janela, placeholder_text="Digite seu Peso", width=240, font=("arial bold", 15),
                                 corner_radius=20)
    peso_cadastro.place(x=400, y=180)

    titulo_objetivo = ctk.CTkLabel(janela, text="Objetivo:", font=("arial bold", 15), width=240)
    titulo_objetivo.place(x=400, y=220)

    obj_var = ctk.StringVar(value="Selecione seu Objetivo:")

    opcoes_objetivo = ["Ganhar Peso", "Perder Peso", "Manter Peso"]

    objetivo_cadastro = ctk.CTkOptionMenu(janela, variable=obj_var, values=opcoes_objetivo, font=("arial bold", 15),
                                          width=240, dropdown_font=("arial bold", 15), state='readonly',
                                          corner_radius=20, fg_color="teal", button_color="teal")
    objetivo_cadastro.place(x=400, y=250)

    titulo_nivelfisico = ctk.CTkLabel(janela, text="Nível de Atividade Fisica:", font=("arial bold", 15), width=240)
    titulo_nivelfisico.place(x=220, y=290)

    nivel_var = ctk.StringVar(value="Selecione seu Nivel de Atividade:")

    opcoes_nivelfisico = ["Sedentário", "Moderada", "Intesa"]

    nivelfisico_cadastro = ctk.CTkOptionMenu(janela, variable=nivel_var, values=opcoes_nivelfisico,
                                             font=("arial bold", 15), width=266, dropdown_font=("arial bold", 15),
                                             state='readonly', corner_radius=20, fg_color="teal", button_color="teal")
    nivelfisico_cadastro.place(x=207, y=320)

    botaoCadastro = ctk.CTkButton(janela, text="Cadastrar", width=240, command=cadastro, font=("arial bold", 15))
    botaoCadastro.place(x=220, y=365)

    botaoVoltar = ctk.CTkButton(janela, text="Voltar", width=25, command=abrir_tela_login, font=("arial bold", 15))
    botaoVoltar.place(x=0, y=0)

def tela_dados(): #FUNÇÃO QUE CRIA A TELA DE INFORMAÇÕES DOS DADOS DE MACRO,CALORIA E AGUA DO USUÁRIO
    for widget in janela.winfo_children():
        widget.destroy()

    class TelaDados:
        def __init__(self, janela):
            self.janela = janela
            self.janela.title("Informações Nutricionais")

            # Configuração da tela
            self.configurar_tela()

            # Configuração dos gráficos
            self.configurar_graficos()

        def configurar_tela(self):
            # Área para exibir os gráficos
            self.figura = Figure(figsize=(6.8, 3.3), tight_layout=True)
            self.eixo = self.figura.add_subplot(111)
            self.grafico = FigureCanvasTkAgg(self.figura, master=self.janela)
            self.grafico.get_tk_widget().grid(row=0, column=2, rowspan=7, padx=10, pady=10)

        def configurar_graficos(self):
            # Configuração inicial dos gráficos

            for spine in self.eixo.spines.values():
                spine.set_edgecolor('white')

            # Mudar a cor dos números do eixo Y
            for tick_label in self.eixo.get_yticklabels():
                tick_label.set_color('white')

            categorias = ['Calorias', 'Proteínas', 'Carboidratos', 'Lipídios', 'Fíbras', 'Água']
            calorias, proteinas, carboidratos, lipideos, fibras, agua = chamarMacros_telaDados()
            valores_iniciais = calorias, proteinas, carboidratos, lipideos, fibras, agua

            self.barras = self.eixo.bar(categorias, valores_iniciais,
                                        color=['red', 'green', 'blue', 'orange', 'purple', 'cyan'])
            self.eixo.set_facecolor('#2C2C2C')
            self.figura.set_facecolor('#2C2C2C')
            self.eixo.set_ylim(0, 100)  # Define o intervalo do eixo Y de 0 a 100
            self.eixo.set_yticks(range(0, 101, 20))  # Define os ticks no eixo Y
            self.eixo.set_yticklabels(
                [f"{i}%" for i in range(0, 101, 20)])  # Adiciona o símbolo de porcentagem ao eixo Y
            self.eixo.set_xticks(range(len(categorias)))

            cor_das_categorias = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']
            for tick, cor in zip(self.eixo.get_xticklabels(), cor_das_categorias):
                tick.set_color(cor)

            self.eixo.set_xticklabels(categorias, rotation=45, ha="right")

            for categoria, valor in zip(categorias, valores_iniciais):
                
                if valor == 100:
                    exibir_mensagem("Aviso", f"Você bateu a Meta Diária de {categoria}")
                elif valor > 100:
                    exibir_mensagem("Aviso", f"Você ultrapassou a Meta Diária de {categoria}")

    botaoAlimentos = ctk.CTkButton(janela, text="LISTA DE ALIMENTOS", width=300, command=abrir_tela_lista_alimentos,
                                   font=("arial bold", 15))
    botaoAlimentos.place(x=375, y=350)

    botaoLogout = ctk.CTkButton(janela, text="LOGOUT", width=300, command=abrir_tela_login, font=("arial bold", 15))
    botaoLogout.place(x=25, y=350)

    TelaDados(janela)

def abrir_tela_login(): #FUNÇÃO PARA CRIAR A TELA INICIAL DO APP
    global email_login, senha_login

    for widget in janela.winfo_children():
        widget.destroy()

    janela.title("NutriAPP")

    my_image = ctk.CTkImage(light_image=Image.open(r"log.png"),
                            dark_image=Image.open(r"log.png"),
                            size=(340, 400))

    button = ctk.CTkButton(janela, text=None, image=my_image, hover=None, fg_color="white")
    button.place(x=0, y=-10)

    frame = ctk.CTkFrame(janela, width=350, height=400)
    frame.pack(side=RIGHT)

    texto = ctk.CTkLabel(frame, text="Sistema de Login", font=("arial bold", 30), width=300)
    texto.place(x=25, y=5)

    titulo_email = ctk.CTkLabel(frame, text="Email:", font=("arial bold", 18), width=300)
    titulo_email.place(x=25, y=85)

    email_login = ctk.CTkEntry(frame, placeholder_text="Digite seu Email", font=("arial bold", 14), width=300,
                               corner_radius=20)
    email_login.place(x=25, y=120)

    titulo_senha = ctk.CTkLabel(frame, text="Senha:", font=("arial bold", 18), width=300)
    titulo_senha.place(x=25, y=157)

    senha_login = ctk.CTkEntry(frame, placeholder_text="Digite sua Senha", font=("arial bold", 14), show="*", width=300,
                               corner_radius=20)
    senha_login.place(x=25, y=190)

    botaoLogin = ctk.CTkButton(frame, text="Login", width=250, command=fazer_login, font=("arial bold", 15))
    botaoLogin.place(x=50, y=275)

    botaoCadastro = ctk.CTkButton(frame, text="Cadastrar novo Usuário", width=250, command=abrir_tela_cadastro,
                                  font=("arial bold", 15))
    botaoCadastro.place(x=50, y=325)

def função_texto_reifeiçao(nome_da_refeiçao): #FUNÇÃO QUE CRIA OS TEXTOS DE CAFÉ, ALMOÇO, LANCHE E JANTA NA TELA DE LISTA DE ALIMENTOS
    dados_todos_usuarios = carregar_dados_usuarios()

    email = dados_do_usuario_do_email_digitado["Email"]

    usuario_logado = dados_todos_usuarios[email]

    dicionarioAlimentos = função_retorna_cardapio()

    cardapio = gera_cardapio(usuario_logado, dicionarioAlimentos)

    refeiçao = cardapio[nome_da_refeiçao]

    lista = list(refeiçao.keys())
    lista.pop()

    texto = ""
    for alimento in lista:
        texto += (str(alimento) + ": " + refeiçao[alimento]["porcao"] + "\n")

    texto += "\n"

    lista = refeiçao["Total de Macronutrientes"]

    for macronutriente in lista:
        texto += f"{macronutriente}: {lista[macronutriente]:.1f}\n"

    texto_modificado = texto.replace("calorias", "Calorias")

    texto_modificado1 = texto_modificado.replace("proteinas", "Proteínas")

    texto_modificado2 = texto_modificado1.replace("carboidratos", "Carboidratos")

    texto_modificado3 = texto_modificado2.replace("gorduras", "Lipídeos")

    texto_modificado4 = texto_modificado3.replace("fibras", "Fíbras")

    return texto_modificado4

def abrir_tela_lista_alimentos(): #FUNÇÃO QUE CRIA A TELA DE LISTA DE ALIMENTOS ONDE O USUÁRIO IRÁ ATUALIZAR O QUE ELE COMEU NO SEU DIA
    for widget in janela.winfo_children():
        widget.destroy()

    TextoCafeDaManha = função_texto_reifeiçao("Café da manhã")

    TextoAlmoço = função_texto_reifeiçao("Almoço")

    TextoLanche = função_texto_reifeiçao("Lanche")

    TextoJanta = função_texto_reifeiçao("Janta")

    telaRefeiçoes = ctk.CTkTabview(janela, width=550, height=300, corner_radius=35, border_width=3,
                                   segmented_button_unselected_hover_color="teal")
    telaRefeiçoes.pack(pady=22)

    opçoes = ["Café da Manhã", "Almoço", "Lanche", "Janta"]

    for opçao in opçoes:
        telaRefeiçoes.add(opçao)
        telaRefeiçoes.tab(opçao).grid_columnconfigure(0, weight=1)

    CardapioCafe = ctk.CTkLabel(telaRefeiçoes.tab("Café da Manhã"), text=TextoCafeDaManha, font=("arial bold", 16))
    CardapioCafe.pack()

    CardapioAlmoço = ctk.CTkLabel(telaRefeiçoes.tab("Almoço"), text=TextoAlmoço, font=("arial bold", 16))
    CardapioAlmoço.pack()

    CardapioJanta = ctk.CTkLabel(telaRefeiçoes.tab("Lanche"), text=TextoLanche, font=("arial bold", 16))
    CardapioJanta.pack()

    CardapioLanche = ctk.CTkLabel(telaRefeiçoes.tab("Janta"), text=TextoJanta, font=("arial bold", 16))
    CardapioLanche.pack()

    botaoVoltar = ctk.CTkButton(janela, text="Voltar", width=25, command=tela_dados, font=("arial bold", 15))
    botaoVoltar.place(x=0, y=0)

    botaoAtualizarAgua = ctk.CTkButton(janela, text="Atualiziar Água", width=240, command=atualizar_dados_agua,
                                       font=("arial bold", 15))
    botaoAtualizarAgua.place(x=221, y=340)

    barra_pesquisa()

# CRIA ARQUIVO DADOS.TXT

try:
    with open("dados.txt", "r") as arquivo:
        pass
except FileNotFoundError:
    with open("dados.txt", "w") as arquivo:
        pass

# CRIA JANELA DO CUSTOMTKINTER

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

abrir_tela_login()

janela.mainloop()