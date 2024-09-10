import matplotlib.pyplot as plt

#Creating a bar graph
x = [1, 5, 3, 11, 6, 4]
y = [2, 6, 5, 13, 8, 7]

plt.bar(x,y, color = "b")
plt.show()

#Creating multiple bars in a single plot
a = [2, 4, 6, 8, 10, 12]
b = [5, 3, 7, 9, 8, 10]
plt.bar(a,b, color = "g")
plt.bar(x,y, color = "b")
plt.show()

#Comparing between two values
plt.bar(["Male Literacy", "Female Literacy"], [90,95])
plt.show()