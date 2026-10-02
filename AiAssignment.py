"""Entry point for the evolutionary route optimization project."""

import matplotlib.pyplot as plt
import numpy as np

import Datahandler as Dh
import EvolutionaryOptimization as Eo


# Optimization parameters
NUM_GENERATIONS = 1000
POPULATION_SIZE = 500
MUTATION_RATE = 0.2
DATA_FILE = "training_dataset.txt"


def optimize_evolutionarily(num_generations, population_size, mutation_rate, data):
    """Run the evolutionary optimization process."""
    matrix = Dh.createCostMatrix(data)
    population = Eo.createFirstGeneration(data, population_size, matrix)

    best_solution = Eo.findBestSolution(population)
    best_costs = []

    for generation in range(num_generations):
        population = Eo.createGeneration(
            population, mutation_rate, matrix, elitism=True
        )

        local_best = Eo.findBestSolution(population)
        if local_best.cost < best_solution.cost:
            best_solution = local_best

        best_costs.append(local_best.cost)

        print(f"{generation + 1}. generation --> cost --> {local_best.cost:.2f}")

    return population, best_costs, best_solution


def draw_cost_generation(costs):
    """Plot the best route cost for each generation."""
    x_values = np.arange(1, len(costs) + 1)

    plt.figure()
    plt.plot(x_values, costs)
    plt.title("Route Cost through Generations")
    plt.xlabel("Generations")
    plt.ylabel("Cost")
    plt.tight_layout()
    plt.show()


def draw_path(solution):
    """Plot the coordinates of the best route."""
    x_values = [node.x for node in solution.chromosome]
    y_values = [node.y for node in solution.chromosome]

    plt.figure()
    plt.scatter(x_values, y_values)
    plt.plot(x_values, y_values, "--", lw=2)
    plt.title("Best Route")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.show()


def main():
    data = Dh.importDataFromFile(DATA_FILE)

    _, costs, best_solution = optimize_evolutionarily(
        num_generations=NUM_GENERATIONS,
        population_size=POPULATION_SIZE,
        mutation_rate=MUTATION_RATE,
        data=data,
    )

    print("\nBest solution node order:", best_solution.chromosome_ids)
    print(f"Best solution cost: {best_solution.cost:.2f}")

    draw_cost_generation(costs)
    draw_path(best_solution)


if __name__ == "__main__":
    main()
