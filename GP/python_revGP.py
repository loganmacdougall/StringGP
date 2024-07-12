import src.ParametersLGP as pLGP
from src.StringRunner import FindString
import string
from python_rev import check_password

charset = string.printable

# Parameters
parameters = pLGP.ParametersStringLGP(
    populationSize=200,
    programMaxLength=16,
    programMinLength=16,
    numOfGenerations=-1,
    fitnessThreshold=49.5,
    mutationRate=0.4,
    function=check_password,
    characterSet=charset,
    maximizeFitness=True,
    confidenceThreshold=0.6,
)

FindString(parameters, False)
