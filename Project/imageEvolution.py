import random
import numpy as np
from turtle import *
from deap import gp
from deap import algorithms
from deap import tools
from deap import base
from deap import creator


def drawForward(distance):
    return "forward(" + str(distance) + ")"


def turnRight(degrees):
    return "right(" + str(degrees) + ")"


def turnLeft(degrees):
    return "left(" + str(degrees) + ")"


def returnToHome():
    return "home()"

pset = gp.PrimitiveSet("MAIN", 0)
pset.addPrimitive(forward, 2)
pset.addPrimitive(right, 2)
pset.addPrimitive(left, 2)
pset.addPrimitive(home, 1)
pset.addEphemeralConstant("rand90", lambda: random.randrange(1, 360))


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset=pset, min_=0, max_=1)
toolbox.register(
    "individual", tools.initRepeat, creator.Individual, toolbox.expr)


def main():
    # random.seed(3)
    # setup()
    expr = gp.genHalfAndHalf(pset=pset, min_=1, max_=2)
    tree = gp.PrimitiveTree(expr)
    print(tree)

if __name__ == "__main__":
    main()
