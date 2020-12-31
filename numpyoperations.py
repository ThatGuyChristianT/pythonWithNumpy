#NumPy Operations:
#   -Array with Array
#   -Array with Scalars
#   -Universal Array Functions

import numpy as np

#Instantiate 1D-array
arr = np.arange(0,11)

#Adding array values
arr + arr #Note: Array index value will add up together.
          #e.g, arr[1,2,3,4,5] + arr[1,2,3,4,5] = arr[2,4,6,8,10]
          #Warning, both arrays have equal-sizing, otherwise an error will be thrown

#Substracting array values
arr - arr #Note: Array index value will subtract each other's value.
          #e.g, arr[1,2,3,4,5] - arr[1,2,3,4,5] = arr[0,0,0,0,0]
          #Warning, both arrays have equal-sizing, otherwise an error will be thrown

#Multiplying array values
arr * arr #Note: Each Array index value will multiply together.
          #e.g, arr[1,2,3,4,5] * arr[1,2,3,4,5] = arr[1,4,9,16,25]
          #Warning, both arrays have equal-sizing, otherwise an error will be thrown

#Array with Scalar Operations
#Scalar means a single number; basically means if we do arr + 1, it will increase all of the index's value by one.

#Scalar Operation: Addition
arr + 100 # arr[1,2,3,4,5] + 100 = arr[101,102,103,104,105]

#Scalar Operation: Substraction
arr - 100 # arr[1,2,3,4,5] - 100 = arr[-99,-98,-97,-96,-95]

#Scalar Operation: Multiplication
arr * 100 # arr[1,2,3,4,5] * 100 = arr[100,200,300,400,500]

#Universal Array Functions

#Squareroot
np.sqrt(arr)#Retrieves a square of everything on all of the array

#Retrieve highest value of the array
np.max(arr)

#Retrieves lowest value of the aray
np.min(arr)

#Sin
np.sin(arr)

#Log
np.log(arr)

#For more information regarding this topic, go-to https://docs.scipy.org/doc/numpy/reference/ufuncs.html