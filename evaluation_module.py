import cv2
import numpy as np
import neat


# Função que avalia o desempenho de um genoma (rede neural) em um ambiente
def evaluate_genome(genome, config, env):
    # Resetar o ambiente e obter a primeira observação
    ob = env.reset()
    ac = env.action_space.sample()

    # Redimensionar as dimensões da observação
    inx, iny, inc = env.observation_space.shape
    inx = int(inx / 8)
    iny = int(iny / 8)

    # Criar a rede neural com base no genoma
    network = neat.nn.FeedForwardNetwork.create(genome, config)

    # Inicializar variáveis de controle do desempenho do genoma
    current_max_fitness = 0

    pontuação_atual = 0
    vida_atual = 0
    quantidade_de_vidas = 0

    pontuação_inicial = 0
    vida_inicial = 0
    quantidade_de_vida_inicial = 0

    fitness_current = 300000

    frame = 0
    counter = 0
    done = False

    # Loop principal de avaliação do genoma
    while not done:
        env.render()  # Renderizar o ambiente
        frame += 1

        # Pré-processamento da observação
        ob = cv2.resize(ob, (inx, iny))
        ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
        ob = np.reshape(ob, (inx, iny)) 
        imgarray = np.ndarray.flatten(ob)

        # Ativar a rede neural com base na observação pré-processada
        nn_output = network.activate(imgarray)

        # Executar a ação na rede neural no ambiente e obter resultados
        ob, rew, done, info = env.step(nn_output)

        # Atualizar a pontuação do genoma com base nas recompensas obtidas
        fitness_current += rew

        # Incrementa a recompensa se o agente avançar na fase
        if info["score"] > pontuação_atual:
            fitness_current += 100000
        elif info["score"] == 0:
            fitness_current -= 100

        # Incrementa a recompensa de acordo com a barra de vida do personagem
        if info["health"] < vida_atual:
            fitness_current -= 500

        # Incrementa a recompensa de acordo com a quantidade de vidas(tentativas) do personagem
        if info["lives"] < quantidade_de_vidas:
            fitness_current -= 50000

        if counter <= 1 or counter % 1001 == 0:
            pontuação_inicial = info["score"]
            vida_inicial = info["health"]
            quantidade_de_vida_inicial = info["lives"]

        if counter % 1000 == 0:
            if (
                pontuação_atual == pontuação_inicial
                and vida_atual == vida_inicial
                and quantidade_de_vidas == quantidade_de_vida_inicial
            ):
                fitness_current -= 300000

        # Pegando a pontuação atual da iteração para usar de comparativo na proxima iteração
        pontuação_atual = info["score"]

        # Pegando a vida atual da iteração para usar de comaprativo na proxima iteração
        vida_atual = info["health"]

        # Pegando a quantidade de vidas que o agente possui a cada iteração
        quantidade_de_vidas = info["lives"]

        # Atualizar a pontuação máxima e o contador de estagnação
        if fitness_current > current_max_fitness:
            current_max_fitness = fitness_current
            counter += 1
        else:
            counter += 1

        # Verificar condições de término da avaliação
        if done or counter == 4001:
            print("Pontuação do agente atual no jogo : ", pontuação_atual)
            done = True
            print(genome.key, fitness_current)

        # Atualizar a pontuação do genoma
        genome.fitness = fitness_current
