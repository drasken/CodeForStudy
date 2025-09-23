import ctypes

# Load the shared library
number_cruncher = ctypes.CDLL('./number_cruncher.so')

# Call the C function
result = number_cruncher.add(5, 3)
print("Result from C:", result)
