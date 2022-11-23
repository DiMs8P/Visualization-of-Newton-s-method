import numpy as np

def line(x,y, a, b, c):
    return a*x + b*y - c

def circle(x,y, a, b, r):
    return (x - a) ** 2 + (y - b) ** 2 - r ** 2

def sin(x,y, amplitude, frequency):
    return np.sin(frequency * x) + amplitude