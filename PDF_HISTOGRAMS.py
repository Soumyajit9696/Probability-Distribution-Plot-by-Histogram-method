import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sps      # For Gamma function   
import matplotlib.pyplot as plt
#from scipy.misc import factorial



#==========================#
# Exponential Distribution #
#==========================#
scale, size, nbin = 1.0, 6000, 20  # Scale Parameter (inverse of Rate Parameter), size and how many bins  
N = np.random.exponential(scale, size);
plt.subplot(2,2,1)
n, bins, patches = plt.hist(N, nbin, density=True, color='mediumblue', edgecolor='red', label=r'$N=$'+str(N.size));
plt.plot(bins, 1/scale*np.exp(-bins/scale), linewidth=2, color='k', label=r'$P(x) = \frac{1}{\beta}e^{-x/\beta}$')
plt.legend(loc='best',prop={'size':8})
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)]); plt.xlabel('x', size=10); plt.xticks(size=4)
plt.ylabel('$P_{Exp}(x)$', size=10); plt.yticks(size=4)

#=======================#
# Gaussian Distribution #
#=======================#
npts, nbin = 6000, 40; # Total Number of Points & Bins
mu, sigma = 0.0, 10;  # Mean & Standard Deviation of PDF
x = np.random.normal(mu, sigma, npts)
plt.subplot(2,2,2)
n, bins, patches = plt.hist(x, nbin, density=True, color='fuchsia', edgecolor='lime', label=r'$N=$'+str(npts))
plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)),
         linewidth=2, color='k',label=r'$P(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{(x-\mu)^2/{2\sigma^2}}$') 
plt.legend(loc='best',prop={'size':8})
plt.title(r'$\mu='+str(mu)+',\ \sigma='+str(sigma)+'$', size=8)
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)])
plt.xlabel('x', size=10); plt.xticks(size=4)
plt.ylabel('$P_{Gauss}(x)$', size=10)

#======================#
# Laplace Distribution #
#======================#
npts, nbin = 6000, 40; 
mu, b = 0.0, 4.0;  
x = np.random.laplace(mu, b, npts)
plt.subplot(2,2,3)
n, bins, patches = plt.hist(x, nbin, density=True, color='coral', edgecolor='black', label=r'$N=$'+str(npts))
plt.plot(bins, np.exp(-np.abs(bins-mu)/b)/(2*b), linewidth=2, color='k',label=r'$P(x) = \frac{1}{2b} e^{\frac{-|x-\mu|}{b}}$') 
plt.legend(loc='best',prop={'size':8})
plt.grid(axis='y')
plt.xlim([min(bins), max(bins)])
plt.xlabel('x', size=10)
plt.xticks(size=4)
plt.ylabel('$P_{Laplace}(x)$', size=10)
plt.yticks(size=4)

#===================#
# Beta Distribution #
#===================#
npts, nbin = 6000, 30; 
alpha, beta = 2.0,2.0
x = np.random.beta(alpha,beta, npts);
plt.subplot(2,2,4)
n, bins, patches = plt.hist(x, nbin, density=True, color='lime', edgecolor='black', label=r'$N=$'+str(npts))
plt.plot(bins, (bins**(alpha-1))*((1-bins)**(beta-1))/sps.beta(alpha,beta), linewidth=2, color='blue',label=r'$P(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$') 
plt.legend(loc='best',prop={'size':8})
plt.grid(axis='y')
plt.xlim([min(bins), max(bins)])
plt.xlabel('x', size=10)
plt.ylabel('$P_{Beta}(x)$', size=10)
plt.show()


