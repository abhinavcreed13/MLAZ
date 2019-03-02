import pandas as pd
from sklearn.linear_model import LinearRegression
import json

class SimpleLinearRegression:

    def __init__(self):
        self.regressor = LinearRegression()

    def train_model(self, training_data_json):
        # print(json.dumps(training_data_json))
        # print(type(training_data_json))
        self.training_data = pd.read_json(path_or_buf=json.dumps(training_data_json), orient='columns')
        self.x = self.training_data.iloc[:, :-1].values
        self.y = self.training_data.iloc[:, 1].values
        self.regressor.fit(self.x, self.y)

    def predict(self,x_val):
        x_val = [[x_val]]
        y_val = self.regressor.predict(x_val)
        return y_val.tolist()[0]
