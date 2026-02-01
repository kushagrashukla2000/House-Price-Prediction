import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from housePricePrediction import HousePrice

class HeatMap(HousePrice):
    def __init__(self) -> None:
        super().__init__()
        self.numerical_dataset = self.dataset.select_dtypes(include=['int64', 'float64'])

    def plot(self) -> None:    
        plt.figure(figsize=(12, 6))
        sns.heatmap(self.numerical_dataset.corr(),
            cmap='BrBG',
            fmt='.2f',
            linewidths=2,
            annot=True)
        plt.title("Correlation Heatmap of Numerical Features")
        plt.tight_layout()
        plt.savefig("Graphs/correlation_heatmap.png")
        print("Heatmap saved as correlation_heatmap.png in Graphs")