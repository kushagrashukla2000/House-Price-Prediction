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