import matplotlib.pyplot as plt


# Função para plotar estatísticas da população ao longo das gerações
def plot_population_statistics(stats):
    # Criar uma lista de números de geração (1 até o número de estatísticas de geração)
    generations = range(1, len(stats.generation_statistics) + 1)

    # Criar uma lista de valores de média de fitness para cada geração
    mean_fitness = [s.mean_fitness for s in stats.generation_statistics]

    # Criar uma lista de valores de fitness máximo para cada geração
    max_fitness = [s.max_fitness for s in stats.generation_statistics]

    # Criar um novo gráfico
    plt.figure()

    # Plotar a média de fitness em relação às gerações
    plt.plot(generations, mean_fitness, label="Mean Fitness")

    # Plotar o fitness máximo em relação às gerações
    plt.plot(generations, max_fitness, label="Max Fitness")

    # Definir rótulos dos eixos x e y
    plt.xlabel("Generation")
    plt.ylabel("Fitness")

    # Definir o título do gráfico
    plt.title("Population Statistics")

    # Adicionar uma legenda ao gráfico
    plt.legend()

    # Exibir o gráfico
    plt.show()
