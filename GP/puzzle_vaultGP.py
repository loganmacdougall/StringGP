import src.ParametersLGP as pLGP
from src.StringRunner import FindString
import string

charset = string.ascii_letters + string.digits + string.punctuation

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
    confidenceThreshold=0.5,
    knownCharacters="XXXXXXXXXXXXXXXXXXXXXault",
    replaceCharacter='X'
)

FindString(parameters, False)
