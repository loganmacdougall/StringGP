from multiprocessing import Pool
import time
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from src.PopulationLGP import PopulationLGP
from src.ParametersLGP import ParametersStringLGP
from src.ProgramLGP import ProgramLGP


confidenceStr = " .:-=+*#%@"
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'


class StringLGP:
    def __init__(self, parameters: ParametersStringLGP):
        self.parameters = parameters

        self.calculated_generation = -1
        self.population = PopulationLGP(parameters)

        self.start_time = time.time()
        self.elapsed_time = 0
        # self.fitness_history = [self.getPopulationStats()]

        self.updateFitnesses()

    def updateFitnesses(self):
        if (self.population.generation != self.calculated_generation):
            if self.parameters.function is None:
                # Execute all the scripts
                for prog in self.population.programs:
                    if prog.fitness is None or self.forceRecalculateFitnesses:
                        prog.execute()
                # Wait for all the scripts to finish executing
                for prog in self.population.programs:
                    if prog.fitness is None or self.forceRecalculateFitnesses:
                        prog.wait()
            else:
                for prog in self.population.programs:
                    if prog.fitness is None or self.forceRecalculateFitnesses:
                        prog.execute_directly()
            # Sort the programs
            self.population.programs = sorted(
                self.population.programs, key=lambda x: x.fitness, reverse=self.parameters.maximizeFitness)

            self.calculated_generation = self.population.generation
            self.forceRecalculateFitnesses = False

    def getPrograms(self):
        self.updateFitnesses()
        return self.population.programs

    def getPopulationStats(self):
        programs = self.getPrograms()
        best = programs[0].fitness
        best_len = len(programs[0].instructions)
        worst = programs[-1].fitness
        worst_len = len(programs[-1].instructions)
        avg = sum((prog.fitness for prog in programs)) / len(programs)
        avg_len = sum((len(prog.instructions)
                      for prog in programs)) / len(programs)
        return (best, avg, worst, best_len, avg_len, worst_len)

    def bestFitness(self):
        return self.getPrograms()[0].fitness

    def bestProgram(self):
        return self.getPrograms()[0]

    def haveMetFitnessThreshold(self):
        topFitness = self.bestFitness()
        return (self.parameters.maximizeFitness and self.parameters.fitnessThreshold <= topFitness) \
            or (not self.parameters.maximizeFitness and self.parameters.fitnessThreshold >= topFitness)

    def train(self):
        def hitMaxGenerations(): return self.population.generation >= self.parameters.numOfGenerations and self.parameters.numOfGenerations > 0

        print("Training: Started")

        try:
            while not hitMaxGenerations() and not self.haveMetFitnessThreshold():
                self.population.nextGeneration()
                self.updateFitnesses()
                self.betweenGenerations()
        except KeyboardInterrupt:
            pass

        self.elapsed_time = time.time() - self.start_time

        print("Training: Completed")

        if self.haveMetFitnessThreshold():
            return True
        else:
            return False

    def betweenGenerations(self):
        # self.fitness_history.append(self.getPopulationStats())
        print(self.getProgressString())

    def graphResult(self):
        x = list(range(len(self.fitness_history)))

        plt.plot(x, [v[0] for v in self.fitness_history], 'g')  # plotting best
        # plotting average
        plt.plot(x, [v[1] for v in self.fitness_history], 'y')
        plt.plot(x, [v[2]
                 for v in self.fitness_history], 'r')  # plotting worst

        plt.legend(["best", "average", "worst"])

        plt.show()

    def getProgressString(self):
        s = f"\nCreated generation {self.population.generation} with best fitness {self.bestFitness()}.\n" + \
            "\tCurrent Best: ( {:<{}} )\n".format(self.bestProgram().string, self.parameters.programMaxLength) + \
            f"\tConfidence:     {''.join(confidenceStr[min(int(self.population.letterConfidence[i] / self.parameters.confidenceThreshold * len(confidenceStr)), len(confidenceStr)-1)] for i in range(self.parameters.programMaxLength))}\n"
        if (self.parameters.fancyPrint):
            return ((LINE_CLEAR + LINE_UP) * 5) + s
        return s
