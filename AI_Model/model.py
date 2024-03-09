import numpy as np
import torch
import os
import pandas as pd

os.environ["KERAS_BACKEND"] = "torch"
import keras_core as keras

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def init_model(input_shape=[3], units=16, activation='sigmoid', num_layers=2):
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=input_shape))
    
    for _ in range(num_layers):
        model.add(keras.layers.Dense(units=units, activation=activation))
    
    model.add(keras.layers.Dense(units=1))
    
    return model


def train_model_from_excel(model, file_path, target_column, test_size=0.2, random_state=42):
    # Load the data from the Excel file
    df = pd.read_excel(file_path)
    
    # Split the data into features (X) and target (y)
    X = df.drop(target_column, axis=1)
    print(target_column)
    y = df[target_column]
    print(y)

    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model.compile(
    loss = keras.losses.MeanSquaredError(),
    optimizer = keras.optimizers.SGD(learning_rate= 0.2)
)
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the test set and calculate the mean squared error
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"Mean Squared Error: {mse}")
    
    return model

def predict_using_model(model, X_train):
    predictions = model.predict(X_train)
    return predictions


    

def main():
    model = init_model([2], 16, 'sigmoid', 3)
    train_model_from_excel(model, 'personenlijst.xlsx', 'score', 0.2, 42)
    # predict_using_model(model, X_train)

    print("Hello World!")

if __name__ == "__main__":
    main()

