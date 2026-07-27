##################################################################

### 8.1 Intro to NumPy ###
"""

# faster mathematical operations in high performance 

import numpy as np
"""

### 8.2  NumPy Arrays (ndarrays) ###
"""

# ndarray: n dimentional arrays

import numpy as np

numbers = [1, 2, 3, 4, 5]

print(numbers)

# np.array(): converts python list to numpy array
arrays = np.array((numbers))
print(arrays)

# type of numpy array
print(type(arrays))

# dimention of numpy array
print(arrays.shape) # 1 dimentional array with 5 element

# veraible type of numpy array
print(arrays.dtype)

# zero vector

array = np.zeros(5)
print(array)

array = np.ones(5)

# numpy array in a range
array = np.arange(0, 10)
print(array)

array = np.arange(0, 30, 3)
print(array)

array = np.linspace(0, 10, 5)
print(array)
"""

### 8.3 Mathematical operations in NumPy ###
"""
import numpy as np

# addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
add = a + b
print(add)

# Substraction
sub = a-b
print(sub)

# multiplication
mul = a * b
x = a * 2
y = x ** 2
z = np.sqrt(y)
print(mul)
print(x)
print(y)
print(z)

# Division
div = a / b
print(div)

# Sum of elements of array
print(np.sum(a))

# Avarage
print(np.mean([1, 2, 3, 4]))

# min an max values
print(np.max([1, 2, 3, 4]))
print(np.min([1, 2,3 ,4]))

# Standart daviation
print(np.std([1, 2, 3, 4]))

"""

### 8.4 Numpy indexing and Slicing ### 
"""
import numpy as np

# Indexing
array = np.array([10, 20, 30, 40, 50])
print(array[0])
print(array[1])
print(array[-1])

# Slicing
print(array[1:4])

print(array[:3])
print(array[2:])

# Step  
print(array[::2])

# Indexing in 2 dimentional arrays

matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)
print(matris[0, 0])
print(matris[1, :])
print(matris[2, 1])
print(matris[:, 2])

print(matris[0:2, 0:2])
"""

### 8.5 Array Merging and Splitting in NumPy ###

"""
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))
print(result)

# 2 dimaentional arrays

a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [
        [5, 6],
        [7,8]
    ]
)
result = np.concatenate((a, b))
print(result)

# Axis parameters
# axis = 0 -> merging with respect to rows
# axis = 1 -> merging with respect to collumns

result = np.concatenate((a, b), axis = 1)
print(result)

# vstack(vertical stack): works like axis = 1

sonuc = np.vstack((a, b))
print(result)

# hstack(horizontal stack): works like axis = 0
result = np.hstack((a, b))
print(result)

# Slicing

array = np.array([1, 2, 3, 4, 5, 6])
result = np.split(array, 2)
print(result)

result = np.split(array, 3)
print(result)

# Splitting in 2 dimentional arrays
matris =(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
)
result = np.split(matris, 2)
print(result)

result = np.split(matris, 3)
print(result)

result = np.split(matris, 2, axis = 1)
print(result)
"""

### 8.6 Multi Dimentional Arrays ### 

"""
import numpy as np

matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)
print(matris.shape)
print(matris.ndim)
print(matris.size)

# 3 dimentional arrays

array3 = np.array(
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
    
)
print(array3)
print(array3.shape)

array = np.arange(12)
print(array)

matris = array.reshape(3, 4)
print(matris)
"""

### 8.7  Matrix Operations ###
"""
import numpy as np
a = np.array(
    [
        [1, 2], 
        [3, 4]
    ]
)
b = np.array(
    [
        [5, 6], 
        [7, 8]
    ]
)
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)

result = np.dot(a, b)
print("result: ", result)

det = np.linalg.det(a)
print(det)

inverse = np.linalg.inv(a)
print(inverse)
"""

### 8.8 Random Number Generation in Numpy ###
"""
import numpy as np

# Random floating poin numbers betwee 0 and 1
rand_gen = np.random.rand(5)
print(rand_gen)

# Random matris 
rand_mat = np.random.rand(3, 3)
print(rand_mat)

# Random integers
rand_int = np.random.randint(1, 10, 5)
print(rand_int)

# Random matris with integers
rand_mat_int = np.random.randint(1, 20, (3, 4))
print(rand_mat_int)

# Generating the same random veraibles
np.random.seed(42)
random = np.random.rand(5)
print(random)

# Choosing random veraible from an array
array = np.array([10, 20, 30, 40, 50])
choose = np.random.choice(array)
print(choose)

# Choosing more then one random veraible from an array
choose = np.random.choice(array, 3)
print(choose)
"""
