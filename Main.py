from Chromosome import Chromosome
import random
import copy

class Main:
    # Config
    INITIAL_POPULATION = 100
    GENERATIONS_QUANTITY = 40
    CROSSOVER_FACTOR = 0.6
    MUTATION_FACTOR = 0.3
    BINARY_MUTATION_FACTORY = 5

    def __init__(self):
        self.population = []
        self.population_size = 0
        self.generation = 1

        self.generate_initial_population()
        while self.GENERATIONS_QUANTITY > 0:
            self.generate_new_population()
            self.GENERATIONS_QUANTITY -= 1
        self.population.sort(key=lambda Chromosome: (Chromosome.fitness, Chromosome.generation), reverse=True)
        better_chromosome = self.population[0]
        self.show_knob_position(better_chromosome)

    def generate_initial_population(self):
        for i in range(0, self.INITIAL_POPULATION):
            cromossomo = Chromosome(self.generation)
            for j in range(0, 36):
                cromossomo.binary_vector[j] = random.randint(0, 1)
            cromossomo.load_fitness()
            self.population.append(cromossomo)

    def generate_new_population(self):
        self.generation += 1
        self.elitist_selection()
        # print("1",len(self.population))
        self.crossover_selection()
        # print("2",len(self.population))
        self.mutation_selection()
        # print("3",len(self.population))
        # print(self.population[0].fitness)

    def mutation_selection(self):
        population = copy.deepcopy(self.population)
        auxiliar_population = []
        mutation_number = int(len(population) * self.MUTATION_FACTOR)
        while mutation_number > 0:
            random_number = random.randint(0, len(population)-1)
            chromosome = population[random_number]
            for i in range(0, self.BINARY_MUTATION_FACTORY):
                index = random.randint(0, 35)
                chromosome.binary_vector[index] = 0 if chromosome.binary_vector[index] == 1 else 1
            auxiliar_population.append(chromosome)
            population.pop(random_number)
            mutation_number -= 1
        self.population.extend(auxiliar_population)

    def elitist_selection(self):
        auxiliar_population = []
        self.population.sort(key=lambda Chromosome: (Chromosome.fitness, Chromosome.generation), reverse=True)
        for i in range(0, self.INITIAL_POPULATION - 1):
            auxiliar_population.append(self.population[i])
        self.population.clear()
        self.population.extend(auxiliar_population)
        self.population_size = len(self.population)

    def crossover_selection(self):
        population = copy.deepcopy(self.population)
        auxiliar_population = []
        applyed_crossover_population = []
        crossover_size = int(len(population) * self.CROSSOVER_FACTOR)
        while crossover_size > 0:
            random_index = random.randint(0, len(population) - 1)
            auxiliar_population.append(population[random_index])
            population.pop(random_index)
            crossover_size -= 1

        auxiliar_chromosome = Chromosome(self.generation)
        i = 0
        for chromosome in auxiliar_population:
            if i == 0:
                auxiliar_chromosome = chromosome
            else:
                applyed_crossover_population.extend(self.apply_crossover(auxiliar_chromosome, chromosome))
                i = 0
            i += 1
        auxiliar_population.extend(applyed_crossover_population)
        self.population.extend(auxiliar_population)

    def apply_crossover(self, chromosome1: Chromosome, chromosome2: Chromosome):
        applyed_crossover_population = []
        son_chromosome1 = Chromosome(self.generation)
        son_chromosome2 = Chromosome(self.generation)

        court_number = random.randint(0, 35)
        for i in range(0, 36):
            if i >= court_number:
                son_chromosome1.binary_vector[i] = chromosome2.binary_vector[i]
                son_chromosome2.binary_vector[i] = chromosome1.binary_vector[i]
            else:
                son_chromosome1.binary_vector[i] = chromosome1.binary_vector[i]
                son_chromosome2.binary_vector[i] = chromosome2.binary_vector[i]

        son_chromosome1.load_fitness()
        applyed_crossover_population.append(son_chromosome1)
        son_chromosome2.load_fitness()
        applyed_crossover_population.append(son_chromosome2)
        return applyed_crossover_population

    def show_knob_position(self, chromosome: Chromosome):
        count = 0
        knob_number = 1;
        knob_value = ""
        print("Fitness:" + str(chromosome.fitness))
        for i in range(0, 36):
            knob_value += str(chromosome.binary_vector[i])
            if count == 3:
                print("Knob: " + str(knob_number) + " => " + str(int(knob_value, 2)), "| bin =>", str(knob_value))
                # print("Botão: " + str(knob_number) + " => " + str(knob_value))
                count = 0
                knob_number += 1
                knob_value = ""
            else:
                count += 1
Main()