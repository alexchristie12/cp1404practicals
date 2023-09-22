"""Simulates a population of Gophers over time"""
import random
import matplotlib.pyplot as plt
import numpy as np

STARTING_POPULATION = 1000
STARTING_YEAR = 2023
FINISH_YEAR = 3033


def main():
    current_population = STARTING_POPULATION
    current_year = STARTING_YEAR
    years = np.zeros(FINISH_YEAR - STARTING_YEAR + 1)
    years[0] = STARTING_YEAR
    population = np.zeros(len(years))
    population[0] = STARTING_POPULATION
    i = 1
    while current_year < FINISH_YEAR:
        current_population = current_population + population_change(current_population)
        current_year += 1
        years[i] = current_year
        population[i] = current_population
        i += 1
    plt.plot(years, population)
    plt.show()


def population_born(current_population):
    return current_population * random.uniform(0.1, 0.2)


def population_deceased(current_population):
    return current_population * -1 * random.uniform(0.05, 0.25)


def population_change(current_population):
    return population_born(current_population) + population_deceased(current_population)


if __name__ == "__main__":
    main()
