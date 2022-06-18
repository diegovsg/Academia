class TelaAluno():

    def mostrar_msg(self, msg):
        print(msg)

    def mostrar_aluno(self, dados_aluno): #mostra os dados do aluno
        print("Nome:", dados_aluno["nome"])
        print("Login:", dados_aluno["login"])
        print("Senha:", dados_aluno["senha"])
        print("CPF:", dados_aluno["cpf"])
        print("Treinos:", dados_aluno["treinos"])

    def pega_dados_aluno(self): 
        nome = input("Digite o nome do aluno:")
        login = input("Digite o login do aluno:")
        senha = input("Digite a senha do aluno:")
        cpf = input("Digite o cpf do aluno:")
        return {"nome":nome, "login":login, "senha":senha, "cpf":cpf}

    def mexer_aluno(self):
        print("----- INÍCIO -----")
        print("----- ABA ALUNO -----") # Aba personal ?
        print("O que você deseja fazer hoje? Digite o número correspondente:")
        print("1 - Cadastrar aluno")
        print("2 - Alterar aluno")
        print("3 - Excluir aluno")
        print("4 - Listar alunos")
        print("5 - Consultar aluno")
        print("6 - Sair")
        print("7 - Consultar Desempenho")

        opcao = int(input())
        return opcao

    def opcao_alterar(self):
        print("----- ALTERAR ALUNO -----")
        print("O que você deseja alterar no aluno?")
        print("1 - Alterar nome")
        print("2 - Alterar cpf")
        print("3 - Alterar login")
        print("4 - Alterar senha")
        print("5 - Sair")

        opcao = int(input())
        return opcao

    def pegar_nome(self):
        nome = input("Digite o nome do aluno:")
        return nome

    def pegar_cpf(self):
        cpf = input("Digite o cpf do aluno:")
        return cpf

    def pegar_login(self):
        login = input("Digite o login do aluno:")
        return login

    def pegar_senha(self):
        senha = input("Digite a senha do aluno:")
        return senha
