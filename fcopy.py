def fcopy(inputFile):
    with open("data\output1.txt", 'w') as outputFile:
        for l in inputFile:
            outputFile.write(l)