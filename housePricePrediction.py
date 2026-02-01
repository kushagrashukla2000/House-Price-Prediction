import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class HousePrice():
    def __init__(self) -> None:
        self.dataset = pd.read_excel("data/HousePricePrediction.xlsx")
        self.categorical_cols = self.dataset.select_dtypes(include=['object']).columns
        self.integer_cols = self.dataset.select_dtypes(include=['int64']).columns
        self.float_cols = self.dataset.select_dtypes(include=['float64']).columns
        self.df_final = None

    def __str__(self) -> str:
        return (
            "Categorical variables:" + str(len(self.categorical_cols)) + "\n"
            "Integer variables:" + str(len(self.integer_cols)) + "\n"
            "Float variables:" + str(len(self.float64)) + "\n"
        )
    
    def clean(self) -> None:
        self.dataset.drop(
            ['Id'],
            axis=1,
            inplace=True
        )
        self.dataset['SalePrice'] = self.dataset['SalePrice'].fillna(
            self.dataset['SalePrice'].mean()
        )
        self.dataset = self.dataset.dropna()
        null_values = list(self.dataset.isnull().sum().values)
        ideal_values = [0] * len(null_values)
        assert null_values == ideal_values, "Data Cleaning Failed"
    
    def label(self) -> None:
        s = (self.dataset.dtypes == 'object')
        object_cols = list(s[s].index)
        print("Categorical variables:")
        print(object_cols)
        print('No. of. categorical features: ', len(object_cols))
        OH_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        OH_cols = pd.DataFrame(OH_encoder.fit_transform(self.dataset[object_cols]))
        OH_cols.index = self.dataset.index
        OH_cols.columns = OH_encoder.get_feature_names_out()
        self.df_final = self.dataset.drop(object_cols, axis=1)
        self.df_final = pd.concat([self.df_final, OH_cols], axis=1)