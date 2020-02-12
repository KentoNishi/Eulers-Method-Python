import euler
import math


class Derivative:
    def evaluate(self, x, y):
        return x - 2 * y * math.sin(x)


calc = euler.EulerCalculator()
points = calc.evaluate(Derivative(), 0, 20, 2, stepSize=0.1)
calc.graph(points)
