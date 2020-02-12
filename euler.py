import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


class EulerCalculator:
    def evaluate(self, derivative, startX, startY, endX, **args):
        stepSize = args["stepSize"] if "stepSize" in args else 0.5
        currentValue = startY
        data = []
        while startX <= endX:
            data.append(
                [startX, currentValue,]
            )
            startX += stepSize
            currentValue += stepSize * derivative.evaluate(startX, currentValue)
        return data

    def graph(self, data):
        x, y = np.array(data).T
        plt.plot(x, y, "-o")
        print(tabulate(data, headers=["x", "y"]))
        plt.show()
