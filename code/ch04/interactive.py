import matplotlib as mpl
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


if __name__ == "__main__":
    mpl.use("MacOSX")
    
    x = np.linspace(-5, 2, 100)
    y1 = x**3 + 5*x**2 + 10
    y2 = 3*x**2 + 10*x
    y3 = 6*x + 10
    
    
    fig, ax = plt.subplots()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.plot(x, y2, color="red", label="y'(x)")
    ax.plot(x, y3, color="green", label = "y''(x)")
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()
