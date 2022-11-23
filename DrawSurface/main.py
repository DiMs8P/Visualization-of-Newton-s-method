import numpy as np
import matplotlib.pyplot as plt
import Application.drawler as drawler
import Application.functions as fu

drawler.circle(2, (0, 0))
drawler.circle(2, (2, 2))

drawler.gradient_background([
    lambda x, y : fu.circle(x,y, 0, 0, 2),
    lambda x, y : fu.circle(x,y, 2, 2, 2),
])
drawler.trajectory("Input/Nyuton.txt")
plt.show()
