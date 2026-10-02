"""Genetic Algorithm operators for route optimization."""

import random

import Chromosome as ch


def create_random_list(nodes):
    """Create a random route while keeping the first node as start/end."""
    if len(nodes) < 2:
        raise ValueError("At least two nodes are required.")

    head = nodes[0]
    tail = random.sample(nodes[1:], len(nodes) - 1)
    return [head, *tail, head]


def createFirstGeneration(data, populationSize, matrix):
    """Create the initial population of random chromosomes."""
    if populationSize < 2:
        raise ValueError("Population size must be at least 2.")

    return [
        ch.Chromosome(create_random_list(data), matrix)
        for _ in range(populationSize)
    ]


def selection(population):
    """Tournament selection: choose the best of four random candidates."""
    if len(population) < 4:
        raise ValueError("Selection requires a population of at least 4.")

    candidates = random.sample(population, 4)
    return min(candidates, key=lambda chromosome: chromosome.cost)


def crossover(p_1, p_2):
    """Perform an order-preserving two-point crossover."""
    length = len(p_1.chromosome)
    if length != len(p_2.chromosome):
        raise ValueError("Parents must contain the same number of nodes.")
    if length < 4:
        raise ValueError("Crossover requires at least four route positions.")

    point_1, point_2 = sorted(random.sample(range(1, length - 1), 2))

    parent_1 = p_1.chromosome
    parent_2 = p_2.chromosome

    child_1_middle = parent_1[point_1:point_2]
    child_2_middle = parent_2[point_1:point_2]

    child_1_remaining = [
        node for node in parent_2[1:-1] if node not in child_1_middle
    ]
    child_2_remaining = [
        node for node in parent_1[1:-1] if node not in child_2_middle
    ]

    child_1_body = child_1_remaining[:point_1] + child_1_middle + child_1_remaining[point_1:]
    child_2_body = child_2_remaining[:point_1] + child_2_middle + child_2_remaining[point_1:]

    start = parent_1[0]
    return [start, *child_1_body, start], [start, *child_2_body, start]


def mutation(chromosome):
    """Swap two non-start/end nodes in a route."""
    if len(chromosome) < 4:
        return chromosome

    index_1, index_2 = random.sample(range(1, len(chromosome) - 1), 2)
    chromosome[index_1], chromosome[index_2] = chromosome[index_2], chromosome[index_1]
    return chromosome


def findBestSolution(generation):
    """Return the chromosome with the lowest route cost."""
    if not generation:
        raise ValueError("Generation cannot be empty.")
    return min(generation, key=lambda chromosome: chromosome.cost)


def createGeneration(previous_generation, mutation_rate, matrix, elitism=True):
    """Create a new generation using selection, crossover and mutation."""
    if not previous_generation:
        raise ValueError("Previous generation cannot be empty.")
    if not 0 <= mutation_rate <= 1:
        raise ValueError("Mutation rate must be between 0 and 1.")

    new_generation = []

    if elitism:
        new_generation.append(findBestSolution(previous_generation))

    target_size = len(previous_generation)
    while len(new_generation) < target_size:
        parent_1 = selection(previous_generation)
        parent_2 = selection(previous_generation)

        child_1_nodes, child_2_nodes = crossover(parent_1, parent_2)

        if random.random() < mutation_rate:
            child_1_nodes = mutation(child_1_nodes)
        if random.random() < mutation_rate:
            child_2_nodes = mutation(child_2_nodes)

        new_generation.append(ch.Chromosome(child_1_nodes, matrix))
        if len(new_generation) < target_size:
            new_generation.append(ch.Chromosome(child_2_nodes, matrix))

    return new_generation
