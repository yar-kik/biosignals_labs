import numpy as np

python_array = [10, 2, 42, 13]
int_numbers = np.array(python_array, int)
float_numbers = np.array(python_array, float)
complex_numbers = np.array(python_array, complex)
print(int_numbers)
print(float_numbers)
print(complex_numbers)

array = np.arange(0, 10)
another_array = np.arange(5, 25, 2)
square_int = array ** 2
sum_array = array + another_array

print(array)
print(another_array)
print(square_int)
print(sum_array)

two_dimension_array = np.array([[1, 2, 142, 421, 42], [124, 12, 53, 14, 5], [6, 374, 23, 12, 785]])
single_number = two_dimension_array[1][2]
sliced_array = two_dimension_array[2, 2:]
shape = np.shape(two_dimension_array)
print(two_dimension_array, single_number, sliced_array, shape, sep='\n')
