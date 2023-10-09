import pickle

# Função para carregar uma população de genomas de um arquivo
def load_population(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Função para salvar uma população de genomas em um arquivo
def save_population(population, filename):
    with open(filename, 'wb') as f:
        pickle.dump(population, f)
        
# Função para lidar com o sinal de interrupção (Ctrl+C)
def handle_interrupt(signal, frame, population, filename):
    print("Programa interrompido pelo usuário. Salvando e encerrando...")
    # Salvar a população antes de encerrar
    save_population(population, filename)
    exit(0)
