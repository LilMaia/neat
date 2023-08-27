import retro
import cv2
import numpy as np
import neat

# Função de avaliação do genoma
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        ob = env.reset()
        ac = env.action_space.sample()

        # Redimensionamento das dimensões de entrada
        inx, iny, inc = env.observation_space.shape
        inx = int(inx/8)
        iny = int(iny/8)

        # Criar rede neural a partir do genoma e configuração
        network = neat.nn.FeedForwardNetwork.create(genome, config)

        current_max_fitness = 0
        fitness_current = 0
        frame = 0
        counter = 0
        done = False

        while not done:
            env.render()
            frame += 1
            ob = cv2.resize(ob, (inx, iny))
            ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
            ob = np.reshape(ob, (inx, iny))

            imgarray = np.ndarray.flatten(ob)

            # Ativar a rede neural com a entrada da imagem
            nnOutput = network.activate(imgarray)
            ob, rew, done, info = env.step(nnOutput)

            fitness_current += rew

            if fitness_current > current_max_fitness:
                current_max_fitness = fitness_current
                counter = 0
            else:
                counter += 1

            if done or counter == 250:
                done = True
                print(genome_id, fitness_current)

            # Atribuir a aptidão ao genoma
            genome.fitness = fitness_current

# Carregar o ambiente do Gym Retro
env = retro.make(game='DaffyDuckTheMarvinMissions-Snes')

# Carregar o arquivo de configuração do NEAT
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'neat_config.txt')

# Criar a população do NEAT
p = neat.Population(config)

# Adicionar relatórios para visualização
p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)

# Rodar o algoritmo NEAT
winner = p.run(eval_genomes)

# Exibir o vencedor
print('\nMelhor indivíduo:\n')
print(winner)