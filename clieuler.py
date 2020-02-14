from math import *

def quirkProcessing(istr):
    with open("equationquirks.txt", 'r') as fin:
        quirks = fin.readlines()
    for quirk in quirks[:-1]:
        original, final = tuple(quirk.split(', '))
        final = final[:-1]
        istr = istr.replace(original, final)
    return istr

def getFunction():
    fstr = input("dy/dx? ")
    fstr = quirkProcessing(fstr)
    return lambda x,y: eval(fstr)

def euler(f, deltax, ogx, ogy, finalx, show = 1):
    deltay = f(ogx, ogy) * deltax
    newy = ogy + deltay
    print(("%.3f\t%.5f\t%.5f\t%.5f" % (ogx, ogy, deltay, newy)) * show, end = '' * show)
    if show == 1: input()
    if abs(ogx + deltax - finalx) <= .000001:
        print('\n'*show, ogx+deltax, newy)
        return
    euler(f, deltax, ogx + deltax, newy, finalx, show)

def main():
    func = getFunction()
    dx = float(input("deltax? "))
    ogx = float(input("original x? "))
    ogy = float(input("original y? "))
    finalx = float(input("final x? "))
    show = int(input("Show work?(0/1) "))
    euler(func, dx, ogx, ogy, finalx, show)

if __name__ == "__main__":
    main()
