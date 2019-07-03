class Chromosome:

    def __init__(self, generation):
        self.generation = generation
        self.fitness = 0
        self.binary_vector = [0] * 36

    # Função de Avaliação(fitness) =
    # 9 + b2b5−b23b14 + b24b4−b21b10 + b36b15−b11b26 + b16b17 + b3b33 + b28b19 + b12b34−b31b
    # 32−b22b25 + b35b27−b29b7 + b8b13−b6b9 + b18b20−b1b30 + b23b4 + b21b15 + b26b16 + b31b1
    # 2 + b25b19 + b7b8 + b9b18 + b1b33
    def load_fitness(self):
        fitness = 9 + self.binary_vector[2 - 1] * self.binary_vector[5 - 1] \
            - self.binary_vector[23 - 1] * self.binary_vector[14 - 1] \
            + self.binary_vector[24 - 1] * self.binary_vector[4 - 1] \
            - self.binary_vector[21 - 1] * self.binary_vector[10 - 1] \
            + self.binary_vector[36 - 1] * self.binary_vector[15 - 1] \
            - self.binary_vector[11 - 1] * self.binary_vector[26 - 1] \
            + self.binary_vector[16 - 1] * self.binary_vector[17 - 1] \
            + self.binary_vector[3 - 1] * self.binary_vector[33 - 1] \
            + self.binary_vector[28 - 1] * self.binary_vector[19 - 1] \
            + self.binary_vector[12 - 1] * self.binary_vector[34 - 1] \
            - self.binary_vector[31 - 1] * self.binary_vector[32 - 1] \
            - self.binary_vector[22 - 1] * self.binary_vector[25 - 1] \
            + self.binary_vector[35 - 1] * self.binary_vector[27 - 1] \
            - self.binary_vector[29 - 1] * self.binary_vector[7 - 1] \
            + self.binary_vector[8 - 1] * self.binary_vector[13 - 1] \
            - self.binary_vector[6 - 1] * self.binary_vector[9 - 1] \
            + self.binary_vector[18 - 1] * self.binary_vector[20 - 1] \
            - self.binary_vector[1 - 1] * self.binary_vector[30 - 1] \
            + self.binary_vector[23 - 1] * self.binary_vector[4 - 1] \
            + self.binary_vector[21 - 1] * self.binary_vector[15 - 1] \
            + self.binary_vector[26 - 1] * self.binary_vector[16 - 1] \
            + self.binary_vector[31 - 1] * self.binary_vector[12 - 1] \
            + self.binary_vector[25 - 1] * self.binary_vector[19 - 1] \
            + self.binary_vector[7 - 1] * self.binary_vector[8 - 1] \
            + self.binary_vector[9 - 1] * self.binary_vector[18 - 1] \
            + self.binary_vector[1 - 1] * self.binary_vector[33 - 1]
        self.fitness = fitness

    def __eq__(self, chromosome):
        return False

    def __lt__(self, chromosome):
        return self.fitness < chromosome.fitness or self.generation - chromosome.generation < 0

    def __gt__(self, chromosome):
        return self.fitness > chromosome.fitness or self.generation - chromosome.generation > 0
