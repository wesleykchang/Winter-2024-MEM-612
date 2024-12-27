import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0,1)
u = y*(1-y)**2

T = (1-y)**2

plt.plot(y, u, color='k', label='dimensionless u')
plt.plot(y, T, color = '#E0001B', label='dimensionless T')

plt.xlabel('$\delta$, boundary layer thickness norm.')
plt.legend()
plt.show()