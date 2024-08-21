import numpy as np
import pandas as pd

#Creating a data frame from a dictionary of series
olympic_series_participation = pd.Series([205, 204, 201, 200, 197], index = [2012, 2008, 2004, 2000, 1996])
olympic_series_country = pd.Series(["London", "Beijing", "Athens", "Sydney", "Atlanta"], index = [2012, 2008, 2004, 2000, 1996] )

df_olympic_series = pd.DataFrame({"Number of Participating Countries" : olympic_series_participation, "Host Cities" : olympic_series_country})
print(df_olympic_series)
print("\n")

#Creating a data frame from an nd array
np_array = np.array([5000, 7456, 2341, 1009, 4325])
dict_ndarray = {"Year" : np_array}

df_ndarray = pd.DataFrame(dict_ndarray)
print(df_ndarray)
print("\n")

#Creating data frame from another data frame
df_copy_1 = pd.DataFrame(df_olympic_series)
print(df_copy_1)
print("\n")

df_copy_2 = df_olympic_series
print(df_copy_2)
print("\n")

#Handling missing values
first_series = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
second_series = pd.Series([10, 20, 30, 40, 50], index = ["c", "e", "f", "g", "h"])

sum_of_series = first_series + second_series
print(sum_of_series)
print("\n")

#Missing value imputation by using drop NA (Not a number) function
dropna_s = sum_of_series.dropna()
print(dropna_s)
print("\n")
#dropna function removes all of the NaN values in a data frame

#Fill the NaN values as 0
fillna_s = sum_of_series.fillna(0)
print(fillna_s)
print("\n")

#Fill NaN with 0s and perform addition operations for missing indexes
new_imputation = first_series.add(second_series, fill_value = 0)
print(new_imputation)