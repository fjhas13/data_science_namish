import numpy as np
import matplotlib.pyplot as plt

a = np.arange(1,10,2)
print(a)

b1 = a**2
b2 = a**3

plt.plot(a,b1, "g--", a,b2, "r--")
plt.show()