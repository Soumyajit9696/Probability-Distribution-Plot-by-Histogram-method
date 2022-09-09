#========================#
# LOGNORMAL DISTRIBUTION #
#========================#

import numpy as np
import matplotlib.pyplot as plt

mu ,sigma ,s ,nbin= 3, 1,6000 ,50# Mean and Standard Deviation
s = np.random.lognormal(mu, sigma, 1000)
bins = 6000
count, bins, ignored = plt.hist(s, 100,density = True,align ='mid')

x = np.linspace(min(bins),max(bins),1000)
pdf = (np.exp(-(np.log(x)-mu)**2/(2*sigma**2))/(x * sigma * np.sqrt(2*np.pi)))
nn, bins, patches = plt.hist(s, nbin, density=True, color='darkorange', edgecolor='teal', label=r'$s=$'+str(s.size));
plt.plot(x,pdf,linewidth = 2,c = 'r',label=r'$p(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{(\frac{(\ln(x)-\mu)^2}{2\sigma^2})}$')
plt.axis('tight')
plt.legend(loc='best',prop={'size':8})
plt.xlabel("x",size = 15)
plt.ylabel("$p_(Lognormal)$")

plt.show()
