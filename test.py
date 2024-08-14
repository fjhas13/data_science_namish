import numpy as np

# Original array
a = np.array([1, 2, 3, 4])
print("Original array:")
print(a)

# Reshape to (2, 2)
reshaped = a.reshape((2, 2))
print("Reshaped array:")
print(reshaped)

# Resize to (2, 3)
resized = np.resize(a, (2, 3))
print("Resized array (new object):")
print(resized)

# In-place resize to (2, 3)
a.resize((2, 3))
print("In-place resized array:")
print(a)