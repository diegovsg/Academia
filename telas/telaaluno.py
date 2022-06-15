class TelaAluno():

    def mostrar_msg(self, msg):
        print(msg)

    def mostrar_aluno(self, dados_aluno): #mostra os dados do aluno
        print("Nome:", dados_aluno["nome"])
        print("Login:", dados_aluno["login"])
        print("Senha:", dados_aluno["senha"])
        print("CPF:", dados_aluno["cpf"])

    def selecionar_aluno_cpf(self): #seleciona aluno por cpf
        cpf = input("Digite o cpf do aluno:")
        return cpf


    def pega_dados_aluno(self): #usuario informa os dados pro usuario
        nome = input("Digite o nome do aluno:")
        login = input("Digite o login do aluno:")
        senha = input("Digite a senha do aluno:")
        cpf = input("Digite o cpf do aluno:")
        return {"nome":nome, "login":login, "senha":senha, "cpf":cpf}

    def mexer_aluno(self):
        print("----- INÍCIO -----")
        print("----- ABA ALUNO -----")
        print("O que você deseja fazer hoje? Digite o número correspondente:")
        print("1 - Cadastrar aluno")
        print("2 - Alterar aluno")
        print("3 - Excluir aluno")
        print("4 - Listar alunos")
        print("5 - Consultar aluno")
        print("6 - Sair")

        opcao = int(input())
        return opcao

