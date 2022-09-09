'''
CU roll : 203012-21-0006
CU reg : 012-1111-0451-20
'''
# Plotting Of Different Probability Distribution Function Using Histogram
import numpy as np
import matplotlib.pyplot as plt
#========================#
# LOGNORMAL DISTRIBUTION #
#========================#
mu ,sigma ,s ,nbin= 3, 1,6000 ,50# Mean and Standard Deviation
s = np.random.lognormal(mu, sigma, 1000)
bins = 6000
count, bins, ignored = plt.hist(s, 100,density = True,align ='mid')
plt.subplot(2,2,1)
x = np.linspace(min(bins),max(bins),1000)
pdf = (np.exp(-(np.log(x)-mu)**2/(2*sigma**2))/(x * sigma * np.sqrt(2*np.pi)))
nn, bins, patches = plt.hist(s, nbin, density=True, color='darkorange', edgecolor='teal', label=r'$s=$'+str(s.size));
plt.plot(x,pdf,linewidth = 2,c = 'r',label=r'$p(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{(\frac{(\ln(x)-\mu)^2}{2\sigma^2})}$')
plt.axis('tight')
plt.legend(loc='best',prop={'size':15})
plt.xlabel("x",size = 15)
plt.ylabel("$p_(Lognormal)$")

#=======================#
# LOGISTIC DISTRIBUTION #
#=======================#

loc, scale, nbin,npts = 10., 1., 50, 10000
s = np.random.logistic(loc, scale, npts);
#count, bins, inored = plt.hist(s,bins = 50)
bins = 50

def logistic(x, loc, scale):
    return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
largest_value = logistic(bins, loc, scale)
plt.subplot(2,2,2)
nn, bins, patches = plt.hist(s, nbin, density=True, color='skyblue', edgecolor='black', label=r'$N=$'+str(npts))
#plt.plot(bins, largest_value * count.max() / largest_value.max())
plt.plot(bins, np.exp((loc-bins)/scale)/(scale*(1+np.exp((loc-bins)/scale))**2),color = 'crimson',linewidth = '2',label = r"$P(x) = \frac{e^{\frac{-(x-\mu)}{s}}}{s(1+e^{\frac{-(x-\mu)}{s}})^2}$")
plt.legend(loc = 'best',prop={'size':15})
plt.grid(axis='y')
plt.xlim([min(bins), max(bins)])
plt.xlabel('X')
plt.ylabel(r'$P_{Logistic}(x)$')



#==========================#
# LOGSERIES DISTRIBUTION   #
#--------------------------#

a,nbin, npts ,binwidth = .6,20, 10000,20
s = np.random.logseries(a, npts)
#bins = 50
#count, bins, ignored = plt.hist(s)
plt.subplot(2,2,3)

#def logseries(p, npts):
  #  return -p**npts/(npts*np.log(1-p))
n, bins, patches = plt.hist(s, nbin, density=True, color='mediumspringgreen', edgecolor='red', label=r'$N=$'+str(npts))
#plt.plot(bins, logseries(bins, a)*count.max()/logseries(bins, a).max(),c='r',label='hh')
plt.plot(bins,-a**bins/(bins*np.log(1-a)),linewidth = '2',label=r'$P(k) = \frac{-p^{k}}{k\ln(1-p)}$',color = 'darkblue')
plt.legend(loc='best',prop={'size':15})
plt.grid(axis='y')
plt.xlabel('x')
plt.ylabel(r'$P_{Logseries}(x)$')
plt.xlim([min(bins), max(bins)])

#=====================#
# Pareto Distribution #
#=====================#

a, m = 3., 2. # shape and mode
nbin, npts = 20,6000
s = (np.random.pareto(a, 1000) + 1)*m # m

plt.subplot(2,2,4)
count, bins, patches =plt.hist(s, nbin, density=True, color='olive', edgecolor='red', label=r'$N=$'+str(npts))
plt.plot(bins, a*m**a / bins**(a+1),label = r'$P(X)=\frac{am^a}{x^{(a+1)}}$')
#plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
plt.grid(axis = 'y')
plt.ylabel(r'$P_{Pareto}(x)$')
plt.legend(loc='best',prop={'size':15})
plt.xlabel('x')
plt.show()





