import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math


class EulerCalculator:
    __quirkDict = dict()

    def __preprocess(self, inputString):
        if len(self.__quirkDict) == 0:
            with open("quirks.txt", "r") as fin:
                quirks = fin.readlines()
            for quirk in quirks[:-1]:
                original, final = tuple(quirk.split(", "))
                final = final[:-1]
                self.__quirkDict["original"] = final
                inputString = inputString.replace(original, final)
        for quirk in self.__quirkDict.keys():
            inputString = inputString.replace(quirk, self.__quirkDict[quirk])
        return inputString

    def __getFunction(self, inputString):
        inputString = self.__preprocess(inputString)
        return lambda x, y: eval(inputString)

    def evaluate(self, **args):
        requiredArgs = ["derivative", "startX", "startY", "endX", "stepSize"]
        for arg in requiredArgs:
            if arg not in args:
                raise ValueError(arg + " is invalid")
        derivative = args["derivative"]
        startX = args["startX"]
        startY = args["startY"]
        endX = args["endX"]
        stepSize = args["stepSize"]
        derivativeFunction = self.__getFunction(derivative)
        currentValue = startY
        data = []
        while startX <= endX:
            data.append(
                [startX, currentValue,]
            )
            startX += stepSize
            currentValue += stepSize * derivativeFunction(startX, currentValue)
        return data

    def graph(self, data):
        x, y = np.array(data).T
        plt.plot(x, y, "-o")
        print(tabulate(data, headers=["x", "y"]))
        plt.show()
