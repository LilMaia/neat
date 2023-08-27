import neat
from neat_config import load_neat_config
from handle_interrupt import load_population

def test_population_function(env, config, population_filename):
    
    # Carregar a população salva, se existir
    try:
        p = load_population(population_filename)
        print("População carregada com sucesso.")
    except FileNotFoundError:
        print("População não encontrada. Execute a evolução primeiro.")
        return
    
    # Avaliar o desempenho de cada agente da população
    for genome_id, genome in p.population.items():
        print(f"Avaliando genoma {genome_id}...")
        
        # Criar a rede neural com base no genoma
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        
        # Realizar a avaliação do genoma no ambiente
        fitness_total = 0
        for _ in range(10):  # Realizar 10 avaliações para cada genoma
            ob = env.reset()
            done = False
            while not done:
                ob = preprocess_observation(ob)  # Pré-processar a observação, se necessário
                nn_output = network.activate(ob)
                ob, rew, done, _ = env.step(nn_output)
                fitness_total += rew
        genome.fitness = fitness_total / 10  # Média das avaliações
        
        print(f"Genoma {genome_id} avaliado. Pontuação: {genome.fitness}")
    
    env.close()

def preprocess_observation(ob):
    # Adicionar pré-processamento da observação aqui, se necessário
    return ob
