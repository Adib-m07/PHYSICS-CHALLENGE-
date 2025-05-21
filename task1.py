import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
l = np.linspace(400,800,100)
c = l/1000
a = np.array([1.03961212, 0.231792344, 1.01146945])
b = np.array([0.00600069867, 0.0200179144, 103.560653])
y=np.zeros(len(l))
for j in range(len(a)):
    y = y + (a[j]*c**2/(-b[j]+c**2))
y = (y+1)**.5
plt.plot(l,y)
plt.axis((400,800,1.51,1.53))
plt.ylabel("refraction")

