#########################################
# Test Bench Cart Pole
    
def testBenchCartPole(i):
    if i == 0:
       # print("starting test bench "+str(i))
        alpha = 0.015
        max_episodes = 80000
        gamma = 0.96
        start_greedy_episode = 10000
        episondes_of_greedynes = 5000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}

        return parameters
    elif i == 1:
        #print("starting test bench "+str(i))
        alpha = 0.1
        max_episodes = 80000
        gamma = 0.98
        start_greedy_episode = 50000
        episondes_of_greedynes = 8000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters
    elif i == 2:
        alpha = 0.2
        max_episodes = 80000
        gamma = 0.95
        start_greedy_episode = 50000
        episondes_of_greedynes = 5000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters
    elif i == 3:
        alpha = 0.01
        max_episodes = 80000
        gamma = 0.99
        start_greedy_episode = 50000
        episondes_of_greedynes = 15000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters

###########################################
#Test Bench for the One Quadrant converter

def testBenchMountainCar(i):
    if i == 0:
       # print("starting test bench "+str(i))
        alpha = 0.015
        max_episodes = 80000
        gamma = 0.96
        start_greedy_episode = 10000
        episondes_of_greedynes = 5000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}

        return parameters
    elif i == 1:
        #print("starting test bench "+str(i))
        alpha = 0.1
        max_episodes = 80000
        gamma = 0.98
        start_greedy_episode = 50000
        episondes_of_greedynes = 8000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters
    elif i == 2:
        alpha = 0.2
        max_episodes = 80000
        gamma = 0.95
        start_greedy_episode = 50000
        episondes_of_greedynes = 5000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters
    elif i == 3:
        alpha = 0.01
        max_episodes = 80000
        gamma = 0.99
        start_greedy_episode = 50000
        episondes_of_greedynes = 15000
        render_every = 1000
        render_after_episode = max_episodes//2
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters

###########################################
#Test Bench for the One Quadrant converter

def testBenchOneQuadrant(i):
    if i == 0:
        alpha = 0.01
        max_episodes = 40000
        gamma = 0.97
        start_greedy_episode = 10000
        episondes_of_greedynes = 1000
        render_every = 100
        render_after_episode = 0
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}

        return parameters
    elif i == 1:
        alpha = 0.1
        max_episodes = 40000
        gamma = 0.95
        start_greedy_episode = 10000
        episondes_of_greedynes = 5000
        render_every = 100
        render_after_episode = 0
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters
    elif i == 2:
        alpha = 0.1
        max_episodes = 40000
        gamma = 0.95
        start_greedy_episode = 10000
        episondes_of_greedynes = 1000
        render_every = 100
        render_after_episode = 0
        epsilon_start = 1
        epsilon_decrease_factor = epsilon_start/(max_episodes - start_greedy_episode - episondes_of_greedynes)

        parameters = {"alpha":alpha,"gamma":gamma,"max_episodes":max_episodes,"start_greedy_episode":
                    start_greedy_episode,"render_every":render_every,
                    "render_after_episode":render_after_episode,"epsilon_start":epsilon_start,
                    "epsilon_decrease_factor":epsilon_decrease_factor}
        return parameters

