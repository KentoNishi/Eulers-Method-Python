import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from math import *


class EulerCalculator:
    __quirkDict = dict()

    def __preprocess(self, inputString):
        if len(self.__quirkDict) == 0:
            with open("quirks.txt", "r") as fin:
                quirks = fin.readlines()
            for quirk in quirks[:-1]:
                original, final = tuple(quirk.split(", "))
                final = final[:-1]
                self.__quirkDict[original] = final
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
        if abs(stepSize) < pow(10, -4):
            raise ValueError("Step size is too small")
        derivativeFunction = self.__getFunction(derivative)
        currentValue = startY
        data = []
        while abs(startX - endX) >= pow(10, -4):
            data.append(
                [startX, currentValue,]
            )
            startX += stepSize
            currentValue += stepSize * derivativeFunction(startX, currentValue)
        return data

    def print(self, data):
        print(tabulate(data, headers=["x", "y"]))

    def graph(self, data):
        x, y = np.array(data).T
        plt.plot(x, y, "-o")
        plt.show()
