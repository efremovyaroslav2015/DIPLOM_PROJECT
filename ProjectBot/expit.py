import numpy as np

data_string ={"matrix ":"2.771331,2030.000000,753.000000,111.860000,22.267857,284.615385,210.000000,70.000000,220.000000,0,5.000000,57.000000"}
#numbers = [float(num) for num in list(data_string.values()).split(',')]
#print(numbers)
values = np.array([2.771331, 2030.0, 753.0, 111.86, 22.267857, 284.615385, 210.0, 70.0, 220.0, 0.0, 5.0, 57.0])
b_values = np.reshape(values, (-1,1))
print(b_values)
print(values)