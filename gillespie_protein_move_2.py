import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import statistics

# N = list(range(101))
# N = list(filter(lambda num: num != 0, N))
N = [0, 1]
t = [0]
ave_N = []

tend = 1000

# forward rate
k = 5
# dissociation rate
delta = 2
# backward rate
gamma = 8

rates = [k, gamma, delta]
rate_sum = sum(rates)

for i in range(50000):
    while t[-1] < tend:

        current_N = N[-1]

        # rates = [k, delta] # take out of loop
        # rate_sum = sum(rates)

        # choosing time-point for next event
        ts = np.random.exponential(scale=1/rate_sum)
        t.append(t[-1] + ts)

        rand = random.uniform(0, 1)

        # forward movement event
        if rand * rate_sum > 0 and rand * rate_sum < rates[0]:
            N.append(N[-1] + 1)

        # backward movement event
        elif rand * rate_sum > rates[0] and rand * rate_sum < rates[0] + rates[1]:
            N.append(N[-1] - 1)

        # detachment event
        else:
            # print("N-steps:", N)
            # print("time-steps:", t)
            # print("\n")
            # print("Total N-steps in this iteration:", len(N))
            # print("Time steps in the iteration:", len(t))
            # print("\t")
            # ave_N.append(len(N))
            break
    ave_N.append(N[-1])

    plt.plot(t, N)
    N = [0, 1]
    t = [0]


for i in range(len(ave_N)):
    ave_N[i] = ave_N[i] - 1
plt.xlabel("time")
plt.ylabel("N-steps")
plt.savefig("N_vs_t-plot.pdf")
print("*** Average distance moved forward by the motor protein:",
      statistics.mean(ave_N), "***")
print ("\n")

# Calculating frequency
freq = {}
for item in ave_N:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

#for key, value in freq.items():
 #       print ("% d : % d"%(key, value))

#Frequency Plot        
#n_steps = pd.DataFrame(freq.items(), columns=['Steps','Frequency'])
#n_steps = n_steps[['Frequency', 'Steps']]
#cols = list(n_steps.columns.values)
#print(n_steps)
plt.bar(list(freq.keys()), freq.values(), color='b')
plt.xlabel("N-Steps")
plt.ylabel("Frequency")
plt.savefig("Frequency_dist_with_backward-step.pdf")
