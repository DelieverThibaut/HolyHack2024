import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import os

os.environ["KERAS_BACKEND"] = "torch"
import keras_core as keras

import matplotlib.pyplot as plt




class Model:
    def __init__(self, file_path, units=16, activation='relu', num_layers= 3, target_columns=["Risk"]):
        self.target_columns = target_columns

        self.num_outputs = len(target_columns)

        self.df=pd.read_excel(file_path)

        self.input_shape = [len(self.df.columns)-self.num_outputs]

        self.model = keras.Sequential()

        self.model.add(keras.layers.Input(shape=self.input_shape))
        
        for _ in range(num_layers):
            self.model.add(keras.layers.Dense(units=units, activation=activation, use_bias=True, bias_initializer="zeros"))

        self.model.add(keras.layers.Dense(units=self.num_outputs))

   
    def train(self, test_size=0.2, random_state=42):        
        # Split the data into features (X) and target (y)
        self.y= self.df[self.target_columns]
        self.X = self.df.drop(self.target_columns, axis=1)
       
        
        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=test_size, random_state=random_state)

        self.model.compile(
            loss = keras.losses.MeanSquaredError(),
            optimizer = keras.optimizers.Adam(learning_rate= 0.005)
        )        
        # Train the model
        callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
        history = self.model.fit(X_train, y_train, validation_split= 0.2, epochs= 200, batch_size= 32, callbacks= [callback], verbose= 0)

        # used to tune training

        # plt.figure()
        # plt.xlabel('epoch')
        # plt.ylabel('training loss')
        # plt.plot(history.history['loss'], color= "firebrick")
        # plt.plot(history.history['val_loss'], color= 'teal')
        # plt.show()

        # Make predictions on the test set and calculate the mean squared error
        # predictions = self.model.predict(X_test)
        # print(predictions)
        # mse = mean_squared_error(y_test, predictions)
        
        # print(f"Mean Squared Error: {mse}")

    def predict(self, inputs):
        # Convert the inputs to a numpy array
        inputs = np.array(inputs)        
        
        # Add an extra dimension to the inputs
        inputs = np.expand_dims(inputs, axis=0)
        
        # Use the model to make a prediction
        prediction = self.model.predict(inputs)

        # Cap risk
        if prediction>100:
            prediction=100.0
        
        # Return the prediction
        return prediction
    
    def save_weights(self, filename):
        # save weights to a file
        self.model.save_weights(filename)

    def load_weights(self, filename):
        # load weights from a file
        self.model.load_weights(filename)


def main():
    my_model = Model('aankooplijst.xlsx', 30, 'relu', 5, ['Risk'])
    # my_model.train(0.2, 42)
    my_model.load_weights("trained_4.weights.h5")

    inputs = [2, 4,30] # retrieve inputs from front-end
    print("PREDICTION: \n \n \n")
    print(my_model.predict(inputs))
    
    inputs = [7, 80, 150] # retrieve inputs from front-end
    print(my_model.predict(inputs))

    inputs = [7, 30, 150] # retrieve inputs from front-end
    print(my_model.predict(inputs))

    inputs = [15, 15, 200] # retrieve inputs from front-end
    print(my_model.predict(inputs))

    inputs = [30, 100, 150] # retrieve inputs from front-end
    print(my_model.predict(inputs))
  
    # my_model.save_weights("trained_4.weights.h5")
    # my_model.load_weights("initial_weights.h5")

if __name__ == "__main__":
    main()
   