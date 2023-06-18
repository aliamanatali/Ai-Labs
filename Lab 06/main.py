import random

def genetic_algorithm(population_size, Utility):
    population = generate_population(population_size)

    generation = 1
    max_generations = 50

    while True:
        new_population = []

        # Reproduction and mutation
        for _ in range(population_size):
            parent1 = random_selection(population, Utility)
            parent2 = random_selection(population, Utility)
            child = reproduce(parent1, parent2)
            if random.random() <= 0.05:  # Mutation with 5% probability
                child = mutate(child)
            new_population.append(child)

        population = new_population

        flag = False
        for individual in population:
            if Utility(individual) == 28:
                flag = True
                break

        generation += 1
        if flag or generation == max_generations:
            break

    best_individual = max(population, key=Utility)
    return best_individual
    #     best_individual = max(population, key=Utility)
    #
    #     if Utility(best_individual) >= 28:
    #         break
    #
    #     generation += 1
    #     if generation == max_generations:
    #         break
    #
    #
    # return best_individual


def generate_population(population_size):
    population = []
    for _ in range(population_size):
        state = []
        for _ in range(8):
            state.append(random.randint(0,7))
        population.append(state)
    return population


def random_selection(population, Utility):
    fitness_values = [Utility(individual) for individual in population]
    total_fitness = sum(fitness_values)
    relative_fitness = [fitness/total_fitness for fitness in fitness_values]
    return random.choices(population, weights=relative_fitness)[0]


# Create a child individual by swapping random positions between parents
def reproduce(parent1, parent2):
    crossover_point = random.randint(0, 7)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


# Randomly swap two positions in the individual
def mutate(individual):
    pos1 = random.randint(0, 7)
    pos2 = random.randint(0, 7)
    individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
    return individual


def fitness_fn(individual):
    conflicts = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                conflicts += 1
    return conflicts


def Utility(state):
    conflicts = fitness_fn(state)
    return 28 - conflicts


def printState(state):
    for i in range(8):
        row = ""
        for j in range(8):
            if i == state[j]:
                row += "* "
            else:
                row += ". "
        print(row)


solution = genetic_algorithm(population_size=8, Utility=Utility)
print("Utility:", fitness_fn(solution))
print("State: ")
printState(solution)