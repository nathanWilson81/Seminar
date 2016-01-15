import numpy

from deap import gp
from deap import algorithms
from deap import tools
from deap import base
from deap import creator

pset = gp.PrimitiveTree("MAIN", 1)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)


def main():
	pop = toolbox.population(n=100)



if __name__ == "__main__":
    main()
