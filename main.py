from plotter import Plotter

if __name__ == "__main__":
    heat_map = Plotter(type="heatmap")
    heat_map.plot()
    bar_graph = Plotter()
    bar_graph.plot()
    bar_graph.plot_by_category()
    bar_graph.clean()