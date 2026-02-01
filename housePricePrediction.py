import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn import svm
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class HousePrice():
    def __init__(self) -> None:
        self.dataset = pd.read_excel("data/HousePricePrediction.xlsx")
        self.categorical_cols = self.dataset.select_dtypes(include=['object']).columns
        self.integer_cols = self.dataset.select_dtypes(include=['int64']).columns
        self.float_cols = self.dataset.select_dtypes(include=['float64']).columns
        self.df_final = None
        self.split_data = None

    def __str__(self) -> str:
        return (
            "Categorical variables:" + str(len(self.categorical_cols)) + "\n"
            "Integer variables:" + str(len(self.integer_cols)) + "\n"
            "Float variables:" + str(len(self.float64)) + "\n"
        )
    
    def clean(self) -> None:
        null_values = list(self.dataset.isnull().sum().values)
        ideal_values = [0] * len(null_values)
        if null_values == ideal_values:
            print("Data is already clean")
            return
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

    def split(self) -> None:

        X = self.df_final.drop(['SalePrice'], axis=1)
        Y = self.df_final['SalePrice']

        self.split_data = train_test_split(
            X, Y, train_size=0.8, test_size=0.2, random_state=0)
    
    def train(self, algo: str = "svm") -> None:
        X_train, X_valid, Y_train, Y_valid = self.split_data
        
        if algo == "svm":
            model_SVR = svm.SVR()
            model_SVR.fit(X_train,Y_train)
            Y_pred = model_SVR.predict(X_valid)
        elif algo == "random forest":
            model_RFR = RandomForestRegressor(n_estimators=10)
            model_RFR.fit(X_train, Y_train)
            Y_pred = model_RFR.predict(X_valid)
        elif algo == "linear regression":
            model_LR = LinearRegression()
            model_LR.fit(X_train, Y_train)
            Y_pred = model_LR.predict(X_valid)
        else:
            raise Exception("Invalid Algorithm")
        print(mean_absolute_percentage_error(Y_valid, Y_pred))

    def analyse(self):
        self.clean()
        self.label()
        self.split()
        self.train()