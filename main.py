import numpy as np
import pandas as pd
from Agent import Agent

# from Exporter_Modul.Exporter_toCSV import Exporter_toCSV
# from Environment_Modul.CliffEnvironment import CliffEnvironment
# from Tests.TrajectoryTester import Trajectory
# from Tests.EnvironmentTest import EnvironmentTester
from Environment_Modul.CartPoleEnvironment import CartPoleEnvironment
from Environment_Modul.CartPoleEnvironment import createEnvironment
from NNModel.NNModelKlass import NNModelKlasse

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

    #test_environment_variables(env)

    # Agent Creation
    DQNAgent = Agent(state_size, action_size, EPSILON,
                        EPSILON_MIN, EPSILON_DECAY, BATCH_SIZE,
                        TRAIN_START)

    # NN creation
    NNModel = NNModelKlasse(input_shape=(state_size,), action_space=action_size)

    trainNetwork(env, DQNAgent, EPISODES, NNModel)




def trainNetwork(env, Agent, episodes, NNModel):
    for episode in range(episodes):
        state = env.reset()
        state = np.reshape(state, [1, Agent.state_size])
        done = False
        i = 0
        while not done:
            #env.render()
            action = Agent.take_action(state, NNModel)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, Agent.state_size])
            #_max_episode_steps restricted to 200
            if not done or i == env._max_episode_steps-1:
                reward = reward
            else:
                # if done the punishment is -100
                reward = -100
            Agent.remember(state, action, reward, next_state, done)
            state = next_state
            i += 1
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}".format(episode, episodes , i, Agent.epsilon))
                if i == env._max_episode_steps:
                    print("Saving trained model as cartpole-dqn.h5")
                    Agent.save("cartpole-dqn-tets.h5")
                    return
                

def test_environment_variables(env):
    print(env._max_episode_steps)


if __name__ == '__main__':
    main()