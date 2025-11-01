import numpy as np
import matplotlib.pyplot as plt

n_iter = int(1e5) 
burn = int(1e4)

state_save_0 = np.zeros(n_iter - burn)
state_save_1 = np.zeros(n_iter - burn)

#Burn in
state_current_0 = 0
state_current_1 = 0
eps = 0
beta = [0, 1.5]
n = 60


def update_state(x_current):
    u = np.random.rand()
    if u<= (1-eps)/2:
        x_new = (x_current - 1) % n
    elif u <= 1-eps:
        x_new = (x_current + 1) % n
    else:
        x_new = x_current
    return x_new


def target_distribution_1(x):
    return np.exp(beta[1] * np.cos(2*np.pi*x/n))

accept_count = 0

state_count_0 = np.zeros(60)
state_count_1 = np.zeros(60)

#burn in for both variables
for k_burn in range(burn):
    #beta = 0
    state_proposal_0 = update_state(state_current_0)
    acceptance_ratio_0 = 1
    state_current_0 = state_proposal_0

    #beta = 1.5
    state_proposal_1 = update_state(state_current_1)
    acceptance_ratio_1 = target_distribution_1(state_proposal_0)/target_distribution_1(state_current_0)
    u = np.random.rand()
    if u< np.min([1, acceptance_ratio_1]):
        state_current_1 = state_proposal_1
        accept_count += 1
    else:
        state_current_1 = state_current_1

#MH: beta = 0

for k_run in range(n_iter - burn):
    state_current_0 = update_state(state_current_0)
    state_save_0[k_run] = state_current_0
    state_count_0[state_current_0] = state_count_0[state_current_0] + 1


for k_run in range(n_iter - burn):
    state_proposal_1 = update_state(state_current_1)
    acceptance_ratio_1 = target_distribution_1(state_proposal_1)/target_distribution_1(state_current_1)
    u = np.random.rand()
    if u< np.min([1, acceptance_ratio_1]):
        state_current_1 = state_proposal_1
        accept_count += 1
    else:
        state_current_1 = state_current_1
    state_save_1[k_run] = state_current_1
    state_count_1[state_current_1] = state_count_1[state_current_1] + 1

print(accept_count/n_iter)
print(state_count_0 / np.linalg.norm(state_count_0, 1))
print(state_count_1 / np.linalg.norm(state_count_1, 1))

u_exp_0 = (state_count_0 / np.linalg.norm(state_count_0, 1))
u_theor_0 = 1/60 * np.ones(60)
val = 0.5*np.linalg.norm(u_theor_0 - u_exp_0, 1)

print(val)
x_ran = np.linspace(0,60,100)
plt.hist(state_save_0, bins = 60, density = True, alpha=0.7, color='skyblue', edgecolor='black')
plt.plot(x_ran, np.ones(100)/60, c = 'r')
plt.title(f"MH MCMC Model on C_60, eps = {eps}, beta = {beta[0]}")
plt.xlabel("Sample")
plt.ylabel("Density")
plt.grid(True)
plt.savefig("hw7_p3.png")
plt.show()

plt.hist(state_save_1, bins = 60, density = True, alpha=0.7, color='skyblue', edgecolor='black')
plt.plot(x_ran, target_distribution_1(x_ran)/100, c = 'r')
plt.title(f"MH MCMC Model on C_60, eps = {eps}, beta = {beta[1]}")
plt.xlabel("Beta")
plt.ylabel("Density")
plt.grid(True)
plt.savefig("hw7_p4.png")
plt.show()

print(state_current_0)


# For run in 

