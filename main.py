from neat_training import run_neat_training
from neat_config import load_neat_config
import retro
from test_population import test_population_function  # Adicione essa linha para importar a função de teste

if __name__ == "__main__":
    game_name = 'DaffyDuckTheMarvinMissions-Snes'
    config_filename = 'neat_config.txt'
    population_filename = 'population.pkl'
    env = retro.make(game=game_name)
    config = load_neat_config(config_filename)
    num_generations = 1000
    
    while True:
        print("Menu:")
        print("1. Continuar evolução")
        print("2. Testar população atual")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            run_neat_training(env, config, population_filename, num_generations)
        elif choice == "2":
            test_population_function(env, config, population_filename)
        elif choice == "3":
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções numeradas.")