
class TelaTreinoDiario():
    def __init__(self):
        pass

    def mostrar_tela_desempenho(self):
        print("Ola Aluno e/ou Professor, você quer consultar o desempenho?")
        print("1 - SIM!")
        print("0 - Voltar")
        escolha = int(input())
        return escolha

    def printar_tela_treino_diario(self):
        print("Ola Professor, você que você deseja?")
        print("1 - consultar o desempenho")
        print("2 - Voltar ao menu inicial")
        print("3 - Colocar os treinos para o aluno vê") # faz sentido ? ou só em treino
        escolha = int(input())
        return escolha

    # def colocar_treino_na_lista_treino_diario(self):
    #     treino_1 = input("Digite o nome do treino:")
    #     treino_2 = input("Digite o nome do treino:")
    #     treino_3 = input("Digite o nome do treino:")
    #     treino_4 = input("Digite o nome do treino:")
    #     return {"treino_1": treino_1, "treino_2": treino_2, "treino_3": treino_3, "treino_4": treino_4}

    def mensagem(self, msg):
        return msg

    def checkin(self, dias):
        print(f"Você fez {dias} de exercício, parabéns! Continue fime.")
