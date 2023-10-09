import neat


# Função para carregar uma configuração NEAT a partir de um arquivo
def load_neat_config(config_filename):
    # Cria uma configuração NEAT com base no arquivo especificado
    return neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_filename,
    )
