import neat
from handle_interrupt import handle_interrupt, save_population, load_population
import signal
from evaluation_module import evaluate_genome

def run_neat_training(env, config, population_filename):
    # Carregar a população salva, se existir
    try:
        p = load_population(population_filename)
        print("População carregada com sucesso.")
    except FileNotFoundError:
        p = neat.Population(config)
    
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    # Configurar o tratamento do sinal de interrupção com o objeto Checkpointer
    signal.signal(signal.SIGINT, lambda sig, frame: handle_interrupt(sig, frame, p, population_filename))

    def eval_genomes(genomes, config):
        for genome_id, genome in genomes:
            evaluate_genome(genome, config, env)

    try:
        winner = p.run(eval_genomes)
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Salvando e encerrando...")
        env.close()
        save_population(p, population_filename)
        exit(0)

    save_population(p, 'final_population.pkl')
    print("\nMelhor indivíduo:\n")
    print(winner)