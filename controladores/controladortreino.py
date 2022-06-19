from entidades.treino import Treino
from telas.telatreino import TelaTreino
from entidades.tipoexercicio import TipoExercicio


class ControladorTreino():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__treinos = []
        self.__manter_tela = True
        self.__tela_treino = TelaTreino()
        self.__tipos_exercicio = [TipoExercicio("Muscular - Superior",200), TipoExercicio("Muscular - Inferior",150), \
        TipoExercicio("Cardiovascular",300)]

    @property
    def tipos_exercicio(self):
        return self.__tipos_exercicio

    def incluir_treino(self):
        novo_treino, nome_treino = self.__tela_treino.montar_treino() #pedir se quer incluir novo treino e o nome do treino 
        while (novo_treino==1) and (nome_treino is not None): #pra criar novo treino
            treino = Treino(nome_treino) #instancia o treino
            self.criar_exercicio(treino) #chama o método para incluir exercicios no treino
            #!verificar se já existe o treino
            self.__treinos.append(treino) #adiciona o treino a lista de todos os treinos do sistema
            aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno() #seleciona o aluno pra vincular #seleciona a instancia do aluno
            aluno.adicionar_treino_aluno(treino) #chama o método pela instancia do aluno
            novo_treino, nome_treino = self.__tela_treino.montar_treino() #pedir se quer incluir novo treino e o nome do treino 

    def criar_exercicio(self, treino: Treino):
        novo_exercicio, dados_exercicio = self.__tela_treino.montar_exercicio(self.__tipos_exercicio)
        #!verificar se os dados_exercicio não são vazios
        while novo_exercicio==1: #pra criar novo exercicio
            treino.incluir_exercicio(dados_exercicio["nome"], dados_exercicio["serie"], dados_exercicio["repeticao"],\
            dados_exercicio["tempo_descanso"], self.__tipos_exercicio[dados_exercicio["tipo_exercicio"]])
            novo_exercicio, dados_exercicio = self.__tela_treino.montar_exercicio(self.__tipos_exercicio)

    def excluir_treino(self):
        treino = self.pegar_treino_por_nome() #busca infos do treino requisitado
        if (treino is not None):
            self.__treinos.remove(treino)
            aluno = self.__controlador_sistema.controlador_aluno.buscar_aluno_por_treino(treino)
            aluno.remover_treino_aluno(treino) #!!!checar se está chamando o aluno mesmo
        else:
            self.__tela_treino.mostrar_msg("ATENCAO: treino não existente")

    def pegar_treino_por_nome(self):
        nome_treino = self.__tela_treino.selecionar_treino_por_nome()
        for treino in self.__treinos:
            if treino.nome == nome_treino:
                return treino
        else:
            return None

    def alterar_treino(self):
        treino = self.pegar_treino_por_nome()
        if (treino is not None):
            opcao = self.__tela_treino.escolher_alteracao_treino()
            if opcao==1:
                self.alterar_nome_treino(treino)
            elif opcao==2:
                treino.excluir_exercicios() #exclui os exercicios do treino
                self.criar_exercicio(treino) #inclui os novos exercicios do treino
        else:
            self.__tela_treino.mostrar_msg("ATENCAO: treino não existente")
        
    def alterar_nome_treino(self, treino: Treino):
        treino.nome = self.__tela_treino.selecionar_treino_por_nome()

    def consultar_treino(self):
        treino = self.pegar_treino_por_nome()
        if (treino is not None):
            treino = {"nome":treino.nome, "exercicios":treino.exercicios}
            self.__tela_treino.mostrar_tela_treino(treino)
        else:    
            self.__tela_treino.mostrar_msg("ATENCAO: treino não existente")

    def retornar(self):
        pass
