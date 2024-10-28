from stringgp import ParametersLGP as pLGP
from stringgp.StringRunner import FindString
import string
from CallumCTF import is_challenge2_password

charset = string.ascii_lowercase

# Parameters
parameters = pLGP.ParametersStringLGP(
    populationSize=200,
    programMaxLength=26,
    programMinLength=26,
    numOfGenerations=-1,
    fitnessThreshold=149.5,
    mutationRate=0.4,
    function=is_challenge2_password,
    characterSet=charset,
    maximizeFitness=True,
    confidenceThreshold=0.9,
    knownCharacters="XXXXXXXXXXXXXXXXwhiteXXXXX",
    replaceCharacter='X'
)

if __name__ == "__main__":
    FindString(parameters, False)
