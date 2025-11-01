import numpy as np

####################################################################################################
###                                        Problem 1                                             ###
####################################################################################################
np.random.seed(17)
N= int(1e2)
state_arr = np.zeros(N)
U = np.random.rand(N)
state = 100
for ind, val in enumerate(U):
    #update array
    state_arr[ind] = state
    if val<= 0.75:
        if state > 0:
            state = state - 1
        else:
            state = 0
    else:
        state += 1
print(state_arr)