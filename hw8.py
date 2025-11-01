import numpy as np
import matplotlib.pyplot as plt
from math import factorial

####################################################################################################
###                                        Problem 1                                             ###
####################################################################################################

###   (1.d.i)

p1 = True

def draw_interarrivaltime(lam):
    u = np.random.rand()
    x = -1*np.log(u)/lam
    return x

def simulate_single_team(lam, T):
    score = 0
    current_time = [0]
    cont = True

    while cont:
        score_time = draw_interarrivaltime(lam)
        if current_time[-1] + score_time <= T:
            current_time.append(current_time[-1] + score_time)
        else:
            cont = False
    # populate score arrays
    score_arr = np.zeros(int(T))
    counter = 1
    score = 0
    current_time.append(48)
    current_time = np.array(current_time)
    for k in range(1, int(T)+1):
        while current_time[counter] < k:
            score += 2
            counter += 1
        score_arr[k-1] = score


    return current_time, score_arr


def simulate_full_game(lam, T):
    current_time = [0]
    cont = True

    while cont:
        score_time = draw_interarrivaltime(2 * lam)
        if current_time[-1] + score_time <= T:
            current_time.append(current_time[-1] + score_time)
        else:
            cont = False
    
    # populate score arrays
    score_arr_A = np.zeros(int(T))
    score_arr_B = np.zeros(int(T))
    counter = 1
    score_A = 0
    score_B = 0
    current_time.append(48)
    current_time = np.array(current_time)
    for k in range(1, int(T)+1):
        while current_time[counter] < k:
            u = int(np.round(np.random.rand()))
            if u:
                score_A += 2
            else:
                score_B += 2
            counter += 1
        score_arr_A[k-1] = score_A
        score_arr_B[k-1] = score_B

    return score_arr_A, score_arr_B


if p1:
    lam = 3
    T = 48

    A_timeline_1, A_score_1 = simulate_single_team(lam,T)
    B_timeline_1, B_score_1 = simulate_single_team(lam,T)


    bars = np.arange(48)
    bar_width = 0.5
    fig, ax = plt.subplots(figsize = (16,12))
    rects1 = ax.bar(bars - bar_width/2, A_score_1, bar_width, label = 'Team A', color = 'r', edgecolor = 'black')
    rects2 = ax.bar(bars + bar_width/2, B_score_1, bar_width, label = 'Team B', color = 'b', edgecolor = 'black')
    ax.set_ylabel('Score')
    ax.set_xlabel('Minute')
    ax.set_title('Event-time Plot: Method 1')
    ax.set_xticks(bars)
    ax.legend()
    plt.savefig("hw8_p1_1.png")
    plt.show()


    #method 2

    A_score_2, B_score_2 = simulate_full_game(lam, T)

    bars = np.arange(48)
    bar_width = 0.5
    fig, ax = plt.subplots(figsize = (16,12))
    rects1 = ax.bar(bars - bar_width/2, A_score_2, bar_width, label = 'Team A', color = 'r', edgecolor = 'black')
    rects2 = ax.bar(bars + bar_width/2, B_score_2, bar_width, label = 'Team B', color = 'b', edgecolor = 'black')
    ax.set_ylabel('Score')
    ax.set_xlabel('Minute')
    ax.set_title("Event Time Plot: Method 2")
    ax.set_xticks(bars)
    ax.legend()
    plt.savefig("hw8_p1_2.png")
    plt.show()

### (1.d.ii)


lam = 3
T = 48

def generate_poisson(lam):
    u = np.random.poisson(lam)
    return u

def distribute_poisson(lam, T):
    n_events = generate_poisson(lam * T)
    dist = T * np.random.rand(n_events)
    return dist, n_events


n_trials = int(1e5)
D = np.zeros(n_trials)
A_win = 0
B_win = 0
tie = 0
for j in range(n_trials):
    N = generate_poisson(2*lam * T)
    X = np.random.binomial(N, 0.5)
    D[j] = 4*X - 2*N
    if D[j]>0:
        A_win += 1
    elif D[j]<0:
        B_win += 1
    else:
        tie += 1

d_pos = A_win/n_trials
d_neg = B_win/n_trials
d_zero = tie/n_trials
d_expec = np.average(D)
d_var = np.var(D)
comp = np.abs(d_var - 8 * lam * T)

print(f"P(D>0) = {d_pos}\nP(D<0) = {d_neg}\nP(D=0) = {d_zero}\nE[D] = {d_expec}\nVar(D) = {d_var}\n|Var(D) - 8*\lam*T| = {comp}\n\n")


####################################################################################################
###                                        Problem 2                                             ###
####################################################################################################
alpha = 0.01 
beta = 0.0005

def big_lambda(t, alpha = 0.01, beta = 0.0005):
    return alpha * t + 0.5*beta*t**2

n_exp = int(1e5)
N = np.zeros(n_exp)
score_time = []

for k in range(n_exp):
    N[k] = np.random.poisson(big_lambda(90))
    for j in range(int(N[k])):
        u = big_lambda(90)* np.random.rand()
        T = (np.sqrt(alpha **2 + (2 * beta * u)) - (alpha))/(beta)
        score_time.append(T)

N_expec = np.average(N)
N_var = np.var(N)
t = np.linspace(0, 90, 100)
lam_t = 0.3333333*(alpha + (beta * t))


plt.hist(np.array(score_time), bins = 30, density = True, alpha = 0.7, color = "skyblue", edgecolor = 'black')
plt.grid(True)
plt.plot(t, lam_t, c = 'r')
plt.xlabel("Score Time (min)")
plt.ylabel("Density")
plt.title("Density Histogram of Score Times")
plt.savefig("hw8_p2.png")
plt.show()

print(f"\n\nE[N] = {N_expec}\nVar(N) = {N_var}\n")



####################################################################################################
###                                        Problem 3                                             ###
####################################################################################################