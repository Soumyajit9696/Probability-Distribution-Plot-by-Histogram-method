#=======================#
# LOGISTIC DISTRIBUTION #
#=======================#

import matplotlib.pyplot as plt
import numpy as np


loc, scale, nbin,npts = 10., 1., 50, 10000
s = np.random.logistic(loc, scale, npts);
#count, bins, inored = plt.hist(s,bins = 50)
bins = 50

def logistic(x, loc, scale):
    return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
largest_value = logistic(bins, loc, scale)
#plt.subplot(2,2,1)
nn, bins, patches = plt.hist(s, nbin, density=True, color='skyblue', edgecolor='black', label=r'$N=$'+str(npts))
#plt.plot(bins, largest_value * count.max() / largest_value.max())
plt.plot(bins, np.exp((loc-bins)/scale)/(scale*(1+np.exp((loc-bins)/scale))**2),color = 'crimson',linewidth = '2',label = r"$P(x) = \frac{e^{\frac{-(x-\mu)}{s}}}{s(1+e^{\frac{-(x-\mu)}{s}})^2}$")
plt.legend(loc = 'best',prop={'size':15})
plt.grid(axis='y')
plt.xlim([min(bins), max(bins)])
plt.xlabel('X')
plt.ylabel(r'$P_{Logistic}(x)$')
plt.show()
