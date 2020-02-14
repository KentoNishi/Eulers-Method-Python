import euler

calc = euler.EulerCalculator()
points = calc.evaluate(
    derivative="x-2*y*sin(x)", startX=0, startY=20, endX=2, stepSize=0.1
)
calc.graph(points)
