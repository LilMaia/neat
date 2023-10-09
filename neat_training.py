import neat
from handle_interrupt import handle_interrupt, save_population, load_population
from evaluation_module import evaluate_genome
from plot import plot_population_statistics
import signal

def run_neat_training(env, config, population_filename, num_generations):
    try:
        # Tenta carregar uma população previamente salva do arquivo
        p = load_population(population_filename)
        print("População carregada com sucesso.")
    except FileNotFoundError:
        # Caso o arquivo não seja encontrado, cria uma nova população com base na configuração
        p = neat.Population(config)
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)

    # Configura o tratamento de interrupção (Ctrl+C)
    signal.signal(
        signal.SIGINT,
        lambda sig, frame: handle_interrupt(sig, frame, p, population_filename),
    )

    def eval_genomes(genomes, config):
        # Avalia os genomas da população
        for genome_id, genome in genomes:     
            evaluate_genome(genome, config, env)

    try:
        for generation in range(num_generations):
            print(f"Generation {generation}")
            winner = p.run(eval_genomes)
            save_population(p, population_filename)
            
            # Atualiza as estatísticas após cada geração
            stats.update(p)

            # Obtem o número de espécies na população nesta geração
            num_species = len(stats.get_species())
            print("Número de espécies na população:", num_species)
            
            best_fitness = winner.fitness
            print("Best genome fitness:", best_fitness)

    except KeyboardInterrupt:
        # Trata a interrupção do usuário (Ctrl+C) e salva a população antes de encerrar
        print("\nProgram interrupted by user. Saving and exiting...")
        env.close()
        save_population(p, population_filename)
        exit(0)

    # Salva a população após a conclusão do treinamento
    save_population(p, "final_population.pkl")
    print("\nTraining completed.")

    # Plota as estatísticas da população
    plot_population_statistics(stats)
