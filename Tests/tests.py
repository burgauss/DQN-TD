import numpy as np
import gym
from gym.wrappers import Monitor
from matplotlib import animation
import matplotlib.pyplot as plt
import gym


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

def test_video():
    env = Monitor(gym.make('CartPole-v0'), './video', force=True)
    state = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        state_next, reward, done, info = env.step(action)
    
    env.close()

def test_video_git(env):
    observation = env.reset()
    frames = []
    for t in range(1000):
        #Render to frames buffer
        frames.append(env.render(mode="rgb_array"))
        action = env.action_space.sample()
        _, _, done, _ = env.step(action)
        if done:
            break
    env.close()
    save_frames_as_gif(frames)

def save_frames_as_gif(frames, path='./', filename='gym_animation.gif'):

    #Mess with this to change frame size
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi=72)

    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    anim.save(path + filename, writer='imagemagick', fps=60)

def mountainCarTest():
    env = gym.make('MountainCar-v0')
    state = env.reset()
    print(state)
    action = 2
    for i in range(1000):
        env.render()
        state, reward, done, _ = env.step(action)
        print(state)
    
    env.close()


