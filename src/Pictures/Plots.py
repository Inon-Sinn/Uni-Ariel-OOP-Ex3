import numpy as np
import matplotlib.pyplot as plt

"""This file is used to make the plots seen in the Wiki of the Git hub project"""


def plotA1_G1Json():
    """Plot of the A1.json"""
    X = ['Load', 'Save', 'Shortest Path', 'Center', 'Tsp']
    python = [1, 3, 1, 4, 2]
    java = [157, 320, 0.245, 5.57, 7]
    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, python, 0.4, label='python')
    plt.bar(X_axis + 0.2, java, 0.4, label='Java')

    plt.xticks(X_axis, X)
    plt.xlabel("Algorithms")
    plt.ylabel("ms")
    plt.title("Runtime for each Algorithm")
    plt.legend()
    plt.show()


def plotA2_G2Json():
    """Plot of the A2.json"""
    X = ['Load', 'Save', 'Shortest Path', 'Center', 'Tsp']
    python = [1, 7, 0, 12, 3]
    java = [41, 11, 0.155, 11.75, 4.25]
    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, python, 0.4, label='python')
    plt.bar(X_axis + 0.2, java, 0.4, label='Java')

    plt.xticks(X_axis, X)
    plt.xlabel("Algorithms")
    plt.ylabel("ms")
    plt.title("Runtime for each Algorithm")
    plt.legend()
    plt.show()


def plotA5_G3Json():
    """Plot of the A5.json"""
    X = ['Load', 'Save', 'Shortest Path', 'Center', 'Tsp']
    python = [1, 5, 2, 36, 8]
    java = [13, 26, 0.435, 10.5, 20.5]
    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, python, 0.4, label='python')
    plt.bar(X_axis + 0.2, java, 0.4, label='Java')

    plt.xticks(X_axis, X)
    plt.xlabel("Algorithms")
    plt.ylabel("ms")
    plt.title("Runtime for each Algorithm")
    plt.legend()
    plt.show()


def plot1000NodesJson():
    """Plot of the 1000Nodes.json"""
    X = ['Load', 'Save', 'Shortest Path', 'Center', 'Tsp']
    python = [38, 196, 58, 33044, 313]
    java = [240, 210, 8.53, 6000, 176]
    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, python, 0.4, label='python')
    plt.bar(X_axis + 0.2, java, 0.4, label='Java')

    plt.xticks(X_axis, X)
    plt.xlabel("Algorithms")
    plt.ylabel("ms")
    plt.title("Runtime for each Algorithm")
    plt.legend()
    plt.show()


def plot10000NodesJson():
    """Plot of the 10000Nodes.json"""
    X = ['Load', 'Save', 'Shortest Path', 'Tsp']
    python = [421, 2098, 573, 4826]
    java = [892, 581, 337.4, 3600]
    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, python, 0.4, label='python')
    plt.bar(X_axis + 0.2, java, 0.4, label='Java')

    plt.xticks(X_axis, X)
    plt.xlabel("Algorithms")
    plt.ylabel("ms")
    plt.title("Runtime for each Algorithm")
    plt.legend()
    plt.show()


def plot100000NodesJson():
    """Plot of the 100000Nodes.json"""
    X = ['Load', 'Save', 'Shortest Path']
    python = [10.5, 45.3, 15.1]
    java = [6.8, 9.3, 45]
    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, python, 0.4, label='python')
    plt.bar(X_axis + 0.2, java, 0.4, label='Java')

    plt.xticks(X_axis, X)
    plt.xlabel("Algorithms")
    plt.ylabel("s")
    plt.title("Runtime for each Algorithm")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # plotA1_G1Json()
    # plotA2_G2Json()
    # plotA5_G3Json()
    # plot1000NodesJson()
    # plot10000NodesJson()
    plot100000NodesJson()
