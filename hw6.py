import numpy as np
import matplotlib.pyplot as plt

####################################################################################################
###                                        Problem 1                                             ###
####################################################################################################
p1 = True
if p1:
    n_exp = int(1e5)

    state = int(np.round(5 * np.random.rand() - 0.5))
    state_count = np.zeros(5)
    state_list = np.zeros(n_exp)

    for j in range(n_exp):
        #update state
        walk_dir = np.round(np.random.rand())
        if walk_dir:
            state = (state - 1)%5
            state_count[state] = state_count[state] + 1
        else:
            state = (state + 1)%5
            state_count[state] = state_count[state] + 1
        state_list[j] = state

    state_avg = state_count / n_exp

    u = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

    diff = np.linalg.norm(u - state_avg, 1)

    print(f"pi_1 = {state_avg}\n")
    print(f"p1 Diff= {diff * 0.5}\n\n")

    plt.hist(state_list, bins = 5, density = False, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title("State Frequency of Random Walk on C_5")
    plt.xlabel("State")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("hw6_p1.png")
    plt.show()



####################################################################################################
###                                        Problem 2                                             ###
####################################################################################################

p2 = True
if p2:

    ### Nearest Neighbor
    n_exp = int(1e5)

    nbh_state_list = np.zeros(n_exp)
    nbh_state_count = np.zeros(5)
    nbh_state = int(np.round(5 * np.random.rand() - 0.5))

    for j in range(n_exp):
        if nbh_state == 0:
            nbh_state = 1
            nbh_state_count[1] = nbh_state_count[1] + 1
        elif nbh_state == 4:
            nbh_state = 3
            nbh_state_count[3] = nbh_state_count[3] + 1
        else:
            u = int(np.round(np.random.rand()))
            if u:
                nbh_state = nbh_state + 1
                nbh_state_count[nbh_state] = nbh_state_count[nbh_state] + 1
            else:
                nbh_state = nbh_state - 1
                nbh_state_count[nbh_state] = nbh_state_count[nbh_state] + 1
        nbh_state_list[j] = nbh_state

    nbh_state_avg = nbh_state_count * (1/n_exp)
    nbh_state_theo = np.array([0.125, 0.25, 0.25, 0.25, 0.125])
    nbh_diff = np.linalg.norm(nbh_state_avg - nbh_state_theo, 1)

    print(f"NN Diff = {nbh_diff}\n")
    print(f"pi_nbh = {nbh_state_avg}\n")

    plt.hist(nbh_state_list, bins = 5, density = False, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title("State Frequency of a Random Walk on the Nearest Neighbor Graph")
    plt.xlabel("State")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("hw6_p2_nbh.png")
    plt.show()


    ### Star Map 
    n_exp = int(1e5)

    star_state_list = np.zeros(n_exp)
    star_state_count = np.zeros(6)
    star_state = int(np.round(6 * np.random.rand() - 0.5))

    for j in range(n_exp):
        if star_state != 0:
            star_state = 0
            star_state_count[0] = star_state_count[0] + 1
        else:
            star_state = int(np.round(5 * np.random.rand() + 0.5))
            star_state_count[star_state] = star_state_count[star_state]  + 1
            star_state_list[j] = star_state

    star_state_avg = star_state_count * (1/n_exp)
    star_state_theo = np.array([0.5, 0.1, 0.1, 0.1, 0.1, 0.1])
    star_diff = np.linalg.norm(star_state_avg - star_state_theo, 1)


    print(f"star_diff = {star_diff}\n")
    print(f"pi_star = {star_state_avg}\n\n")

    plt.hist(star_state_list, bins = 6, density = False, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title("State Frequency of a Random Walk on K_{1,5}")
    plt.xlabel("State")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("hw6_p2_star.png")
    plt.show()



####################################################################################################
###                                        Problem 3                                             ###
####################################################################################################


p3 = True
if p3:
    N = 10
    S = np.arange(N+1)

    beta = 0.5
    gamma = 0.5
    dt = 1/6

    lam = np.zeros(N)
    mu = np.zeros(N)

    for k in range(N):
        lam[k] = beta * (N-k)
        mu[k] = gamma * (k+1)
    mu[-1] = 0


    n_exp = int(1e5)

    state = int(np.round(11*np.random.rand() - 0.5))
    state_count = np.zeros(N+1)
    bd_state_list = np.zeros(n_exp)
    bd_state_list[0] = state
    update = 0

    while update < n_exp-1:
        move = False
        u = np.random.rand()
        if state != 10 and state != 0:
            if u<= lam[state]*dt:
                state = state + 1
                state_count[state] = state_count[state] + 1
                update += 1
                move = True
            elif u<= mu[state -1]*dt :
                state = state - 1
                state_count[state] = state_count[state] + 1
                update += 1
                move = True
            else:
                state = state
        elif state == 10:
            state = 0
            state_count[0] = state_count[0] + 1
            update += 1
            move = True
        else:
            state = 1
            state_count[state] = state_count[state] + 1
            update += 1
            move = True
        if move:
            bd_state_list[update] = state


    
    state_avg = state_count * (1/n_exp)
    print(f"pi_3 = {state_avg}\n")

    plt.hist(bd_state_list, bins = 11, density = False, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title("State Frequency of a Random Walk on Birth-Death Walk")
    plt.xlabel("State")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("hw6_p3.png")
    plt.show()

