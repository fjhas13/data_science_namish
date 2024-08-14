import numpy as np

first_trial_cyclist = [10, 15, 17, 26]
second_trial_cyclist = [12, 11, 21, 24]
np_first_trial_cyclist = np.array(first_trial_cyclist)
np_second_trial_cyclist = np.array(second_trial_cyclist)
np_sum = np_first_trial_cyclist + np_second_trial_cyclist
print(np_sum)
# The above sum operation in numpy arrays can only happen if the length of items in both the arrays are same, else it will display error

print('\n')

#Accessing array elements through indexing
cyclist_trials = np.array([[10, 15, 17, 26], [12, 11, 21, 24]])
first_trial = cyclist_trials[0][2]
print(first_trial)
second_trial = cyclist_trials[1]
print(second_trial)


## Indexing examples in details using lists
# Indexes are positional values of items. They start from 0 and continue as 0, 1, 2, 3 ...
list1 = [13, 12.14, "Namish", [167, True, 10.14, "Hello Namish"], False]
print(len(list1))

print(list1[4])

print(list1[2][3])

print(list1[3][3][6])

## Slicing
# Slicing means extracting a portion of the list 
# It has a starting index and destination index
# We start counting from starting index, and will always go upto 1 less than the destination index
# 
print(list1[1:3]) 
print(list1[2:7])
print(list1[0:3])
print(list1[1:])
print(list1[:])