import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class HousePrice():
    def __init__(self) -> None:
        self.dataset = pd.read_excel("data/HousePricePrediction.xlsx")
        self.categorical_cols = self.dataset.select_dtypes(include=['object']).columns
        self.integer_cols = self.dataset.select_dtypes(include=['int64']).columns
        self.float_cols = self.dataset.select_dtypes(include=['float64']).columns

    def __str__(self) -> str:
        return (
            "Categorical variables:" + str(len(self.categorical_cols)) + "\n"
            "Integer variables:" + str(len(self.integer_cols)) + "\n"
            "Float variables:" + str(len(self.float64)) + "\n"
        )