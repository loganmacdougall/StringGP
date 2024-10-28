import numpy as np
from .ParametersLGP import ParametersStringLGP
from .BaseLGP import StringLGP


def FindString(parameters: ParametersStringLGP, graph=True):
    classifierLGP = StringLGP(parameters)
    classifierLGP.train()

    bestProg = classifierLGP.bestProgram()

    print(f"Elapsed Time: {classifierLGP.elapsed_time:.03f} secs\n")
    print("Best String: ")
    print(bestProg.string)
    print(f'String got a fitness of {bestProg.fitness}.')

    if (graph):
        classifierLGP.graphResult()
