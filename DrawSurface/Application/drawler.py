import matplotlib.pyplot as plt
import numpy as np
import config as co

eps = 0.000_1

def circle(radius, startpoint):
    fig = plt.gcf()
    ax = fig.gca()
    circle1 = plt.Circle(startpoint, radius, facecolor='none', edgecolor='r')
    plt.xlim(co.Xborder[0], co.Xborder[1]), plt.ylim(co.Yborder[0], co.Yborder[1])
    ax.add_artist(circle1)

def sin(amplitude, frequency):
    x = np.arange(co.Xborder[0], co.Xborder[1], 0.01)  # start,stop,step
    y = amplitude * np.sin(x * frequency)
    plt.plot(x, y)

def line(startpoint, endpoint):
    if abs(startpoint[0] - endpoint[0]) < eps:
        line_vertical((startpoint[0] + endpoint[0]) /2)
        return
    tg = (endpoint[1] - startpoint[1]) / (endpoint[0] - startpoint[0])
    b = startpoint[1] - startpoint[0] * tg
    x1 = (co.Xborder[0], co.Xborder[1])
    y1 = (co.Xborder[0] * tg + b, co.Xborder[1] * tg + b)
    plt.xlim(co.Xborder[0], co.Xborder[1]), plt.ylim(co.Yborder[0], co.Yborder[1])
    plt.plot(x1, y1)

def line_vertical(x):
    plt.axvline(x=x)

def line_segment(startpoint, endpoint):
    x1 = (startpoint[0], endpoint[0])
    y1 = (startpoint[1], endpoint[1])
    plt.xlim(co.Xborder), plt.ylim(co.Yborder)
    plt.plot(x1, y1)

def gradient_background(f):
    mas = [[gradient(i, j, f) for j in range(0, co.plotLengthX)] for i in range(0, co.plotLengthY)]
    plt.imshow(mas,
               extent=(co.Xborder[0], co.Xborder[1], co.Yborder[1], co.Yborder[0]),
               cmap='gray',
               alpha = 0.6)

def gradient(i, j, f):
    sum = 0
    for func in f:
        x, y = get_xy_from_ij(i,j)
        z = func(x,y)
        sum += z**2

    return sum ** 0.5

def get_xy_from_ij(i,j):
    xLen = co.Xborder[1] - co.Xborder[0]
    yLen = co.Yborder[1] - co.Yborder[0]

    plotLengthX = co.plotLengthX
    plotLengthY = co.plotLengthY

    x = co.Xborder[0] + (xLen / plotLengthX * j)
    y = co.Yborder[0] + (yLen / plotLengthY * i)

    return x,y

def trajectory(filePath):
    data = []
    with open("Input/Nyuton.txt") as f:
        for line in f:
            data.append([float(x) for x in line.replace(',', '.').split()])

    x = []
    y = []
    for pair in data:
        x.append(pair[0])
        y.append(pair[1])

    plt.plot(x, y, '-', color="blue")
