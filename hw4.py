import numpy as np
import matplotlib.pyplot as plt

N = 10000
initial_states = [1,2,3]
h_i = np.zeros(3)
g_i = np.zeros(3)
tau_4_i = np.zeros(3)
tau_0_i = np.zeros(3)
alpha = 1/4



first20 = np.zeros((20,3))
first20[0] = np.array([1,2,3])


# for ind, x0 in enumerate(initial_states):
#     hit4 = 0
#     hit0 = 0
    
#     time0 = []
#     time4 = []
#     time_abs = np.zeros((N))
#     for j in range(N):
#         state = x0
#         time = 0
#         cont = True
#         while cont:
#             u = np.random.rand()
#             # Update state
#             if state == 1:
#                 if u <= 1-alpha:
#                     state = 0
#                 else:
#                     state = 2
#             elif state ==2:
#                 if u<= 0.5:
#                     state = 1
#                 else:
#                     state = 3
#             elif state == 3: 
#                 if u <= 1- alpha:
#                     state = 4
#                 else:
#                     state = 2
#             else:
#                 print("something went horribly wrong")
#             if j<19:
#                 first20[j+1, ind] = state
#             # update time 
#             time += 1
#             #stopping condition
#             if state == 0:
#                 hit0 += 1
#                 time0.append(time)
#                 time_abs[j] = time
#                 cont = False
#             elif state == 4:
#                 hit4 += 1
#                 time4.append(time)
#                 time_abs[j] = time
#                 cont = False
#     h_i[ind] = hit4/N
#     g_i[ind] = np.average(time)
#     tau_0_i[ind] = np.average(time0)
#     tau_4_i[ind] = np.average(time4)

print("debug stop")

first20 = np.zeros((20,3))
first20[0] = np.array([1,2,3])

kmax = 0
end4 = [0,0,0]
end_iter = [0,0,0]
for ind, x0 in enumerate(initial_states):
    hit4 = 0
    hit0 = 0
    
    time0 = []
    time4 = []
    time_abs = np.zeros((N))
    state = x0
    time = 0
    cont = True
    k=0
    while cont:
        u = np.random.rand()
        # Update state
        if state == 1:
            if u <= 1-alpha:
                state = 0
            else:
                state = 2
        elif state ==2:
            if u<= 0.5:
                state = 1
            else:
                state = 3
        elif state == 3: 
            if u <= 1- alpha:
                state = 4
            else:
                state = 2
        else:
            print("something went horribly wrong")
        if k < 19:
            first20[k+1, ind] = state
        k+= 1
        # update time 
        time += 1
        #stopping condition
        if state == 0:
            kmax = max(k, kmax)
            cont = False
        elif state == 4:
            kmax = max(k, kmax)
            cont = False
            end4[ind] = 1 
            end_iter[ind] = k


for n in range(3):
    if end4[n]:
        first20[end_iter[n]:, n] = 4



print(first20)
first20 = first20[:kmax+1,:]
print(kmax)

print(first20)

if kmax >= 4:
    kran = np.linspace(0, kmax, kmax+1)
    plt.plot(kran, first20[:,0], c= 'r')
    plt.plot(kran, first20[:,1], c= 'b')
    plt.plot(kran, first20[:,2], c= 'g')
    plt.scatter(kran, first20[:,0], c= 'r')
    plt.scatter(kran, first20[:,1], c= 'b')
    plt.scatter(kran, first20[:,2], c= 'g')
    plt.xlabel("Iteration")
    plt.ylabel("State")
    plt.title("Sample Run")
    plt.show()
else:
    print("run again bozo")


# u = int(np.round(np.random.rand()))

# state = 1
# if state == 1:
#     if u:
#         print("updated state")
#         state = 2
#     else:
#         print("updated state")
#         state = 3
# elif state ==2:
#     print("fuck")
# elif state == 3:
#     print("still fuck but whatever")
# else:
#     print('*w*')

