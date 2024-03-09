import pandas as pd
import numpy as np

# os.environ["KERAS_BACKEND"] = "torch"
import keras_core as keras

import matplotlib.pyplot as plt

# x= 3
# y= 5
# z = 13
inputs = [x, y, z]
def predict():

    model = keras.Sequential()
    model.add(keras.layers.Input(shape=[3]))

    for _ in range(5):
        model.add(keras.layers.Dense(units=30, activation='relu', use_bias=True, bias_initializer="zeros"))

    model.add(keras.layers.Dense(units=1))
    model.load_weights("trained_4.weights.h5")
    # inputs = [2, 4,30] 
    inputs = np.array(inputs)
            
    # Add an extra dimension to the inputs
    inputs = np.expand_dims(inputs, axis=0)

    # Use the model to make a prediction
    prediction = model.predict(inputs)

    # Cap risk
    if prediction>100:
        prediction=100.0

    # Return the prediction
    with open('output.txt', 'w') as file:
        # Append content to the file
        file.write(str(prediction[0][0]))
    # print(prediction)
        
# predict(inputs)