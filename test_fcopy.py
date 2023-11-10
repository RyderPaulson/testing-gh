import fcopy
with open("data\input1.txt") as inputFile:
    fcopy.fcopy(inputFile)

def testCopy():
    with open("data\input1.txt") as inputFile:
        with open("data\output1.txt") as outputFile:
            while readline(inputFile) and realine(outputFile):
                i = inputFile.readline()
                o = outputFile.readline()
                if i != o:
                    return False
    return True

print(testCopy)