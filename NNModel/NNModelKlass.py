from keras.models import Model, load_model
from keras.layers import Input, Dense
from keras.optimizers import Adam, RMSprop


def NNModelKlasse(input_shape, action_space):
    X_input = Input(input_shape)

    # Using dense as the basic form of a neural network layer
    # Input Layer of state size and Hiden Layer with 512 nodes
    X = Dense(512, input_shape=input_shape, activation="relu", 
            kernel_initializer='he_uniform')(X_input)

    # Hidden layer with 256 nodes
    X = Dense(256, activation="relu", kernel_initializer='he_uniform')(X)

    # Hidden layer with 64 nodes
    X = Dense(64, activation="relu", kernel_initializer='he_uniform')(X)

    #Output Layer with # of actions: 2 nodes (left and right)
    

