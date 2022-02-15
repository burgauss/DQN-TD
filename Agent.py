from collections import deque
from keras.models import Model, load_model
import numpy as np
import random

class Agent():

    def __init__(self, parametersDict, state_space, action_space, batch_size, Model):
                
        # Environment parameters
        self.state_size = state_space
        self.action_size = action_space
        
        #E-greedy parameters
        self.epsilon = parametersDict['epsilon_start']
        self.epsilon_min = parametersDict['epsilon_min']
        self.epsilon_decay = parametersDict['epsilon_decay']

        #Train parameters
        # self.episodes = episodes
        self.batch_size = batch_size
        self.train_start = parametersDict['train_start']
        self.memory = deque(maxlen=2000) 
        self.gamma = parametersDict['gamma']
        
        #Model
        self.model = Model


    def remember(self, state, action, reward, next_state, done):
        # Memorize the trajectory
        self.memory.append((state, action, reward, next_state, done))
        if len(self.memory) > self.train_start: # check for size of the memory
            self.decay_epsilon()

    def decay_epsilon(self): # Decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def take_action(self, state): # Be greedy
        if self.epsilon > np.random.random():
            action = np.random.randint(0,self.action_size)
        else:
            action = np.argmax(self.model.predict(state))
        
        return action

    def replay(self, doFit):
        if len(self.memory) < self.train_start:
            return
        # Randomly sample minibatch from the memory
        # Minibatch of size min(len(memory)) or batch size

        minibatch = random.sample(self.memory, min(len(self.memory), self.batch_size))
        state = np.zeros((self.batch_size, self.state_size))
        next_state = np.zeros((self.batch_size, self.state_size)) # matrix
        action, reward, done = [], [], []

        # before prediction
        for i in range(self.batch_size):
            state[i] = minibatch[i][0]
            action.append(minibatch[i][1])
            reward.append(minibatch[i][2])
            next_state[i] = minibatch[i][3]
            done.append(minibatch[i][4])
        
        # Batch prediction
        target = self.model.predict(state)
        target_next = self.model.predict(next_state)

        for i in range(self.batch_size):
            # Correction of the Q val for action used
            # if done[i]:
            #     target[i][action[i]] = reward[i]
            # else:
                # Standard DQN
                # DQN chooses the max Q value among next action
                # Selection and evaluation of action is on the target of Q Network
                # Q_max = max_a' Q_target(s', a')
            target[i][action[i]] = reward[i] + self.gamma * (np.amax(target_next[i]))
        # Train
        if doFit == True:
            self.model.fit(state, target, batch_size=self.batch_size, verbose=0)

    def load(self, name):
        self.model = load_model(name)
    
    def save(self, name):
        self.model.save(name)

