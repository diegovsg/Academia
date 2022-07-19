import PySimpleGUI as sg


class TelaAluno():

    def __init__(self):
        self.__window = None
        self.layout_pegar_nome()
        self.layout_pegar_cpf()
        self.layout_pegar_login()
        self.layout_pegar_senha()
        self.layout_opcao_alterar()
        #self.mostrar_aluno()
        self.layout_mexer_aluno()
        self.layout_pega_dados_aluno()
        self.layout_escolher_opcao_treino()

    def mostrar_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def mostrar_aluno(self, dados_aluno):  # mostra os dados do aluno
        infos_aluno = "Nome:" + dados_aluno["nome"] + '\n'
        infos_aluno = infos_aluno + "Login:" + dados_aluno["login"] + '\n'
        infos_aluno = infos_aluno + "Senha:" + dados_aluno["senha"] + '\n'
        infos_aluno = infos_aluno + "CPF:" + dados_aluno["cpf"] + '\n'
        infos_aluno = infos_aluno + "Treinos:" + dados_aluno["treinos"] + '\n'
        sg.popup("------DADOS ALUNO------", infos_aluno)

    def mostrar_treino_aluno(self, treinos):
        botoes_treinos = []
        for id, treino in enumerate(treinos):
            botoes_treinos.append([sg.Radio(id, "RD1", key=treino.nome)])
        layout = [
            [sg.Text('Qual treino você deseja alterar?')],
            botoes_treinos,
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        treino_escolhido = values[treino.nome]
        #alterar para dicionário e retornar certo
        return treino_escolhido

    def escolher_opcao_treino(self):
        self.layout_escolher_opcao_treino()
        button, values = self.__window.Read()
        escolha = 0
        if values['1']:
            escolha = 1
        elif values['2']:
            escolha = 2
        return escolha

    def layout_escolher_opcao_treino(self):
        layout = [
            [sg.Text('O que você deseja fazer?', font=("Helvica", 25))],
            [sg.Radio('Excluir um treino de um aluno', "RD2", key='1')],
            [sg.Radio('Adicionar um treino ao aluno', "RD2", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        
    def pega_dados_aluno(self):
        self.layout_pega_dados_aluno()
        button, values = self.__window.Read()
        nome = values['nome']
        login = values['login']
        senha = values['senha']
        cpf = values['cpf']
        #tratar botão cancelar e inserções incorretas
        return {"nome": nome, "login": login, "senha": senha, "cpf": cpf}

    def layout_pega_dados_aluno(self):
        layout = [
            [sg.Text('Digite o nome do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='nome')],
            [sg.Text('Digite o login do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='login')],
            [sg.Text('Digite a senha do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='senha')],
            [sg.Text('Digite o cpf do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)

    def mexer_aluno(self):
        self.layout_mexer_aluno()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def layout_mexer_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('----- INÍCIO -----', font=("Helvica", 25))],
            [sg.Text('----- ABA ALUNO -----', font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer hoje?', font=("Helvica", 15))],
            [sg.Radio('Cadastrar aluno', "RD3", key='1')],
            [sg.Radio('Alterar aluno', "RD3", key='2')],
            [sg.Radio('Excluir aluno', "RD3", key='3')],
            [sg.Radio('Listar alunos', "RD3", key='4')],
            [sg.Radio('Consultar aluno', "RD3", key='5')],
            [sg.Radio('Consultar Desempenho do aluno', "RD3", key='6')],
            [sg.Radio('Retornar', "RD3", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)

    def opcao_alterar(self):
        self.layout_opcao_alterar()
        button, values = self.__window.Read()
        opcao = 0
        if values['nome']:
            opcao = 1
        elif values['cpf']:
            opcao = 2
        elif values['login']:
            opcao = 3
        elif values['senha']:
            opcao = 4
        elif values['treino']:
            opcao = 5
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def layout_opcao_alterar(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('----- ALTERAR ALUNO -----', font=("Helvica", 25))],
            [sg.Text('O que você deseja alterar no aluno?', font=("Helvica", 15))],
            [sg.Radio('Alterar nome', "RD4", key='nome')],
            [sg.Radio('Alterar cpf', "RD4", key='cpf')],
            [sg.Radio('Alterar login', "RD4", key='login')],
            [sg.Radio('Alterar senha', "RD4", key='senha')],
            [sg.Radio('Alterar treino', "RD4", key='treino')],
            [sg.Radio('Retornar', "RD4", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)

    def layout_pegar_nome(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite o nome do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='nome')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def pegar_nome(self):
        self.layout_pegar_nome()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            nome = None
        else:
            nome = values['nome']
        return nome

    def pegar_cpf(self):
        self.layout_pegar_cpf()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            cpf = None
        else:
            cpf = values['cpf']
        return cpf

    def layout_pegar_cpf(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite o cpf do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='cpf')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def pegar_login(self):
        self.layout_pegar_login()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            login = None
        else:
            login = values['login']
        return login

    def layout_pegar_login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite o login do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='login')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def pegar_senha(self):
        self.layout_pegar_senha()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            senha = None
        else:
            senha = values['senha']
        return senha

    def layout_pegar_senha(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite a senha do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='senha')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)
