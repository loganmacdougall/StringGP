from dataclasses import dataclass, field
from enum import Enum
import math
import sys
from typing import Callable
import string
import src.DataHelper as dp


@dataclass(kw_only=True)
class ParametersStringLGP:
    numOfGenerations: int = -1
    populationSize: int = 100
    programMaxLength: int = 64
    programMinLength: int = 0
    fitnessThreshold: int | float
    mutationRate: float = 0.4
    populationKeepPercentage: float = 0.8
    maximizeFitness: bool = True
    useMatrices: bool = True
    populationKeepAmount: int = field(init=False)
    executableFString: str = None
    function: Callable[[str], int] = None
    characterSet: str = string.printable
    knownCharacters: str = None
    replaceCharacter: chr = None
    confidenceThreshold: float = 0.9,
    fancyPrint: bool = True

    def _post_init(self):
        if (self.executableFString is None and self.function is None):
            raise Exception(
                "You must include either \"executableFString\" or \"function\".")

        self.populationKeepAmount = math.floor(
            self.populationKeepPercentage * self.populationSize)
        if self.knownCharacters is not None:
            self.programMinLength = max(
                self.programMinLength, len(self.knownCharacters))

    def __post_init__(self):
        print("Configuring Parameters: Start")
        self._post_init()
        print("Configuring Parameters: Complete")
