import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import os

os.environ["KERAS_BACKEND"] = "torch"
import keras_core as keras


class Model:
    def __init__(self, file_path, units=16, activation='sigmoid', num_layers= 3, target_columns=["score", "score2"]):
        self.target_columns = target_columns
        self.num_outputs = len(target_columns)
        self.df=pd.read_excel(file_path)
        self.input_shape = [len(self.df.columns)-self.num_outputs] # 2 outputs

        self.model = keras.Sequential()
        self.model.add(keras.layers.Input(shape=self.input_shape))
        
        for _ in range(num_layers):
            self.model.add(keras.layers.Dense(units=units, activation=activation))
        
        self.model.add(keras.layers.Dense(units=self.num_outputs))

    def train(self, test_size=0.2, random_state=42):        
        # Split the data into features (X) and target (y)
        X = self.df.drop(self.target_columns, axis=1)
        y = self.df[self.target_columns]
        print(y)
        
        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        self.model.compile(
            loss = keras.losses.MeanSquaredError(),
            optimizer = keras.optimizers.SGD(learning_rate= 0.2)
        )        
        # Train the model
        callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
        self.model.fit(X_train, y_train, validation_split= 0.2, epochs= 20, batch_size= 64, callbacks= [callback], verbose= 0)
        # self.model.fit(X_train, y_train, epochs= 50, batch_size= 64)

        # Make predictions on the test set and calculate the mean squared error
        predictions = self.model.predict(X_test)
        print(predictions)
        mse = mean_squared_error(y_test, predictions)
        
        print(f"Mean Squared Error: {mse}")

    def predict(self, inputs):
        # Convert the inputs to a numpy array
        inputs = np.array(inputs)        
        
        # Add an extra dimension to the inputs
        inputs = np.expand_dims(inputs, axis=0)
        
        # Use the model to make a prediction
        prediction = self.model.predict(inputs)
        
        # Return the prediction
        return prediction



def main():
    my_model = Model('personenlijst.xlsx', 16, 'sigmoid', 3, ['score', 'score2'])
    my_model.train(0.2, 42)
    inputs = [2233, 3] # retrieve inputs from front-end
    print(my_model.predict(inputs)) 

    print("Hello World!")

if __name__ == "__main__":
    main()