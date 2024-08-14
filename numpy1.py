import numpy as np

np_city = np.array(["Los Angeles", "New York City", "Amsterdam", "London"])
print(np_city, np_city.ndim, np_city.shape, np_city.size)

print("\n")

np_city_state = np.array([["Los Angeles", "New York City", "Amsterdam", "London"], ["California", "New York", "North Holland", "UK"]])
print(np_city_state, np_city_state.ndim, np_city_state.shape, np_city_state.size)

print(np_city.dtype, np_city_state.dtype)

#Copying an array into another 
np_city_new = np_city
print(np_city_new)

view_of_city = np_city_new.view()
print("\n")
print(view_of_city, len(view_of_city))

view_of_city[3] = "Tokyo"
print(view_of_city, np_city_new)

np_school_marks = np.array([[10, 20, 30, 40, 55, 67], [11, 21, 31, 44, 56, 69]])
np_school_marks_resize = np.array([10, 20, 30, 40, 55, 67, 11, 21, 31, 44, 56, 69])
#Flattening the data
print(np_school_marks.ravel(), np_school_marks.shape)

print("\n")
#Reshaping the array
print(np_school_marks.reshape(3, 4))

#Resizing the array
#print(np_school_marks_resize.resize(a2, 4))

arr = np.array([1, 2, 3, 4, 5, 6]) 
# Resize using np.resize (returns a new array) 
new_arr = np.resize(arr, (3, 3)) 
print(new_arr)
