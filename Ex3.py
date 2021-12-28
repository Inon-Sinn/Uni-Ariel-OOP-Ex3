from src.Graph_Gui import GUI
from src.Graph_Algo import GraphAlgo
import sys


def main(jsonFileName):
    algo = GraphAlgo()
    algo.load_from_json("data/{}".format(jsonFileName))
    algo.plot_graph()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main("A0.json")
    else:
        main(sys.argv[1])
