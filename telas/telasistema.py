class TelaSistema:
    def mostrarMenu_inicial(self):
        global opcao
        try:
            print("Olá, bem vindo! Aqui começa sua jornada"
                  " para superar seus limites!")
            print("Faça seu login")
            print("1 - Aluno")
            print("2 - Professor")
            print("0 - Sair")
            opcao = int(input())
        except ValueError:
            if opcao != 1 and opcao != 2:
                print("Você só pode apertar 1 ou 2, caro padawan")
        return opcao

    def logar(self, opcao_escolhida):
        login = None
        senha = None
        if opcao_escolhida == 1:
            print("Bem vindo ao login")
            print('Aluno, digite seu login')
            login = input()
            print('Aluno, digite sua senha')
            senha = input()
        elif opcao_escolhida == 2:
            print("Bem vindo ao login")
            print('Professor, digite seu login')
            login = input()
            print('Professor, digite sua senha')
            senha = input()
        return login, senha

    def mostrar_msg_telasistema(self, msg):
        return msg
