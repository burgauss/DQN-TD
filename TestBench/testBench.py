#########################################
# Test Bench Cart Pole
    
def testBenchCartPole(i):
    if i == 0:
       # print("starting test bench "+str(i))
        alpha = 0.00025 
        max_episodes = 60
        gamma = 0.98
        train_start = 500
        epsilon_decay = 0.999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 1
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 1:
        #print("starting test bench "+str(i))
        alpha = 0.00025 
        max_episodes = 60
        gamma = 0.95
        train_start = 500
        epsilon_decay = 0.999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 1
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 2:
        alpha = 0.001 
        max_episodes = 60
        gamma = 0.98
        train_start = 500
        epsilon_decay = 0.998
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 1
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 3:
        alpha = 0.0015 #Wont be use here
        max_episodes = 50
        gamma = 0.98
        train_start = 500
        epsilon_decay = 0.998
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 1
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters

###########################################
#Test Bench for the One Quadrant converter

def testBenchMountainCar(i):
    if i == 0:
       # print("starting test bench "+str(i))
        alpha = 0.001
        max_episodes = 600#  300
        gamma = 0.99
        train_start = 1000
        epsilon_decay = 0.9999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 10
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 1:
        #print("starting test bench "+str(i))
        alpha = 0.001 
        max_episodes = 600
        gamma = 0.95
        train_start = 1000
        epsilon_decay = 0.9999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 10
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 2:
        alpha = 0.002 
        max_episodes = 600
        gamma = 0.98
        train_start = 1000
        epsilon_decay = 0.9999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 10
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 3:
        alpha = 0.015 #Wont be use here
        max_episodes = 600
        gamma = 0.98
        train_start = 1000
        epsilon_decay = 0.9999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 10
        render_after_episode = 0
        epsilon_start = 1.0
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters

###########################################
#Test Bench for the One Quadrant converter

def testBenchOneQuadrant(i):
    if i == 0:
        alpha = 0.015
        max_episodes = 4000
        gamma = 0.96
        train_start = 500
        epsilon_decay = 0.99999
        epsilon_min = 0.001
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters

    elif i == 1:
        alpha = 0.001
        max_episodes = 4000
        gamma = 0.95
        train_start = 500
        epsilon_decay = 0.99999
        epsilon_min = 0.001
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters
    elif i == 2:
        alpha = 0.1
        max_episodes = 4000
        gamma = 0.95
        train_start = 500
        epsilon_decay = 0.99999
        epsilon_min = 0.001
        #start_greedy_episode = 10000
        #episondes_of_greedynes = 5000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        #epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"train_start":train_start,
                    "epsilon_decay":epsilon_decay,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_min":epsilon_min}

        return parameters

