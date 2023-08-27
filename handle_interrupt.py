import pickle

def load_population(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save_population(population, filename):
    with open(filename, 'wb') as f:
        pickle.dump(population, f)
        
# Função para lidar com o sinal de interrupção (Ctrl+C)
def handle_interrupt(signal, frame, p, filename):
    print("Programa interrompido pelo usuário. Salvando e encerrando...")
    # Salvar a população antes de encerrar
    save_population(p, filename)
    exit(0)