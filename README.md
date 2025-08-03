# DQN-TD (Deep Q-Network)
This DQN project is part fo the **RL For Control Purposes** project made in the University of Siegen in collaboration with the M.Sc. Tim Decker and the department of mechanical engineering, full paper can be found in https://www.academia.edu/143237205/Reinforcement_Learning_For_Control_Purposes. 
This work aims to present popular algorithms in Reinforcement Learning (RL) and their application in control environments. These algorithms include:
- SARSA
- Q-Learning
- Deep Q-Learning (DQN)

Each one of them will be implemented for three different control environments:
- Cart-pole
- Mountain Car
- One-Quadrant converter

The conceptual process that takes to understand and implement any of these reinforcement learning algorithms and their interaction with diverse environments setup will be presented.
This work depends reasonably in the book on Richard Sutton and Andrew Barto [34], mostly in the introduction chapter. Some non-control examples from the mentioned reference are used for simplification and understanding purposes.
Parallel to the RL theory presentation objective of the present work, it also has as motivation to increase the interest of the readers to implement
their RL algorithm implementations for their own purposes and projects, consequently it has been included numerous pseudocodes, python implementations and references.
This work is classified as follows: chapter one presents an introduction to reinforcement learning. It starts with some classification ideas concerning where reinforcement learning settles in the field of artificial intelligence; furthermore, the fundamentals and diverse theories that are inseparable in the area will also be included in this chapter. The second chapter focuses in explaining the RL algorithms, the mathematical development as well as the pseudo code for each of the agents. The third chapter describes the environment’s architectures, their inherent attributes, and the dynamics and the reward functions. Likewise, the one-quadrant converter environment section presents the unique self-created environment; therefore, a programming setup based on the gym libraries [14] is also described. The fourth chapter merges the principles developed in the second and third chapter. Results and observations from the interaction agent-environment will be shown. Finally, a fifth chapter includes the conclusions, but also the future work necessary to continue a study in reinforcement learning.


## Technologies and packages used
- python
- pandas
- numpy
- Keras
- matplotlib
- tensor flow
- control system environments from gym, see https://gymnasium.farama.org/ 
---
## Definition of Task
The idea behind reinforcement learning (RL) is very similar to human learning and therefore intuitive. Act, observe, evaluate the reward, and
adjust your policy for enacting with the environment. With the growing power of computers, an enormous amount of trials can be carried out in simulation in a short amount of time. For example, the project OpenAI Five [6] gathered 180 years worth of playtime experience in one single
day. With such computational power, agents (can be understood as controller) can be trained which surpass human abilities to fulfill tasks as playing Dota, Chess and Go (AlphaGo [4]). In engineering RL is often considered unreliable, since the agents fail to consistently perform well, training might take too long and can often not be done in the real environment but just in simulation. 
In order to understand these issues, a study about RL categories and some of their methods needs to be done. With this knowledge promising methods need to be selected for training agents to solve simulated engineering problems (stable and unstable). Finally, the application of these methods needs to be investigated and evaluated.

### Tasks
- Get familiar with reinforcement learning categories and methods
- Choose stable and unstable control applications (simulated)
- Select several methods for training agents• Apply the reinforcement learning algorithms to the chosen applications
- Evaluate the outcome and compare it to existing control strategies for the chosen applications.
