# StringGP

This is a Genetic Algorithms Model written in Python for the purposes of cracking password vault like challenges. A challenge where you're provided a file with a complicated set if statements which can only be passed when the correct password is entered.

## Example

Here was a file which I had recieved during a HackTheBox hacking compitition
```python
import sys
password = input('Use the correct spell to exorcise the curse: ')
if len(password) != 16:
    print('[-] This is not the correct spell!\n')
    sys.exit(0)
if ord(password[0]) != 112 and 104 != ord(password[3]) and password[10] != chr(95) and 110 != ord(password[5]) and ord(password[6]) ^ ord(password[10]) != 0 and password[12] != chr(115) and ord(password[8]) != (ord(password[7]) - ord(password[0])) + 49 and (ord(password[0]) - ord(password[1])) + 125 != ord(password[2]) and password[14] != chr(101) and ord(password[1]) - 9 != ord(password[0]) and password[9] != chr(118) and password[11] != chr(49) and ord(password[7]) - ord(password[0]) != 2 and str(0) != password[4] and ord(password[13]) != ord(password[6]) or password[15] != 'Z'.lower():
    print('[-] This is not the correct spell!\n')
    sys.exit(0)
else:
    print(f'''This spell will exorcise the curses: HTB{{{password}}}''')
```

The expected solution for a challenge like this is to slowly go through each statements and figure out which string would make the program pass. Using this tool, the next step is to seprate the different statments apart and then have each failing statement be a reduction of score. We're also going to turn this code into a function that return a score based on the number of statements passed.
```python
def check_password(password):
  score = 50
  try:
    if len(password) != 16:
      return 0
    if ord(password[0]) != 112: score -= 2
    if 104 != ord(password[3]): score -= 2
    if password[10] != chr(95): score -=2
    if 110 != ord(password[5]): score -= 2
    if ord(password[6]) ^ ord(password[10]) != 0: score -=2
    if password[12] != chr(115): score -=2
    if ord(password[8]) != (ord(password[7]) - ord(password[0])) + 49: score -=2
    if (ord(password[0]) - ord(password[1])) + 125 != ord(password[2]): score -= 2
    if password[14] != chr(101):score -= 2
    if ord(password[1]) - 9 != ord(password[0]): score -= 2
    if password[9] != chr(118): score -= 2
    if password[11] != chr(49): score -= 2
    if ord(password[7]) - ord(password[0]) != 2: score -= 2
    if str(0) != password[4]: score -= 2
    if ord(password[13]) != ord(password[6]) or password[15] != 'Z'.lower(): score -= 2
  except Exception:
    score = 0

  return score
```

We now need to configure the StringGP to be able to solve this file. The most important fields are:
 - programMaxLength, programMinLength (min and max length of the password being solved)
 - fitnessThreshold (the score the password needs to hit before the program stops running)
 - function (the function which accepts a password and returns a score)
 - characterSet (Can the password contain letters, numbers, special characters)

Here's a configuration for the file above:

```python
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
```

We then just need to run the file
![stringgp-demo](https://github.com/loganmacdougall/StringGP/blob/main/Stringgp-demo.gif)


## Setup

To install this into your environment, do the following steps. This is also the required setup to run the example files

```
(.env) $ git clone https://github.com/loganmacdougall/StringGP.git
(.env) $ cd StringGP
(.env) $ pip install -r requirements.txt
(.env) $ pip install -e stringgp/ # installing stringgp folder
```
