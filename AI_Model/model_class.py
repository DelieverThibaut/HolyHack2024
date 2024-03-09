import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import os

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader

os.environ["KERAS_BACKEND"] = "torch"
import keras_core as keras


class MyModel:
    def __init__(self, file_path, units=16, activation='sigmoid', num_layers= 3, num_outputs = 2):
        
        self.df=pd.read_excel(file_path)
        self.input_shape = [len(self.df.columns)-num_outputs] # 2 outputs

        self.model = keras.Sequential()
        self.model.add(keras.layers.Input(shape=self.input_shape))
        
        for _ in range(num_layers):
            self.model.add(keras.layers.Dense(units=units, activation=activation))
        
        self.model.add(keras.layers.Dense(units=num_outputs))

    def train(self, target_column, test_size=0.2, random_state=42):        
        # Split the data into features (X) and target (y)
        X = self.df.drop(target_column, axis=1)
        y = self.df[target_column]
        
        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        self.model.compile(
            loss = keras.losses.MeanSquaredError(),
            optimizer = keras.optimizers.SGD(learning_rate= 0.2)
        )        
        # Train the model
        self.model.fit(X_train, y_train, batch_size=32, epochs=10)
        
        # Make predictions on the test set and calculate the mean squared error
        predictions = self.model.predict(X_test)
        print(predictions)
        mse = mean_squared_error(y_test, predictions)
        
        print(f"Mean Squared Error: {mse}")

    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions

def main():
    my_model = MyModel('personenlijst.xlsx', 16, 'sigmoid', 3, 1)
    my_model.train('score', 0.2, 42)
    # my_model.predict(X_client) # retrieve X_client from front-end

    print("Hello World!")

if __name__ == "__main__":
    main()