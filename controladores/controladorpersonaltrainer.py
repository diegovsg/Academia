from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema
from TrabalhoPOO.telas.telaaluno import TelaAluno


# from TrabalhoPOO.controladores.controladortreinodiario import TreinoDiario
# from TrabalhoPOO.controladores.controladorsistema import ControladorSistema


class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__tela_aluno = TelaAluno()
        self.__tela_sistema = TelaSistema()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema
        self.__personal = PersonalTrainer("12345678905", "Judi", "a", "a", "01")  # criou o personal

    @property
    def consultar_personal(self):
        return self.__personal

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            if self.__personal.login == login and self.__personal.senha == senha:  # get
                return True

    def abre_tela_inicial(self):  # abre a tela personal pos login da tela do sistema
        mexer_personal_opcoes = {1: self.abre_tela_funcoes_personal,
                                 2: self.__controlador_sistema.controlador_aluno.abre_tela_funcoes_aluno,
                                 3: self.__controlador_sistema.controlador_treino.abre_tela_funcoes_treino,
                                 0: self.__tela_personal.mexer_personal
                                 }
        while True:
            opcao_escolhida = self.__tela_personal.mexer_personal()
            funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
            return funcao_escolhida()

    def voltar(self):
        return self.abre_tela_inicial()

    def abre_tela_funcoes_personal(self):
        mexer_personal_opcoes = {1: self.consultar_personal,
                                 2: self.alterar_personal,
                                 0: self.voltar
                                 }
        while True:
            opcao_escolhida = self.__tela_personal.tela_aba_personal()
            if opcao_escolhida == 1:
                # {"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                #      "treinos": aluno.treinos})
                self.__tela_personal.mostrar_personal_trainer({"nome": self.__personal.nome, "cpf": self.__personal.cpf,
                                                               "login": self.__personal.login,
                                                               "senha": self.__personal.senha, "habilitacao":
                                                                   self.__personal.habilitacao})
                return self.voltar()
            else:
                funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
                return funcao_escolhida()

    # def abre_tela_inicial(self):  # abre a tela personal pos login da tela do sistema
    #     mexer_personal_opcoes = {1: self.alterar_personal,
    #                              2: self.tela_alterar_dados_alunos,
    #                              3: self.__controlador_sistema.controladortreino.abre_tela_funcoes_treino
    #                              0: self.retornar
    #                              }
    #     while True:
    #         opcao_escolhida = self.__tela_personal.mexer_personal()
    #         if opcao_escolhida == 0:
    #             return self.retornar(0)
    #         else:
    #             funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
    #         return funcao_escolhida()

    def alterar_personal(self):  # aqui ele está alterando os dados do personal baseado no dicionario da tela
        if self.__personal is not None:  # OK
            novos_dados = self.__tela_personal.tela_alterar_dados()  # vai ser um dicionario
            self.__personal.nome = novos_dados["nome"]
            self.__personal.cpf = novos_dados["habilitacao"]
            self.__personal.login = novos_dados["login"]
            self.__personal.senha = novos_dados["senha"]
            self.__personal.habilitacao = novos_dados["habilitacao"]

        return self.abre_tela_funcoes_personal()

    # def tela_alterar_dados_alunos(self):  # abre_tela_inicial manda para ca
    #     # na tela personal tem a opcao do personal escolher
    #     return self.__controlador_sistema.controlador_aluno.abre_tela_funcoes_aluno()
    #     # print("ii", self)
    #     # while True:
    #     #     opcao_modificar_aluno = self.__controlador_sistema.controlador_aluno.abre_tela_funcoes_aluno
    #     #     funcao_escolhida = mexer_personal_opcoes[opcao_modificar_aluno]
    #     #     return funcao_escolhida()

    def colocar_treino_na_lista_treino_diario(self):
        self.__controlador_sistema.controlador_treino_diario.colocar_treino_na_lista_treino_diario()

    def consultar_tela_desempenho(self):  # NAO TEM A OPCAO NA LISTA DE MEXER ALUNO!
        return self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario()

    def consultar_desempenho(self):
        escolha = self.consultar_tela_desempenho()

    def retornar(self, opcao_escolhida):
        return self.__tela_sistema.logar(opcao_escolhida)
