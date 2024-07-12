import src.ParametersLGP as pLGP
from src.StringRunner import FindString
import string
from puzzle_vault import check_password

charset = string.ascii_letters

# Parameters
parameters = pLGP.ParametersStringLGP(
    populationSize=200,
    programMaxLength=25,
    programMinLength=25,
    numOfGenerations=-1,
    fitnessThreshold=49.5,
    mutationRate=0.4,
    function=check_password,
    characterSet=charset,
    maximizeFitness=True,
    confidenceThreshold=0.6,
    knownCharacters="XXXXXXXXXXXXXXXXXXXXXault",
    replaceCharacter='X'
)

FindString(parameters, False)
