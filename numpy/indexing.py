import numpy as np
 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
 
print(arr[0,1,2]) 
print('\n')
print(arr[1, 0, 2])
print('\n')


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
 
print('Last element from 2nd dim: ', arr[1, -1])