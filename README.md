# 🏡 House Price Prediction

A Python‑based machine learning project to predict house prices using regression techniques and data visualization.

This repository contains scripts to preprocess data, train predictive models, visualize relationships between features and prices, and display results through graphs.

---

## 🔍 Project Overview

The goal of this project is to build a machine learning model that predicts house prices based on various features such as size, number of rooms, and other relevant attributes.

It demonstrates:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Regression modeling
- Data visualization

---

## 📂 Project Structure

```
House-Price-Prediction/
├── data/                        # Dataset files
├── bargraph.py                 # Script for bar graph visualization
├── heatmap.py                  # Script for correlation heatmap
├── housePricePrediction.py     # Core ML model logic
├── main.py                     # Main execution file
├── plotter.py                  # Plotting utilities
├── README.md
└── requirements.txt
```

---

## 🛠️ Features

- Data loading and preprocessing
- Correlation analysis using heatmaps
- Data distribution analysis using bar graphs
- House price prediction using regression models
- Easy‑to‑run Python scripts

---

## 📈 Workflow

1. Load dataset
2. Clean and preprocess data
3. Perform exploratory data analysis
4. Train regression model
5. Predict and visualize results

---

## 💻 Getting Started

### Prerequisites

- Python 3.7+
- Required libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit‑learn

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Installation

```bash
git clone https://github.com/kushagrashukla2000/House-Price-Prediction.git
cd House-Price-Prediction
```

---

### Usage

Run the main script:

```bash
python main.py
```

Or use in your project:

```bash
from plotter import Plotter

heat_map = Plotter(type="heatmap")
```

---

## 📊 Visualizations

- Heatmaps for feature correlation
- Bar graphs for data insights
- Prediction vs actual price plots

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Open a pull request

---
