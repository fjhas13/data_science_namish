#Histograms
import matplotlib.pyplot as plt

x = [18, 10, 22, 34, 41, 21, 19, 8, 15, 47]
y = [0, 10, 20, 30, 40, 50]

plt.xlabel("Age Intervals")
plt.ylabel("Frequency/Number of People")
plt.title("Ages that go to an amusement park")
plt.hist(x,y,histtype="bar", rwidth = 3, edgecolor = "black")
plt.show()