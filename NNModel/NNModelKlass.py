from keras.models import Model
from keras.layers import Input, Dense
from keras.optimizers import Adam, RMSprop
import tensorflow as tf
###Comment to test github

def NNModelKlasse(input_shape, action_space, lr):
    X_input = Input(input_shape)

    # Using dense as the basic form of a neural network layer
    # Input Layer of state size and Hiden Layer with 512 nodes
    X = Dense(24, input_shape=input_shape, activation="relu", 
            kernel_initializer='he_uniform')(X_input)
#     X = Dense(512, input_shape=input_shape, activation="relu", 
#             kernel_initializer='he_uniform')(X_input)

    # Hidden layer with 256 nodes
    X = Dense(48, activation="relu", kernel_initializer='he_uniform')(X)
#   X = Dense(256, activation="relu", kernel_initializer='he_uniform')(X)

    # Hidden layer with 64 nodes
    #X = Dense(64, activation="relu", kernel_initializer='he_uniform')(X)

    #Output Layer with # of actions: 2 nodes (left and right)
    X = Dense(action_space, activation='linear', kernel_initializer='he_uniform')(X)

    model = Model(inputs = X_input, outputs = X, name='CartPole_DQN_modelV2')
    #model.compile(loss="mean_squared_error", optimizer=RMSprop(lr=0.00025, rho=0.95, epsilon=0.01), metrics=["accuracy"])
    model.compile(loss="mean_squared_error", optimizer=Adam(learning_rate=lr), metrics=["accuracy"])
    model.summary()
    return model


def NNModelKlasseOneQuadrant(input_shape, action_space, lr):
    X_input = Input(input_shape)

    # 'Dense' is the basic form of a neural network layer
    # Input Layer of state size(4) and Hidden Layer with 512 nodes
    X = Dense(64, input_shape=input_shape, activation="relu", kernel_initializer=tf.keras.initializers.RandomUniform(
        minval = -0.03, maxval = 0.03))(X_input)

    # Hidden layer with 256 nodes
    #X = Dense(256, activation="relu", kernel_initializer='he_uniform')(X)
    
    # Hidden layer with 64 nodes
    X = Dense(32, activation="relu", kernel_initializer='he_uniform')(X)

    # Output Layer with # of actions: 2 nodes (left, right)
    X = Dense(action_space, activation=None, kernel_initializer='he_uniform')(X)

    model = Model(inputs = X_input, outputs = X, name='OneQuadrant_DQN_model')
    model.compile(loss="mean_squared_error", optimizer=RMSprop(learning_rate=0.001, rho=0.95, epsilon=0.01), metrics=["accuracy"])
    model.summary()
    return model