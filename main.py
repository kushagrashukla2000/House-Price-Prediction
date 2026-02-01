from heatmap import HeatMap
from bargraph import BarGraph

if __name__ == "__main__":
    heat_map = HeatMap()
    heat_map.plot()
    bar_graph = BarGraph()
    bar_graph.plot()
    bar_graph.plot_by_category()