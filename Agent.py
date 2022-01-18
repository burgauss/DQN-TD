from collections import defaultdict
from typing import DefaultDict
import numpy as np
from numpy import random

class Agent():
    def __init__(self, state_space, action_space):
        #self.policy = defaultdict(lambda: np.zeros(action_space))
        self.state_space = state_space
        self.action_space = action_space

        self.policy = {}  # Policy is a dictionary, where the key is the state
        for state in range(state_space + 1):  
            self.policy[state] = np.zeros(action_space)  # The items are a vector of size 3

    def agent_start_unirfomly_random(self):
        for state in range(self.state_space + 1):
            self.policy[state] = np.ones(self.action_space) / self.action_space

    def agent_start_randomly(self):
        for state in range(self.state_space + 1):
            self.policy[state] = np.random.dirichlet(np.ones(self.action_space), size = 1)


    def agent_fav_right(self):
        for state in range(self.state_space +1):
            if state >= 37 and state <=47:
                self.policy[state] = [0,0,0,0]
            else:
                self.policy[state] = [0.15, 0.15, 0.15, 0.55]  #Favourly to the right

    def agent_action(self, state): # Be greedy
        q_values = self.policy[state]
        top = float("-inf")
        tie_vals = []
        
        for ind in range(len(q_values)):
            if q_values[ind] > top:
                top = q_values[ind]
                tie_vals = []
                
            
            if q_values[ind] == top:
                tie_vals.append(ind)
                
        action =  random.choice(tie_vals)      
        return action
        

    def agent_action_epsilon(self, state, epsilon):
        if (epsilon > np.random.random()):
            action = np.random.randint(0,4)
        else:
            # action = np.argmax(self.policy[state])
            action = self.agent_action(state)
        
        return action

    def agent_update_policy(self, s, a, r, next_s, alpha, gamma):
        q_values = self.policy[s]
        next_q_values = self.policy[next_s]
        q_values[a] = q_values[a] + alpha * (r + gamma*(np.max(next_q_values)) -q_values[a])

        self.policy[s] = q_values
    
    def agent_update_policy_end(self, s,a,r, alpha):
        q_values = self.policy[s]
        q_values[a] = q_values[a] + alpha * (r  - q_values[a])

        self.policy[s] = q_values
