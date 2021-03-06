from gym import Env
import numpy as np
import pandas as pd
from Agent import Agent
from keras.models import load_model
from matplotlib import animation
import matplotlib.pyplot as plt


from Environment_Modul.Environments import CartPoleEnvironment, createMountainCarEnvironment
from Environment_Modul.Environments import createCartPoleEnvironment
from Environment_Modul.Environments import OneQuadrant
from Exporter_Modul.Exporter_toCSV import Exporter_toCSV
from NNModel.NNModelKlass import NNModelKlasse, NNModelKlasseOneQuadrant
from TestBench.testBench import testBenchCartPole, testBenchMountainCar, testBenchOneQuadrant
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
    # If 0 then train
    train = 0
    ###############################################
    ###########Cart Pole Environment###############
    ###############################################
    """
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
    """

    ###############################################
    ###########End Cart Pole Environment###########
    ###############################################

    ###############################################
    ###########Mountain Car Environment############
    ###############################################

    # Environment creation
    """
    env, state_size, action_size = createMountainCarEnvironment()
    
    #Gettin parameters and training
    if train == 0:
        for i in range(4):
            parameters = testBenchMountainCar(i)
            learning_rate = parameters['alpha']
            episodes = parameters['max_episodes']
            render_every = parameters['render_every']
            render_after_episode = parameters['render_after_episode']

            NNModel = NNModelKlasse(input_shape=(state_size,), action_space=action_size, lr=learning_rate)
            DQNAgent = Agent(parameters, state_size, action_size, BATCH_SIZE,
                        NNModel)
            trainMountainCarNetwork(env, DQNAgent, episodes, render_every, render_after_episode, i)
    else:
        # Specify parameters for visualization
        parameters = testBenchMountainCar(0)
        learning_rate = parameters['alpha']
        NNModel = NNModelKlasse(input_shape=(state_size,), action_space=action_size, lr=learning_rate)
        DQNAgent = Agent(parameters, state_size, action_size, BATCH_SIZE,
            NNModel)
        testNetwork(env, agent=DQNAgent, episodes=10)
    """
    ###############################################
    ###########Mountain Car Environment############
    ###############################################

    ###############################################
    #######Start One-Quadrant Environment##########
    ###############################################
    # Environment creation
    env = OneQuadrant()
    state_size = len(env.observation_space)
    action_size = len(env.action_space)
    
    #Gettin parameters and training
    if train == 0:
        for i in range(2,3):
            parameters = testBenchOneQuadrant(i)
            learning_rate = parameters['alpha']
            episodes = parameters['max_episodes']
            render_every = parameters['render_every']
            render_after_episode = parameters['render_after_episode']

            NNModel = NNModelKlasseOneQuadrant(input_shape=(state_size,), action_space=action_size, lr=learning_rate)
            DQNAgent = Agent(parameters, state_size, action_size, BATCH_SIZE,
                        NNModel)
            trainOneQuadrant(env, DQNAgent, episodes, render_every, render_after_episode, i)
    else:
        # Specify parameters for visualization
        parameters = testBenchMountainCar(0)
        learning_rate = parameters['alpha']
        NNModel = NNModelKlasse(input_shape=(state_size,), action_space=action_size, lr=learning_rate)
        DQNAgent = Agent(parameters, state_size, action_size, BATCH_SIZE,
            NNModel)
        testNetwork(env, agent=DQNAgent, episodes=10)
    ###############################################
    #######End One-Quadrant Environtmnet###########
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

 
def trainMountainCarNetwork(env, Agent, episodes, render_every, render_after_episode, iteration):
    exporterRewards = Exporter_toCSV()
    rewards_perEpisode = []
    count_steps = 0
    trainAchieved = False
    for episode in range(episodes):
        if episode % render_every == 0:
            averageReward = count_steps/render_every
            rewards_perEpisode.append(averageReward)
            count_steps = 0
        
        max_position = -99
        state = env.reset()
        state = np.reshape(state, [1, Agent.state_size])
        done = False
        i = 0
        while not done:
            # if episode % render_every == 0 and episode > render_after_episode:
            #     env.render()

            action = Agent.take_action(state, trainAchieved)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, Agent.state_size])
            count_steps += 1
            
            #Keeping track of maximun position
            if next_state[0][0] > max_position:
                max_position = next_state[0][0]
            
            if next_state[0][0] >= 0.5:  #If car achieved the limit
                reward += 10
            #_max_episode_steps restricted to 200
 
            Agent.remember(state, action, reward, next_state, done)
            
            # Agent.remember(state, action, reward, next_state, done)
            state = next_state
            i += 1
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}".format(episode, episodes , i, Agent.epsilon))
                #We save when we achieved a reward of -150
                if i <= env._max_episode_steps-50 and trainAchieved == False:
                    print("Saving trained model as mountainCar-dqn.h5")
                    Agent.save("mountainCar-dqn"+str(iteration)+str(episode)+".h5")
                    #trainAchieved = True
                    #Agent.epsilon = Agent.epsilon_min
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

def trainOneQuadrant(env, Agent, episodes, render_every, render_after_episode, iteration):
    exporterRewards = Exporter_toCSV()
    rewards_perEpisode = []
    count_steps = 0
    trainAchieved = False
    episode_reward_every = 0
    for episode in range(episodes):
        if episode % render_every == 0:     #use to get the average reward
            averageReward = episode_reward_every/(render_every*100)
            rewards_perEpisode.append(averageReward)
            episode_reward_every = 0
        episode_reward = 0
        state = env.reset()
        state = np.reshape(state, [1, Agent.state_size])
        done = False
        i = 0
        while not done:
            action = Agent.take_action(state, trainAchieved)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, Agent.state_size])
            count_steps += 1
            episode_reward += reward
            episode_reward_every += episode_reward
            Agent.remember(state, action, reward, next_state, done)
            state = next_state
            i += 1
            if done:
                print("episode: {}/{}, score: {}, e: {}, ep_reward: {:.2f}".format(episode, episodes , i,
                                                                 Agent.epsilon, episode_reward))

            Agent.replay(not trainAchieved)
        
        # if episode % render_every == 0:
        #     print("episode: " + str(episode) +" num_steps: " + str(count_steps) + 
        #     " epsilon: " + str(Agent.epsilon))

    exporterRewards.add_toCSV(rewards_perEpisode)
    exporterRewards.create_csv("OneQuadrantRewards_"+str(iteration)+".csv",1)
    

def testNetwork(env, agent, episodes):
    # agent.load("cartpole-dqn-tets_2.h5")
    agent.load("mountainCar-dqn0.h5")
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