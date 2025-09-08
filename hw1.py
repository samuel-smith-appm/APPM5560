import numpy as np 

Nsims = 100000
Ntrials = 10
results = np.zeros(Ntrials)

for k in range(Ntrials):
    xyz = np.random.rand(Nsims, 3)

    count = 0
    for ind, val in enumerate(xyz):
        if (val[0]**2 + val[1]**2 < val[2]) and (val[0]*val[1] < val[2]**3):
            count += 1
    results[k] = count/Nsims

print(results)
print(np.average(results))


