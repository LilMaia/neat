import neat
from handle_interrupt import handle_interrupt, save_population, load_population
import signal
from evaluation_module import evaluate_genome
from plot import plot_population_statistics

def run_neat_training(env, config, population_filename, num_generations):
    try:
        p = load_population(population_filename)
        print("População carregada com sucesso.")
    except FileNotFoundError:
        p = neat.Population(config)
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)

    signal.signal(
        signal.SIGINT,
        lambda sig, frame: handle_interrupt(sig, frame, p, population_filename),
    )

    def eval_genomes(genomes, config):
        for genome_id, genome in genomes:
            evaluate_genome(genome, config, env)

    try:
        for generation in range(num_generations):
            print(f"Generation {generation}")
            winner = p.run(eval_genomes)
            save_population(p, population_filename)

            best_fitness = winner.fitness
            print("Best genome fitness:", best_fitness)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Saving and exiting...")
        env.close()
        save_population(p, population_filename)
        exit(0)

    save_population(p, "final_population.pkl")
    print("\nTraining completed.")

    # Plot population statistics
    plot_population_statistics(stats)
