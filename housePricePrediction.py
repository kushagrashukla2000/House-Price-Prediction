import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("data/HousePricePrediction.xlsx")

print(dataset.head(5))