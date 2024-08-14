import numpy as np
import pandas as pd

#Creating a series from a list
first_series = pd.Series(list("abcdef"))
print(first_series)

#Creating a series from a nd (n-dimensional) array
np_country = np.array(["USA", "China", "Mexico", "India", "Canada", "Switzerland", "Italy", "Austria", "Germany", "Russia"])
country = pd.Series(np_country)
print("/n")
print(country)

#Creating a series from a dictionary
age = pd.Series([887, 123, 456, 567, 987, 234, 999, 888, 408, 240], index = ["USA", "China", "Mexico", "India", "Canada", "Switzerland", "Italy", "Austria", "Germany", "Russia"] )
print(age)

#Series with Scalor (unidirectional) input
scalor_series = pd.Series(45.0, index = ["a", "b", "c", "d", "e"])
print(scalor_series)

#Access elements in series
print(age["India"])
print(age.iloc[3])
print(age.loc["Italy"])
#loc function is used for custom index names, whereas iloc is based on item index location

print(age.iloc[1:5])