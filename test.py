"""Basic tests for the route optimization project."""

import unittest

import Chromosome as Ch
import Datahandler as Dh


class ProjectTests(unittest.TestCase):
    def test_dataset_loads(self):
        nodes = Dh.importDataFromFile("training_dataset.txt")
        self.assertEqual(len(nodes), 20)
        self.assertEqual(nodes[0].id, 1)
        self.assertEqual(nodes[-1].id, 20)

    def test_cost_matrix_shape(self):
        nodes = Dh.importDataFromFile("training_dataset.txt")
        matrix = Dh.createCostMatrix(nodes)
        self.assertEqual(len(matrix), 20)
        self.assertTrue(all(len(row) == 20 for row in matrix))

    def test_route_cost(self):
        nodes = Dh.importDataFromFile("training_dataset.txt")
        matrix = Dh.createCostMatrix(nodes)
        route = [nodes[0], nodes[1], nodes[0]]
        chromosome = Ch.Chromosome(route, matrix)
        self.assertGreater(chromosome.cost, 0)


if __name__ == "__main__":
    unittest.main()
