import random

def selecionar_questoes(numero_total, numero_selecionado):
    # Defina as proporções desejadas para questões fáceis, médias e difíceis
    proporcao_facil = 0.4
    proporcao_media = 0.4
    proporcao_dificil = 0.2

    # Calcule o número de questões para cada dificuldade com base nas proporções
    num_facil = int(numero_selecionado * proporcao_facil)
    num_media = int(numero_selecionado * proporcao_media)
    num_dificil = numero_selecionado - num_facil - num_media

    # Gere índices aleatórios para cada dificuldade
    indices_facil = random.sample(range(1, numero_total + 1), num_facil)
    
    # Converta para lista antes de usar random.choices
    indices_media = random.sample(list(set(range(1, numero_total + 1)) - set(indices_facil)), num_media)
    
    # Converta para lista antes de usar random.choices
    indices_dificil = random.sample(list(set(range(1, numero_total + 1)) - set(indices_facil) - set(indices_media)), num_dificil)

    # Combine os índices de todas as dificuldades
    indices_selecionados = indices_facil + indices_media + indices_dificil

    # Ordene os índices antes de retorná-los
    indices_selecionados.sort()

    return indices_selecionados

# Solicitar entrada do usuário
numero_total_de_questoes = int(input("Digite o número total de questões: "))
numero_de_questoes_selecionadas = int(input("Digite a quantidade desejada de questões a serem selecionadas: "))

# Exemplo de uso
questoes_selecionadas = selecionar_questoes(numero_total_de_questoes, numero_de_questoes_selecionadas)
print("Questões selecionadas:", questoes_selecionadas)

