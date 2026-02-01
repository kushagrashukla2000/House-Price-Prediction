import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from housePricePrediction import HousePrice

class BarGraph(HousePrice):
    def __init__(self) -> None:
        super().__init__()
        self.unique_values = []
        for col in self.categorical_cols:
            self.unique_values.append(self.dataset[col].unique().size)
    
    def plot(self) -> None:
        plt.figure(figsize=(10,6))
        plt.title('No. Unique values of Categorical Features')
        plt.xticks(rotation=90)
        sns.barplot(x=self.categorical_cols,y=self.unique_values)
        plt.savefig("Graphs/correlation_bargraph.png")
        print("Bar Graph saved as correlation_bargraph.png in Graphs")

    def plot_by_category(self) -> None:
        plt.figure(figsize=(18, 36))
        plt.title('Categorical Features: Distribution')
        plt.xticks(rotation=90)
        index = 1

        for col in self.categorical_cols:
            y = self.dataset[col].value_counts()
            plt.subplot((len(self.categorical_cols) + 3) // 4, 4, index) # dynamic rows
            sns.barplot(x=list(y.index), y=y)
            plt.title(col)
            plt.xticks(rotation=90)
            plt.tight_layout(pad=3.0)  # spacing between subplots
            index += 1
        plt.savefig("Graphs/correlation_bargraph_by_category.png")
        print("Bar Graph saved as correlation_bargraph_by_category.png in Graphs")
