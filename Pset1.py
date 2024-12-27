import matplotlib.pyplot as plt
import numpy as np


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

Pr_H2O = 4.6
Pr_air = 0.709

x = np.linspace(0,1)
print(x)

'''water'''
ax1.plot(x, 0.005*np.sqrt(x), c = 'k', label='water')
ax1.plot(x, 0.005*np.sqrt(x)* (Pr_H2O)**(-1/3), c='r', label='water, thermal b.l.')

'''air'''
ax1.plot(x, 0.005*np.sqrt(x)*np.sqrt(1.659E-5/6.6E-7), c='orange', label='air')
ax1.plot(x, 0.005*np.sqrt(x)*np.sqrt(1.659E-5/6.6E-7) *Pr_air**(-1/3), c='g', label='air, thermal b.l.')
ax1.legend()
plt.show()
 