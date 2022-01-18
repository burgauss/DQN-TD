import numpy as np
import pandas as pd
from Agent import Agent

# from Exporter_Modul.Exporter_toCSV import Exporter_toCSV
# from Environment_Modul.CliffEnvironment import CliffEnvironment
# from Tests.TrajectoryTester import Trajectory
# from Tests.EnvironmentTest import EnvironmentTester
from Environment_Modul.CartPoleEnvironment import CartPoleEnvironment
from Environment_Modul.CartPoleEnvironment import createEnvironment

#Hyperparameters
env_width = 12
env_height = 4
env_action_space = 4
ALPHA = 0.01
max_episodes = 5000
GAMMA = 0.98
#########################


def main():
    # env = CliffEn
    env, state_size, action_size = createEnvironment()



    # env.env_init(env_height, env_width)
    # env_state_space = env.state(env.goal_loc)
    # right_fav_agent = Agent(env_state_space, env_action_space)
    # right_fav_agent.agent_fav_right()
    
    # # trajectory_tester = Trajectory()
    # # trajectory_tester.example_trajectory(env, right_fav_agent, 2)

    # # env_tester = EnvironmentTester()
    # # env_tester.test_one_step()

    # q_learning_algorithm(ALPHA,
    #  GAMMA, env, right_fav_agent, max_episodes)




def q_learning_algorithm(alpha, gamma, env, agent, episodes):
    exporter = Exporter_toCSV()
    exporterRewards = Exporter_toCSV()
    exporterTrajectory = Exporter_toCSV()

    action_values = []
    rewards_perEpisode = []
    trajectory_samples = []
    # action_values.append(agent.policy)
    action_values.append([[-1] + q for q in agent.policy.values()])
    action_values_clean = []
    for episode in range(episodes+1):
        count_steps = 0
        sumRewards = 0
        env.env_start()
        reward, state, terminal = env.reward_state_term
        #action = agent.agent_action(state)
        while (terminal != True):
            count_steps += 1
            action = agent.agent_action_epsilon(state,0.1)
            if episode % 50 == 0:
                # Just map the trajectories every 50 episodes
                trajectory_samples.append([episode, count_steps, state, action, reward])
            
            env.env_step(action)
            reward, next_state, terminal = env.reward_state_term
            sumRewards += reward # Help to print rewards per episode

            if terminal == True:
                #Agend end
                agent.agent_update_policy_end(state, action, reward, alpha)
            else:
                agent.agent_update_policy(state, action, reward, next_state, alpha, gamma)

            state = next_state
            #action = next_action

        if episode % 50 == 0:
            #action_values.append(agent.policy)
            new_action_values = [[episode] + q for q in agent.policy.values()]
            #action_values = action_values + new_action_values
            action_values.append(new_action_values)
            rewards_perEpisode.append([episode, sumRewards])
            print("episode: " + str(episode) +" num_steps: " + str(count_steps))

    # Exporting Q-Values
    exporter.add_toCSV(action_values)
    exporter.create_csv("action_values_1.csv",2)

    # exporting Rewards per Episode
    exporterRewards.add_toCSV(rewards_perEpisode)
    exporterRewards.create_csv("rewardsPerEpisode.csv",1)

    # Exporting the trajectory
    exporterTrajectory.add_toCSV(trajectory_samples)
    exporterTrajectory.create_csv("trajectoryQLearning.csv", 1)

if __name__ == '__main__':
    main()