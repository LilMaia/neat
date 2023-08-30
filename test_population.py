import neat
from neat_config import load_neat_config
from handle_interrupt import load_population
from evaluation_module import evaluate_genome

def test_population_function(env, config, population_filename):
    # Load the saved population
    population = load_population(population_filename)

    # Iterate through the genomes and their keys in the population
    for genome_id, genome in population.population.items():
        evaluate_genome(genome, config, env)
