filename = "step_3.txt"

def basicCalculator(request):
    operator = request[0]
    parameterA = int(request[1])
    parameterB = int(request[2])

    if (operator == "x"):
        return parameterA * parameterB
    elif (operator == "+"):
        return parameterA + parameterB
    elif (operator == "-"):
        return parameterA - parameterB
    elif (operator == "/"):
        return parameterA / parameterB
    elif (operator == "^"):
        return parameterA ** parameterB

def parseLine(line):
    instruction = content[line - 1]
    if instruction in usedInstructions:
        print("instruction: ", instruction, ", line: ", line)
        # print(usedInstructions)
    else:
        usedInstructions.add(instruction)
        print("instruction: ", instruction, ", line: ", line)
        splitInstruction = instruction.split(' ')
        action = splitInstruction[0]

        if splitInstruction[0] == "calc":
            print(basicCalculator(splitInstruction[1:]))

        elif splitInstruction[0] == "goto":
            goToInstruction = splitInstruction[1:]
            if goToInstruction[0] == "calc":
                parseLine(round(basicCalculator(goToInstruction[1:])))
            elif len(goToInstruction) == 1:
                parseLine(int(goToInstruction[0]))

        elif action == "remove":
            if len(content) >= splitInstruction:
                del content[splitInstruction[1] - 1]
                parseLine(splitInstruction[1])

        elif splitInstruction[0] == "replace":
            linesToSwap = splitInstruction[1:]
            if len(content) >= max(linesToSwap):
                content[linesToSwap[0] - 1], content[linesToSwap[1] - 1] = content[linesToSwap[1] - 1], content[linesToSwap[0] - 1]
 
def readLines(content):
    for line in content:
        parseLine(line)

with open(filename) as f:
    content = f.read().splitlines()

usedInstructions = set()
parseLine(1)

