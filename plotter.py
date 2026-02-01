from heatmap import HeatMap
from bargraph import BarGraph

class Plotter():
    def __new__(cls, type: str = "bar"):
        if type == "bar":
            return BarGraph()
        elif type == "heatmap":
            return HeatMap()
        print("Error: Invalid type passed defaulting to Bar Graph")
        return BarGraph()