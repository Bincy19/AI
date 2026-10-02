"""Data structures and cost calculation for route chromosomes."""


class Node:
    """A location represented by an ID and two-dimensional coordinates."""

    def __init__(self, id, x, y):
        self.x = float(x)
        self.y = float(y)
        self.id = int(id)

    def __repr__(self):
        return f"Node(id={self.id}, x={self.x}, y={self.y})"


class Chromosome:
    """A candidate route in the evolutionary optimization."""

    def __init__(self, nodes, matrix):
        self.chromosome = nodes
        self.chromosome_ids = [node.id for node in nodes]
        self.cost = calculateChrCost(self.chromosome_ids, matrix)
        self.fitness_value = 1 / self.cost if self.cost > 0 else float("inf")

    # Backward-compatible name used by the original assignment.
    @property
    def chromosomeIdes(self):
        return self.chromosome_ids


def calculateChrCost(route, matrix):
    """Calculate the total distance of a route using the cost matrix."""
    return sum(matrix[route[i] - 1][route[i + 1] - 1] for i in range(len(route) - 1))
