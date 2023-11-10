def fcopy(myFile):
    with open("data\output1.txt", 'w') as outputFile:
        for l in myFile:
            outputFile.write(l)