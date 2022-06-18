from TrabalhoPOO.controladores.controladoraluno import ControladorAluno
from TrabalhoPOO.controladores.controladortreino import ControladorTreino
from TrabalhoPOO.controladores.controladortreinodiario import ControladorTreinoDiario
from TrabalhoPOO.controladores.controladorpersonaltrainer import ControladorPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_treino = ControladorTreino(self)
        self.__controlador_treino_diario = ControladorTreinoDiario(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_personal_trainer = ControladorPersonalTrainer(self)
        self.__tela_sistema = TelaSistema()
        self.__usuario_logado = None

    @property
    def usuario_logado(self):  # conseguimos saber quem logou
        return self.__usuario_logado

    @property
    def controlador_treino(self):
        return self.__controlador_treino

    @property
    def controlador_treino_diario(self):
        return self.__controlador_treino_diario

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_personal_trainer(self):
        return self.__controlador_personal_trainer

    def iniciar_tela_sistema(self):  # OK
        login_com_sucesso = None
        lista_opcoes = {1: self.__tela_sistema.mostrar_tela_aluno,
                        2: self.__controlador_personal_trainer.abre_tela_inicial,
                        0: self.encerrar_sistema}
        login = None
        senha = None
        while True:
            opcao_escolhida = self.__tela_sistema.mostrarMenu_inicial()
            # self.__tela_sistema.logar(opcao_escolhida)  # se for vdd ele vai entrar no menu de cada: aluno ou personal
            login, senha = self.__tela_sistema.logar(opcao_escolhida)
            if opcao_escolhida == 1:
                login_com_sucesso, self.__usuario_logado = self.__controlador_aluno.verificar_login_senha(login, senha)
            elif opcao_escolhida == 2:
                login_com_sucesso = self.__controlador_personal_trainer.verificar_login_senha(login, senha)
            if login_com_sucesso is not None:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                return funcao_escolhida()
            else:
                print("Else não deveria aqui")
                self.__tela_sistema.mostrar_msg_telasistema(f"{opcao_escolhida} invalida, "
                                                            f"digite 1, 2 ou 0 para sair. ")
                self.__tela_sistema.mostrarMenu_inicial()

    def encerrar_sistema(self):  # OK
        exit(0)

    # if opcao_escolhida == 1:
    #     self.__tela_sistema.logar(1)  # se for vdd ele vai entrar no menu de cada: aluno ou personal
    #     login, senha = self.__tela_sistema.logar(1)
    #     verficar = self.__controlador_aluno.verificar_login_senha(login, senha)
    #     if verficar:
    #         funcao_escolhida = lista_opcoes[opcao_escolhida]
    #         return funcao_escolhida()
    #     else:
    #         self.__tela_sistema.mostrar_msg_telasistema(f"{opcao_escolhida} invalida, "
    #                                                     f"digite 1, 2 ou 0 para sair. ")
    #         self.__tela_sistema.mostrarMenu_inicial()
    # elif opcao_escolhida == 2:
    #     login, senha = self.__tela_sistema.logar(2)
    #     if self.__controlador_personal_trainer.verificar_login_senha(login, senha):
    #         funcao_escolhida = lista_opcoes[opcao_escolhida]
    #         return funcao_escolhida()
    # elif opcao_escolhida == 0:
    #     funcao_escolhida = lista_opcoes[opcao_escolhida]
    #     return funcao_escolhida()
