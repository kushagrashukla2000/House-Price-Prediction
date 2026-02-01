from plotter import Plotter

if __name__ == "__main__":
    heat_map = Plotter(type="heatmap")
    heat_map.plot()
    bar_graph = Plotter()
    bar_graph.plot()
    bar_graph.plot_by_category()
    bar_graph.clean()
    bar_graph.label()
    bar_graph.split()
    bar_graph.train()
    bar_graph.train(algo="random forest")
    bar_graph.train(algo="linear regression")