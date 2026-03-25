# NutriApp

Aplicativo desktop para controle nutricional com interface gráfica em CustomTkinter, regras de negócio em camadas e persistência em CSV.

## Objetivo do projeto

Permitir que o usuário:

1. Faça cadastro e login.
2. Receba metas nutricionais calculadas automaticamente.
3. Visualize progresso diário em gráfico.
4. Atualize ingestão de água e macronutrientes.
5. Consulte sugestões de refeições e alimentos.

## Arquitetura em camadas

### Domain

Responsabilidade:

- Modelos centrais do negócio.
- Contratos de abstração.

Arquivos:

- app_domain/models.py
- app_domain/contracts.py
- app_domain/__init__.py

### Application

Responsabilidade:

- Casos de uso.
- Validação de payload de entrada.
- Erros de aplicação por código.

Arquivos:

- app_application/use_cases.py
- app_application/errors.py
- app_application/__init__.py

### Infrastructure

Responsabilidade:

- Persistência de dados em CSV.

Arquivos:

- user_repository_csv.py
- app_infra/user_repository_csv.py
- app_infra/__init__.py

### Presentation

Responsabilidade:

- Interface gráfica e interação com usuário.

Arquivos:

- ui_views.py
- app_presentation/views.py
- app_presentation/__init__.py

### Entry point

- NutriApp.py

## Mapeamento UML para código

### Entidades

- Usuario: app_domain/models.py
- MetaNutricional: app_domain/models.py
- RegistroDiario: app_domain/models.py
- Alimento: app_domain/models.py

### Enumerações

- Sexo: app_domain/models.py
- Objetivo: app_domain/models.py
- NivelAtividade: app_domain/models.py

### Contrato

- UserRepository: app_domain/contracts.py

### Implementação concreta

- UserRepositoryCsv: user_repository_csv.py

### Casos de uso

- LoginUseCase: app_application/use_cases.py
- CadastroUseCase: app_application/use_cases.py
- CadastroInput: app_application/use_cases.py

### Erros de aplicação

- ApplicationError: app_application/errors.py

### Controlador de interface

- AppController: NutriApp.py

## Decisões importantes de modelagem

1. Repositório desacoplado por contrato

A camada de aplicação depende de UserRepository, não da implementação concreta.

2. Erros por código na regra de negócio

Casos de uso retornam códigos de erro por ApplicationError.

O mapeamento de mensagem legível ficou na camada de apresentação, no AppController.

3. Persistência em CSV

A infraestrutura serializa e desserializa Usuario com colunas explícitas.

Também há tratamento de valores inválidos no parse numérico.

4. Compatibilidade de import

Arquivos raiz domain.py, contracts.py e use_cases.py são wrappers de compatibilidade.

## Estrutura de dados CSV

Arquivo padrão: dados.csv

Campos:

- email
- senha
- nome
- sexo
- idade
- peso
- altura
- objetivo
- nivel_fisico
- meta_calorias
- meta_proteinas
- meta_carboidratos
- meta_lipideos
- meta_fibras
- meta_agua_ml
- diario_calorias
- diario_proteinas
- diario_carboidratos
- diario_lipideos
- diario_fibras
- diario_agua_ml

## Requisitos

- Python 3.14 ou compatível
- Dependências do requirements.txt

## Instalação

No diretório do projeto:

1. Criar venv:

python -m venv .venv

2. Ativar no Windows PowerShell:

.\.venv\Scripts\Activate.ps1

3. Instalar dependências:

python -m pip install -r requirements.txt

## Execução

No diretório do projeto:

python NutriApp.py

## Testes

No diretório do projeto:

python -m unittest discover -s tests -v

## Cobertura atual de testes

- Fluxo de login e cadastro.
- Erros de payload de cadastro.
- Persistência CSV principal.
- Casos de borda de CSV:
  - arquivo vazio
  - colunas faltantes
  - valores numéricos inválidos
  - operação sequencial sem usuário
- Filtro de busca de alimentos na UI.

## Observações de qualidade

- Tipagem estática sem erros reportados.
- Suite de testes validada com sucesso.
- Arquitetura preparada para extensão futura com novas implementações de repositório.

## Próximos incrementos recomendados

1. Adicionar logs estruturados na camada de aplicação e infraestrutura.
2. Adicionar exportação de relatório diário em CSV separado.
3. Evoluir para banco relacional mantendo o mesmo contrato UserRepository.
