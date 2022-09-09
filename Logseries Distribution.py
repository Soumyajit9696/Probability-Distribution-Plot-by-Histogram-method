


#==========================#
# LOGSERIES DISTRIBUTION   #
#--------------------------#

import matplotlib.pyplot as plt
import numpy as np

a,nbin, npts ,binwidth = .6,20, 10000,20
s = np.random.logseries(a, npts)
#bins = 50
#count, bins, ignored = plt.hist(s)


#def logseries(p, npts):
  #  return -p**npts/(npts*np.log(1-p))
n, bins, patches = plt.hist(s, nbin, density=True, color='mediumspringgreen', edgecolor='red', label=r'$N=$'+str(npts))
#plt.plot(bins, logseries(bins, a)*count.max()/logseries(bins, a).max(),c='r',label='hh')
plt.plot(bins,-a**bins/(bins*np.log(1-a)),linewidth = '2',label=r'$P(k) = \frac{-p^{k}}{k\ln(1-p)}$',color = 'darkblue')
plt.legend(loc ='best')
plt.grid(axis='y')
plt.xlim([min(bins), max(bins)])
plt.show()
