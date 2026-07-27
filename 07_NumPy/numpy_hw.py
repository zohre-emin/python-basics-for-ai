############################################################

### Answer 1 ###

import numpy as np

#### Answer 3 ###
array = np.arange(0,31)

print(array)

print(array[10:21])

#### Answer 4 ###
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a+b)
print(np.concatenate((a, b)))

### Answer 5 ###
array = np.arange(1, 13)
matris = array.reshape(3, 4)
print(matris)
print(matris.shape)

### Answer 6 ###
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris[1, :])
print(matris[:, 1])

### Answer 7 ###

matris = np.random.rand(3, 3)
print(matris)

print(np.mean(matris))
print(np.max(matris))

### Answer 8 ###
a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

print(a * b)

### Answer 9 ###
array = np.arange(1,10)
matris = array.reshape(3, 3)
print(matris.T)

### Answer 10 ###
rand_array = np.random.randint(1, 51, 10)
print(np.sum(rand_array))
print(np.mean(rand_array))