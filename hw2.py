import numpy as np
import matplotlib.pyplot as plt
from time import time

#np.random.seed(17)

####################################################################################################
###                                        Problem 1                                             ###
####################################################################################################

p1 = True
if p1:
    alpha = 3
    n_list = [100, 1000, 100000]
    f = lambda x: alpha * x **(alpha-1)
    xran = np.linspace(0, 1, 1000)

    for ind, N in enumerate(n_list):
        res = np.zeros(N)
        for j in range(N):
            u = np.random.rand()
            res[j] = u**(1/alpha)
        plt.hist(res, bins=int(3*np.log10(N)), density=True, alpha=0.7, color='skyblue', edgecolor='black')
        plt.plot(xran, f(xran), c = 'r')
        plt.xlabel('Value of X')
        plt.ylabel('Density')
        plt.title('(1) Empirical Distribution of Random Variable X')
        plt.text(
            x=0.05, y=0.95,
            s=f'Number of samples: {N}',
            transform=plt.gca().transAxes,
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3')
        )

        plt.grid(True)
        plt.savefig(f"hw2_p1_N{N}.png")
        plt.show()




####################################################################################################
###                                        Problem 2                                             ###
####################################################################################################
p2 = True
if p2:
    n_list = [100, 1000, 100000]
    f = lambda x: x*np.exp(-(x**2)/2)
    xran = np.linspace(0, 5, 1000)
    for ind, N in enumerate(n_list):
        res = np.zeros(N)
        for j in range(N):
            u = np.random.rand()
            res[j] = np.sqrt(np.log(1/((1-u)**2)))
        plt.hist(res, bins=int(3*np.log10(N)), density=True, alpha=0.7, color='skyblue', edgecolor='black')
        plt.plot(xran, f(xran), c = 'r')
        plt.xlabel('Value of X')
        plt.ylabel('Density')
        plt.title('(2) Empirical Distribution of Random Variable X')
        plt.text(
            x=0.95, y=0.95,
            s=f'Number of samples: {N}',
            transform=plt.gca().transAxes,
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

        plt.grid(True)
        plt.savefig(f"hw2_p1_2{N}.png")
        plt.show()


####################################################################################################
###                                        Problem 3                                             ###
####################################################################################################
p3 = True
if p3:
    nsamples = 1000
    res = np.zeros(nsamples)
    n1 = 0
    n2 = 0
    n3 = 0
    for j in range(nsamples):
        u = np.random.rand()
        if u<= 0.78:
            res[j] = 2
            n2+= 1
        elif u <= 0.98:
            res[j] = 3
            n3 += 1
        else:
            res[j] = 1
            n1 += 1
    plt.hist(res, bins=3 , density=True, alpha=0.7, color='skyblue', edgecolor='black')
    plt.xlabel('Value of Sampled Z')
    plt.ylabel('Density')
    plt.title('(3) Empirical Frequency of Sampled Z')
    plt.text(
        x=0.05, y=0.95,
        s=f'Number of samples: {100}',
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='left',
        bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

    plt.grid(True)
    plt.savefig("hw2_p3.png")
    plt.show()

    print(f"Empirical Frequency of 1: {n1/nsamples}\n")
    print(f"Empirical Frequency of 2: {n2/nsamples}\n")
    print(f"Empirical Frequency of 3: {n3/nsamples}\n")


####################################################################################################
###                                        Problem 4                                             ###
####################################################################################################



p4 = True
if p4:
    def accept_reject_standard(pdf, M, L):
        """
        run accept reject on pdf f
        """
        x = L * np.random.rand()
        y = M* np.random.rand()
        reject_count = 0
        while y > pdf(x):
            reject_count +=1
            x = L * np.random.rand()
            y = M* np.random.rand()
        run_count = reject_count + 1
        return (x, run_count)

    def accept_reject_modified(comp, G_inv):
        """
        run accept reject on pdf f with modified proposal function g
        """
        u = np.random.rand()
        x = G_inv(u)
        y = np.random.rand()
        reject_count = 0
        while y> comp(x):
            reject_count +=1
            u = np.random.rand()
            x = G_inv(u)
            y = np.random.rand()
        run_count = reject_count + 1
        return (x, run_count)

    def pdf(x):
        return (5/3) * (1-x) * (1 + 2*(x**3))
    # standard:
    n_list = [1000, 10000]
    run_count_standard = [0,0]
    time_standard = [0,0]
    xran = np.linspace(0, 1, 100)


    for ind, N in enumerate(n_list):
        t0 = time()
        x_dist = np.zeros(N)
        for j in range(N):
            (x_dist[j], run_j) = accept_reject_standard(pdf, 5/3, 1)
            run_count_standard[ind] = run_count_standard[ind] + run_j
        time_standard[ind] = time() - t0
        plt.hist(x_dist, bins=round(2*np.log10(N)**2) , density=True, alpha=0.7, color='skyblue', edgecolor='black')
        plt.plot(xran, pdf(xran), c = 'r')
        plt.xlabel('Generated X')
        plt.ylabel('X')
        plt.title('(4c) Generated Accept-Reject esimation of PDF')
        plt.text(
            x=0.95, y=0.95,
            s=f'Number of samples: {N}',
            transform=plt.gca().transAxes,
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

        plt.grid(True)
        plt.savefig(f"hw2_p4_N{N}_stand.png")
        plt.show()


    def g_prop(x):
        return (3/2) * np.sqrt(1-x)

    def G_inv(w):
        return 1 - w**(2/3)

    def comp(x):
        return (80/81) * np.sqrt(1-x) * (1 + 2*(x**3))


    n_list = [1000, 10000]
    run_count_mod = [0,0]
    time_mod = [0,0]

    for ind, N in enumerate(n_list):
        t0 = time()
        x_dist = np.zeros(N)
        for j in range(N):
            (x_dist[j], run_j) = accept_reject_modified(comp, G_inv)
            run_count_mod[ind] = run_count_mod[ind] + run_j
        time_mod[ind] = time() - t0
        plt.hist(x_dist, bins=round(2*np.log10(N)**2) , density=True, alpha=0.7, color='skyblue', edgecolor='black')
        plt.plot(xran, pdf(xran), c = 'r')
        plt.xlabel('Generated X')
        plt.ylabel('Density')
        plt.title('(4d) Modified Generated Accept-Reject esimation of PDF')
        plt.text(
            x=0.95, y=0.95,
            s=f'Number of samples: {N}',
            transform=plt.gca().transAxes,
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

        plt.grid(True)
        plt.savefig(f"hw2_p4_N{N}_mod.png")
        plt.show()


    avg_sample_time_standard = (time_standard[0]/1000 + time_standard[1]/10000)/2
    avg_sample_time_mod = (time_mod[0]/1000 + time_mod[1]/10000)/2

    acceptance_ratio_standard = 11000/(np.sum(np.array(run_count_standard)))
    acceptance_ratio_mod = 11000/(np.sum(np.array(run_count_mod)))


    print(f"(c) Mean time to generate accepted sample: {avg_sample_time_standard} (s)")
    print(f"(d) Mean time to generate accepted sample: {avg_sample_time_mod} (s)\n")

    print(time_standard)
    print(time_mod)

    print(f"\n(c) Empirical Acceptance Ratio: {acceptance_ratio_standard}")
    print(f"(d) Empirical Acceptance Ratio: {acceptance_ratio_mod}\n")


    print(run_count_standard)
    print(run_count_mod)

