import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Rex = np.array([0.255, 0.423, 0.58, 0.736, 0.889, 1.045, 1.196, 1.353, 1.507, 1.661, 1.823, 1.97, 2.13, 2.28, 2.44, 2.6, 2.75, 2.9, 3.05, 3.18, 3.36])*1E6
print(Rex)
St = np.array([2.73, 2.41, 2.13, 2.11, 2.06, 2.02, 1.97, 2.01, 1.85, 1.79, 1.84, 1.78, 1.79, 1.73, 1.74, 1.75, 1.72, 1.68, 1.73, 1.67, 1.54])*1E-3
Pr = 0.707
Nu = Rex * St * Pr

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
slope, intercept = np.polyfit(np.log(Rex),np.log(Nu), 1)
 
ax1.plot(np.log(Rex), np.log(Nu), marker = 'o')
ax1.plot(np.log(Rex), slope * np.log(Rex) + intercept, 'r', label='Linear regression')
ax1.plot(np.log(Rex), np.log(0.0296*Pr**0.6*Rex**0.8))
print(Pr**0.6*0.0296)
print(f"Slope: {slope}, Intercept: {np.exp(intercept)}")
# ax1.set_yscale('log')
# ax1.set_xscale('log')
plt.show()

fig2 = plt.figure()
r = np.linspace(-10,10)
R = 10
mu = 1
P = 4

u = R**2/(4*mu)*P*(1-(r/R)**2)
ax1 = fig2.add_subplot(111)
ax1.plot(u, r)
plt.show()
