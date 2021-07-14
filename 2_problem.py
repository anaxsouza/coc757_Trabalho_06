import numpy as np
from numpy.lib.utils import info
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#FIRST INITIAL CONDITION

# function that returns dy/dt
def model(y,t):
    k = 200
    dydt = -k * y**2
    return dydt

# initial condition
y0 = 1

# time points
t = np.linspace(0,1)

# solve ODE
y1, infodict1 = odeint(model,y0,t, full_output= True)

# plot results
plt.plot(t,y1)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

# print step sizes
stepsize1 = infodict1['hu']
print(stepsize1)


#SECOND INITIAL CONDITION

# initial condition
y3 = 1/901

# solve ODE
y2, infodict2 = odeint(model,y3,t, full_output= True)

# plot results
plt.plot(t,y2)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

# print step sizes
stepsize2 = infodict2['hu']
print(stepsize2)