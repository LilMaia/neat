import neat
from neat_config import (
    load_neat_config,
)  # Importa a função para carregar a configuração NEAT
from handle_interrupt import (
    load_population,
)  # Importa a função para carregar a população salva
from evaluation_module import evaluate_genome  # Importa a função para avaliar um genoma


def test_population_function(env, config, population_filename):
    # Carrega a população salva
    population = load_population(population_filename)

    # Itera através dos genomas e suas chaves na população
    for genome_id, genome in population.population.items():
        # Avalia cada genoma usando a função de avaliação fornecida
        evaluate_genome(genome, config, env)
