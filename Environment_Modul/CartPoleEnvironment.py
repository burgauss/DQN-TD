import gym

class CartPoleEnvironment():
    def __init__(self):
        self.env = gym.make('CartPole-v0')
        self.state_size = self.env.observation_space.shape[0]
        self.action_size = self.env.action_space.n
        

def createCartPoleEnvironment():
    env = gym.make('CartPole-v0')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    return env, state_size, action_size
