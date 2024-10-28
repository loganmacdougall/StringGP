import random
import numpy as np
from scipy import stats
from .ParametersLGP import ParametersStringLGP
from .ProgramLGP import ProgramLGP


class PopulationLGP:
    def __init__(self, parameters: ParametersStringLGP):
        self.parameters = parameters
        self.programs = [ProgramLGP(parameters)
                         for _ in range(parameters.populationSize)]

        self.generation = 0
        self.ordLetterMode = [0] * parameters.programMaxLength
        self.letterConfidence = [0] * parameters.programMaxLength
        for program in self.programs:
            program.randomize()
            if (self.parameters.knownCharacters is not None):
                program.stamp()

    def nextGeneration(self):
        best = self.programs[:self.parameters.populationKeepAmount]

        ordPrograms = np.array([[ord(s[i]) if i < len(s) else 0 for i in range(
            self.parameters.programMaxLength)] for s in [prog.string for prog in best]])
        self.ordLetterMode = [stats.mode(
            ordPrograms[:, i]).mode for i in range(self.parameters.programMaxLength)]
        self.letterConfidence = [np.count_nonzero(
            self.ordLetterMode[i] != 0 and self.ordLetterMode[i] == ordPrograms[:, i]) / len(best) for i in range(self.parameters.programMaxLength)]

        children_amount = self.parameters.populationSize - \
            self.parameters.populationKeepAmount
        children = []

        for _ in range(0, children_amount + 1):
            [prog1, prog2] = random.choices(best, k=2)
            children.append(prog1.getCrossbreed(
                prog1.parameters, prog1.string, prog2.string))

        for prog in children:
            prog.string = prog.string[:self.parameters.programMaxLength].ljust(
                self.parameters.programMaxLength, random.choice(self.parameters.characterSet))
            prog.mutate(self.letterConfidence, self.ordLetterMode)
            if (self.parameters.knownCharacters is not None):
                prog.stamp()

        gen = best + children

        self.programs = gen
        self.generation += 1

        return len(best)
