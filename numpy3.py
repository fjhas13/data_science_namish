import numpy as np

test_scores = np.array([[32, 37, 51, 68], [38, 98, 45, 77]])
pass_score = test_scores > 60
print(pass_score)
print(test_scores[pass_score])

#Deep copy and shallow copy
array1 = np.array([31, 45, 67, 78, 91])
array1_shallowcopy = array1.view()
array1_shallowcopy[2] = 99
print(array1, array1_shallowcopy)

array2 = np.array([31, 45, 67, 78, 91])
array2_deepcopy = array2.copy()
array2_deepcopy[2] = 99
print(array2, array2_deepcopy)

#Multiplication within arrays
array3 = np.array([56, 78, 90, 21, 44])
array4 = np.array([31, 67, 83, 46, 77])
array_product = array3 * array4
print(array_product)

#Division within arrays
array_quotient = array3 / array4
print(array_quotient)

array_quotient1 = array3 / 5
print(array_quotient1)

#Array Transpose
test_scores = np.array([[32, 37, 63], [38, 98, 44], [12, 67, 32]])
print(test_scores.transpose())

#Trace - Trace gives us the sum of the diagnol elements in a square array
print(np.trace(test_scores))