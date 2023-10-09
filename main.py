from neat_training import run_neat_training  # Importa a função de treinamento NEAT
from neat_config import (
    load_neat_config,
)  # Importa a função para carregar a configuração NEAT
import retro  # Importa a biblioteca para criar ambientes de jogos retro
from test_population import (
    test_population_function,
)  # Importa a função de teste de população

if __name__ == "__main__":
    game_name = "DaffyDuckTheMarvinMissions-Snes"  # Nome do jogo retro
    config_filename = "neat_config.txt"  # Nome do arquivo de configuração NEAT
    population_filename = "population.pkl"  # Nome do arquivo de população
    env = retro.make(game=game_name)  # Cria o ambiente de jogo retro
    config = load_neat_config(
        config_filename
    )  # Carrega a configuração NEAT a partir de um arquivo
    num_generations = 1000  # Número de gerações para o treinamento

    while True:
        print("Menu:")
        print("1. Continuar evolução")
        print("2. Testar população atual")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            # Executa o treinamento NEAT
            run_neat_training(env, config, population_filename, num_generations)
        elif choice == "2":
            # Testa a população atual
            test_population_function(env, config, population_filename)
        elif choice == "3":
            # Sai do programa
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções numeradas.")
