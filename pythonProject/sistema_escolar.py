import random

lista_alunos = []

def gerar_matricula():
    return random.randint(1, 9999)

def calcular_bolsa(renda_familiar):
    if renda_familiar <= 1412:
        return 1.0
    elif renda_familiar <= 2824:
        return 0.5
    elif renda_familiar <= 4236:
        return 0.3
    else:
        return 0.0

def obter_resposta(mensagem, opcoes_validas):
    while True:
        resposta = input(mensagem).lower()
        if resposta in opcoes_validas:
            return resposta
        else:
            print("Informação inválida. Por favor, corrija.")

def validar_cpf(cpf):
    if cpf.isdigit() and len(cpf) == 11:
        return True
    else:
        return False

def validar_email(email):
    if "@" in email:
        return True
    else:
        return False

def validar_idade(idade):
    return 1 <= idade <= 99

def cadastrar_aluno():
    matricula = gerar_matricula()
    nome = input("Digite o nome do aluno: ")
    sobrenome = input("Digite o sobrenome do aluno: ")

    idade = 0
    while not validar_idade(idade):
        try:
            idade = int(input("Digite a idade do aluno (1-99): "))
        except ValueError:
            print("Informação inválida. Por favor, insira um valor numérico.")
        if not validar_idade(idade):
            print("Idade inválida. Por favor, insira uma idade entre 1 e 99.")

    email = ""
    while not validar_email(email):
        email = input("Digite o email do aluno: ")
        if not validar_email(email):
            print("Email inválido. Por favor, insira um email válido.")

    renda_familiar = 0.0
    while True:
        try:
            renda_familiar = float(input("Digite a renda familiar do aluno: "))
            break
        except ValueError:
            print("Informação inválida. Por favor, insira um valor numérico.")

    cpf = ""
    while not validar_cpf(cpf):
        cpf = input("Digite o CPF do aluno (somente números e 11 dígitos): ")
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, insira um CPF válido.")

    opcoes_escolaridade = ["fundamental", "médio", "superior"]
    escolaridade = obter_resposta("Digite a escolaridade do aluno (Fundamental/Médio/Superior): ", opcoes_escolaridade)

    if idade < 18:
        status = "Menor de idade"
    else:
        status = "Maior de idade"

    while True:
        try:
            nota_enem = int(input("Digite a nota do Enem (0-1000): "))
            break
        except ValueError:
            print("Informação inválida. Por favor, insira um valor numérico.")

    aluno = {
        "Matrícula": matricula,
        "Nome completo": f"{nome} {sobrenome}",
        "Idade": f"{idade} anos ({status})",
        "Email": email,
        "Renda Familiar": f"R${renda_familiar:.2f}",
        "CPF": cpf,
        "Escolaridade": escolaridade,
        "Nota Enem": nota_enem
    }

    if nota_enem < 500:
        percentual_bolsa = calcular_bolsa(renda_familiar)

        if percentual_bolsa > 0:
            aluno["Bolsa"] = f"{percentual_bolsa * 100}%"

    else:
        aluno["Bolsa"] = "Não há direito a bolsa devido à pontuação do Enem."

    lista_alunos.append(aluno)

    print("\nAluno cadastrado com sucesso:")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")

quantidade_alunos = int(input("Digite a quantidade de alunos que deseja cadastrar: "))
for _ in range(quantidade_alunos):
    cadastrar_aluno()

print("\nLista de alunos cadastrados:")
for aluno in lista_alunos:
    print("\n----------------------")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")
