import random
import numpy as np
from deap import gp
from deap import algorithms
from deap import tools
from deap import base
from deap import creator

def drawForward():
    return "Forward"

def turnRight():
    return "Right"

def home():
    return "Home"

pset = gp.PrimitiveSet("MAIN", 0)
#pr = gp.Primitive('forw', int, int)
pset.addEphemeralConstant("distance", lambda: random.randrange(1, 40))
pset.addPrimitive(drawForward(),2,'forward')
#pset.addPrimitive(turnRight(), 1,'right')
#pset.addTerminal(home())
pset.addEphemeralConstant("rand90", lambda: random.randrange(1, 360))


#creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

#toolbox = base.Toolbox()
#toolbox.register("expr", gp.genFull, pset=pset, min_=0, max_=1)
#toolbox.register(
#    "individual", tools.initRepeat, creator.Individual, toolbox.expr)


def main():
    # random.seed(3)
    expr = gp.genHalfAndHalf(pset=pset, min_=1, max_=2)
    tree = gp.PrimitiveTree(expr)
    print(tree)

if __name__ == "__main__":
    main()
