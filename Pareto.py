#=====================#
# Pareto Distribution #
#=====================#



import matplotlib.pyplot as plt
import numpy as np

a, m = 3., 2. # shape and mode
nbin, npts = 20,6000
s = (np.random.pareto(a, 1000) + 1)*m # m


count, bins, patches =plt.hist(s, nbin, density=True, color='olive', edgecolor='red', label=r'$N=$'+str(npts))
plt.plot(bins, a*m**a / bins**(a+1),label = r'$P(X)=\frac{am^a}{x^{(a+1)}}$')
#plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
plt.legend(loc = 'best')
plt.grid(axis = 'y')
plt.ylabel(r'$P_{Pareto}(x)$')
plt.xlabel('x')
plt.show()
