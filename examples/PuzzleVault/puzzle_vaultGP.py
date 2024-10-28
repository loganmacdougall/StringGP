import stringgp.ParametersLGP as pLGP
from stringgp.StringRunner import FindString
import string

charset = string.ascii_letters

# Parameters
parameters = pLGP.ParametersStringLGP(
    populationSize=200,
    programMaxLength=25,
    programMinLength=25,
    numOfGenerations=-1,
    fitnessThreshold=49.5,
    mutationRate=0.4,
    executableFString="node GP/puzzle_vault.js {}",
    characterSet=charset,
    maximizeFitness=True,
    confidenceThreshold=0.6,
    knownCharacters="XXXXXXXXXXXXXXXXXXXXXault",
    replaceCharacter='X'
)

if __name__ == "__main__":
    FindString(parameters, False)
