import numpy as np

def test_environment_variables(env):
    print(env._max_episode_steps)

def test_agent_actions(env, Agent, episodes):
    for episode in range(episodes):
        state = env.reset()
        state = np.reshape(state, [1, Agent.state_size])
        done = False
        i = 0
        while not done:
            #env.render()
            action = Agent.take_action(state)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, Agent.state_size])
            print("state is:", state, "action is: ", action)
            state = next_state