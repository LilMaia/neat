import matplotlib.pyplot as plt

def plot_population_statistics(stats):
    generations = range(1, len(stats.generation_statistics) + 1)
    mean_fitness = [s.mean_fitness for s in stats.generation_statistics]
    max_fitness = [s.max_fitness for s in stats.generation_statistics]

    plt.figure()
    plt.plot(generations, mean_fitness, label="Mean Fitness")
    plt.plot(generations, max_fitness, label="Max Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Population Statistics")
    plt.legend()
    plt.show()