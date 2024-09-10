#Plotting multiple graphs on a single plot

import matplotlib.pyplot as plt
x = [1,5,3,7,8]
y = [2,8,10,9,2]
a = [7,8,3,1,4]
b = [2,3,1,5,4]
plt.plot(x,y, "r--", label = "y=2x", linewidth = 5 )
plt.plot(a,b, "g--", label = "y=3x", linewidth = 3)
plt.legend(["company a", ["company b"]])
plt.show()