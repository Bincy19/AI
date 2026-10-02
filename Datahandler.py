"""Functions for loading route data and building a distance matrix."""

import math

import Chromosome as Ch


def importDataFromFile(file_path):
    """Read ID/X/Y coordinates from a whitespace-separated text file."""
    data_list = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            values = line.strip().split()
            if not values:
                continue
            if len(values) != 3:
                raise ValueError(
                    f"Invalid data on line {line_number}: expected 3 values."
                )

            node_id, x, y = values
            data_list.append(Ch.Node(id=node_id, x=x, y=y))

    if not data_list:
        raise ValueError("The dataset is empty.")

    return data_list


def createCostMatrix(nodes):
    """Create an NxN matrix containing Euclidean distances between nodes."""
    number_of_nodes = len(nodes)
    matrix = [[0.0 for _ in range(number_of_nodes)] for _ in range(number_of_nodes)]

    for i, node_a in enumerate(nodes):
        for j, node_b in enumerate(nodes):
            matrix[i][j] = math.hypot(node_a.x - node_b.x, node_a.y - node_b.y)

    return matrix
