import numpy as np
import pandas as pd
from Agent import Agent

# from Exporter_Modul.Exporter_toCSV import Exporter_toCSV
# from Environment_Modul.CliffEnvironment import CliffEnvironment
# from Tests.TrajectoryTester import Trajectory
# from Tests.EnvironmentTest import EnvironmentTester
from Environment_Modul.CartPoleEnvironment import CartPoleEnvironment
from Environment_Modul.CartPoleEnvironment import createEnvironment

# Hyperparameters

EPISODES = 1000
EPSILON = 1.0   # exploration rate
EPSILON_MIN = .001
EPSILON_DECAY = 0.999
BATCH_SIZE = 64
TRAIN_START = 1000
GAMMA = 0.98
#########################


def main():
    # Environment creation
    env, state_size, action_size = createEnvironment()
    # Agent Creation
    DQNAgent = Agent(state_size, action_size, EPISODES, EPSILON,
                        EPSILON_MIN, EPSILON_DECAY, BATCH_SIZE,
                        TRAIN_START)
    trainNetwork(env, DQNAgent)




def trainNetwork(env, Agent):
    for episode in range(Agent.episodes):
        state = env.reset()


if __name__ == '__main__':
    main()