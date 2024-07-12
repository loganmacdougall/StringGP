import random
import shlex
import subprocess
import numpy as np
from src.ParametersLGP import ParametersStringLGP


class ProgramLGP:
    def __init__(self, parameters: ParametersStringLGP, string: str = ""):
        self.parameters = parameters
        self.fitness = None
        self.proc = None
        self.string = string
        self.executedOnGeneration = -1

    def randomize(self):
        length = random.randint(
            self.parameters.programMinLength, self.parameters.programMaxLength)
        self.string = ''.join(random.choice(
            self.parameters.characterSet) for _ in range(length))
        self.fitness = None

    def setString(self, string: str):
        self.string = string

    def execute(self):
        if (self.fitness == None):
            self.proc = subprocess.Popen(
                self.parameters.executableFString.format(shlex.quote(self.string.rstrip("\x00"))),
                shell=True)

    def wait(self):
        if (self.fitness == None):
            self.proc.wait()
            self.fitness = int(self.proc.returncode)

    def execute_directly(self):
        if (self.fitness == None):
            self.fitness = self.parameters.function(self.string)

    def mutate(self, confidence: list = None, ordBest: np.array = None):
        mutRate = self.parameters.mutationRate
        if (confidence is None):
            self.string = ''.join(random.choice(self.parameters.characterSet)
                                  if random.random() < mutRate else c for c in self.string)
        else:
            confidenceThresh = self.parameters.confidenceThreshold
            self.string = ''.join(chr(ordBest[i]) if confidence[i] > confidenceThresh else (random.choice(self.parameters.characterSet)
                                  if random.random() < mutRate else c) for i, c in enumerate(self.string))

        charsToSubtract = len(self.string) - self.parameters.programMinLength
        charsToAdd = self.parameters.programMaxLength - len(self.string)
        if (charsToAdd > 0 and random.random() < mutRate / 4):
            self.string += ''.join(random.choices(self.parameters.characterSet,
                                   k=random.randint(0, charsToAdd)))
        elif (len(self.string) > self.parameters.programMinLength and random.random() < mutRate / 3):
            self.string = self.string[:random.randint(-charsToSubtract, 0)]
        self.fitness = None

    def stamp(self):
        stamp = self.parameters.knownCharacters
        replace = self.parameters.replaceCharacter
        max_copy_index = min(len(self.string), len(stamp))
        stamped_string = ''.join(
            self.string[i] if stamp[i] == replace else stamp[i] for i in range(max_copy_index)
        )
        self.string = stamped_string + self.string[max_copy_index:]

    @staticmethod
    def getCrossbreed(parameters: ParametersStringLGP, input1: str, input2: str):
        newStr1: str
        newStr2: str

        l = min(len(input1), len(input2))
        rl = random.randint(0, l)
        c = random.randint(0, l - rl)

        newStr = input1[:c] + input2[c:c+rl] + input1[c+rl:]

        return ProgramLGP(parameters, newStr)

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.__str__()
