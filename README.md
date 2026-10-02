# Evolutionary Route Optimization

A Python implementation of a **Genetic Algorithm (Evolutionary Algorithm)** for finding a low-cost route through a set of two-dimensional locations.

The project was developed as an AI/optimization assignment. It represents each possible route as a chromosome and improves a population of routes over multiple generations using selection, crossover, mutation, and elitism.

## Project Objective

Given a set of locations represented by `(x, y)` coordinates, the program searches for a short route that:

- starts at the first location,
- visits every location,
- returns to the starting location, and
- minimizes the total Euclidean travel distance.

## How the Algorithm Works

1. **Dataset loading** – locations are read from `training_dataset.txt`.
2. **Cost matrix** – Euclidean distances between every pair of locations are calculated.
3. **Initial population** – random routes are generated.
4. **Fitness evaluation** – shorter routes receive better fitness.
5. **Tournament selection** – four candidates are sampled and the lowest-cost route is selected.
6. **Crossover** – two parent routes are combined to create new routes while preserving the route structure.
7. **Mutation** – two route positions are randomly swapped to maintain diversity.
8. **Elitism** – the best route from the previous generation is retained.
9. **Evolution** – the process repeats for the configured number of generations.
10. **Visualization** – the route cost over generations and the final route are plotted.

## Dataset

`training_dataset.txt` contains 20 locations. Each row has:

```text
ID X Y
```

Example:

```text
1 25.0 1050.0
2 450.0 950.0
3 480.0 1100.0
```

## Default Parameters

| Parameter | Value |
|---|---:|
| Generations | 1000 |
| Population size | 500 |
| Mutation rate | 0.2 (20%) |
| Locations | 20 |

The parameters can be changed at the top of `AiAssignment.py`.

## Project Structure

```text
AI/
├── AiAssignment.py                # Main program and visualizations
├── Chromosome.py                  # Node/chromosome classes and route cost
├── Datahandler.py                 # Dataset loading and distance matrix
├── EvolutionaryOptimization.py    # Genetic Algorithm operators
├── training_dataset.txt           # Location dataset
├── test.py                        # Basic project tests
├── requirements.txt               # Python dependencies
├── .gitignore                     # Files excluded from Git
└── README.md                      # Project documentation
```

## Requirements

- Python 3.9 or newer
- NumPy
- Matplotlib

## Installation

Clone the repository and enter the project directory:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI
```

Create and activate a virtual environment (recommended):

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python AiAssignment.py
```

The program prints the best cost found for each generation and opens two plots:

- route cost across generations
- the final best route on the coordinate plane

## Run Tests

```bash
python -m unittest test.py
```

## Notes

This repository contains a cleaned and generalized version of the original assignment implementation. Hard-coded assumptions about population size and the number of locations have been removed so that the algorithm can work with different population sizes and datasets.

## Technologies

- Python
- NumPy
- Matplotlib
- Genetic Algorithms / Evolutionary Optimization
- Euclidean distance

## Author

**Bincy Annamma Saji**
