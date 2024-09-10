#Creating a scatter plot

import matplotlib.pyplot as plt
x = [1, 4, 5, 9, 12]
y = [2, 6, 3, 1, 8]
plt.plot(x,y, "o--")
plt.title("Information")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()