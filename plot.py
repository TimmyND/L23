import matplotlib.pyplot as plt
import math

def display_plot():
    X = [x/10 for x in range(100)]
    plt.plot(X, [math.sin(x) for x in X])
    plt.show()

display_plot()
