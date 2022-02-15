import numpy as np
import pandas as pd
from Agent import Agent
from keras.models import load_model
from matplotlib import animation
import matplotlib.pyplot as plt

# from Exporter_Modul.Exporter_toCSV import Exporter_toCSV
# from Environment_Modul.CliffEnvironment import CliffEnvironment
# from Tests.TrajectoryTester import Trajectory
# from Tests.EnvironmentTest import EnvironmentTester
from Environment_Modul.CartPoleEnvironment import CartPoleEnvironment
from Environment_Modul.CartPoleEnvironment import createCartPoleEnvironment
from Exporter_Modul.Exporter_toCSV import Exporter_toCSV
from NNModel.NNModelKlass import NNModelKlasse
from TestBench.testBench import testBenchCartPole
from Tests.tests import test_environment_variables
from Tests.tests import test_agent_actions
from Tests.tests import test_video
from Tests.tests import test_video_git, mountainCarTest

# Hyperparameters

# EPISODES = 1000
# EPSILON = 1.0   # exploration rate
# EPSILON_MIN = .001
# EPSILON_DECAY = 0.999
BATCH_SIZE = 64
# TRAIN_START = 500
# GAMMA = 0.98
#########################


def main():
    # If one then train
    train = 1
    ###############################################
    ###########Cart Pole Environment###############
    ###############################################
    # Environment creation
    env, state_size, action_size = createCartPoleEnvironment()
    
    #Gettin parameters and training
    if train == 1:
        for i in range(4):
            parameters = testBenchCartPole(i)
            learning_rate = parameters['alpha']
            episodes = parameters['max_episodes']
            render_every = parameters['render_every']
            render_after_episode = parameters['render_after_episode']

            NNModel = NNModelKlasse(input_shape=(state_size,), action_space=action_size, lr=learning_rate)
            DQNAgent = Agent(parameters, state_size, action_size, BATCH_SIZE,
                        NNModel)
            trainCartPoleNetwork(env, DQNAgent, episodes, render_every, render_after_episode, i)
    else:
        # Specify parameters for visualization
        parameters = testBenchCartPole(1)
        DQNAgent = Agent(parameters, state_size, action_size, BATCH_SIZE,
            NNModel)
        testNetwork(env, agent=DQNAgent, episodes=10)
    
    #############Old modifications
    # Agent Creation
    # DQNAgent = Agent(state_size, action_size, GAMMA, EPSILON,
    #                     EPSILON_MIN, EPSILON_DECAY, BATCH_SIZE,
    #                     TRAIN_START, NNModel)


    # trainCartPoleNetwork(env, DQNAgent, EPISODES)


    #testNetwork(env, agent=DQNAgent, episodes=1)

    ###############################################
    ###########End Cart Pole Environment###########
    ###############################################

    ###############################################
    ###########Mountain Car Environment############
    ###############################################

def trainCartPoleNetwork(env, Agent, episodes, render_every, render_after_episode, iteration):
    exporterRewards = Exporter_toCSV()
    rewards_perEpisode = []
    count_steps = 0
    trainAchieved = False
    for episode in range(episodes):
        if episode % render_every == 0:
            averageReward = count_steps/render_every
            rewards_perEpisode.append(averageReward)
            count_steps = 0
        state = env.reset()
        state = np.reshape(state, [1, Agent.state_size])
        done = False
        i = 0
        while not done:
            # if episode % render_every == 0 and episode > render_after_episode:
                #env.render()

            action = Agent.take_action(state, trainAchieved)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, Agent.state_size])
            count_steps += 1
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
                if i == env._max_episode_steps and trainAchieved == False:
                    print("Saving trained model as cartpole-dqn.h5")
                    Agent.save("cartpole-dqn-test"+str(iteration)+".h5")
                    trainAchieved = True
                    Agent.epsilon = Agent.epsilon_min
                    #env.close()
                    #return
            # if done and episode % render_every == 0:
            #      Agent.replay(True)
            # else:
            #     Agent.replay(False)
            Agent.replay(not trainAchieved)
        
        # if episode % render_every == 0:
        #     print("episode: " + str(episode) +" num_steps: " + str(count_steps) + 
        #     " epsilon: " + str(Agent.epsilon))

        exporterRewards.add_toCSV(rewards_perEpisode)
        exporterRewards.create_csv("CartPolerewardsPerEpisode"+str(iteration)+".csv",1)
    
    env.close()
                
def testNetwork(env, agent, episodes):
    agent.load("cartpole-dqn-tets_2.h5")
    #frames = []
    for episode in range(episodes):
        state = env.reset()
        state = np.reshape(state, [1, agent.state_size])
        done = False
        i = 0
        while not done:
            env.render()
           # frames.append(env.render(mode="rgb_array"))
            action = np.argmax(agent.model.predict(state))
            next_state, reward, done, _ = env.step(action)
            state = np.reshape(next_state, [1, agent.state_size])
            i += 1
            if done:
                print("episode: {}/{}, score: {}".format(episode, episodes, i))
                #env.close()
                #save_frames_as_gif(frames)
                break
    env.close()

def save_frames_as_gif(frames, path='./', filename='gym_animation.gif'):

    #Mess with this to change frame size
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi=72)

    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    anim.save(path + filename, writer='imagemagick', fps=60)


if __name__ == '__main__':
    main()