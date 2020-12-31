##NumPy Arrays
import numpy as np

#Instiates a list with fixed value
my_list = [1,2,3]

#Casts List as an array and assign value to var
arr = np.array(my_list)
print(arr)

#Creates 2D-Array(List of list converted into 2D-Array)
my_mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(my_mat)

#One-liner of creating an array with values 0-9
print(np.arange(0,10)) # np.arange() is a common way of creating Array(s)

#One-liner of creating an array with values 0-9 with step-size of two. (Result: 0,2,4,6,8)
print(np.arange(0,10,2))

#Generating specific types of Arrays

#Generating 1D-array of all Zeroes
np.zeros(3)

#Generating 2D-array of all Zeroes
np.zeros((5,5))#First value inside the tuple represents the number of rows, while the second one represents the columns

#Generating 1D-array of all Zeroes
np.ones(3)

#Generating 2D-array of pure ones
np.ones((3,4))

#Linspace will take the third argument as the number of points entered while Arange will take the step size entered.
np.linspace(0,5,10)#Returns 1 dimensional vector of 10 evenly points from 0~5

#Identity Matrix is a useful when dealing on Algebra problems.
#It's basically a 2D square matrix that has equal rows and columns that has diagonal of 1s and the rest are zeroes.
#It only takes a single arg because the matrix must be squared as the output
np.eye(4)

#Numpy Random feature

#Creating 1D-array that creates an array that is populated with random uniform distribution from 0~1
np.random.rand(5)

#Creating 2D-array that creates an array that's populated with random distribution anywhere from 0~1
np.random.rand(5,5)

#Creating 1D-array that returning numbers that isn't a uniform number from 0~1 but anywhere centered around 0. (-1 ~ 1)
np.random.randn(2)

#Creating 2D-array that returning numbers that isn't a uniform number from 0~1 but anywhere centered around 0. (-1 ~ 1)
np.random.randn(5,5)

#Generating 1D-Array with a single randomized value from 1~99
np.random.randint(1, 100, 10)

#Generating 1D-Array with 10 randomized value from 1~100
np.random.randint(1, 100, 10)#Third parameter determines how many randomized value(s) will generated and inserted into the array

#Few useful methods of an array
arr = np.arange(25) #Creates 1D-array with values, 0~24
random_array = np.random.randint(0,50,10)#Generates 10 random generated integer value from 0~49
arr.reshape(5,5)#Allows to reshape an existing array.
#NOTE: You will get an error if you try to reshape an Array more than the values stored.
#How to avoid: if you're trying to make a 2D array, make sure it is ROW*COLUMN = total array index.

#Retrieving Max/Min Values & its' index position
random_array.max()#Returns max value of the Array
random_array.min()#Returns min value of the Array
random_array.argmax()#Returns the highest value's index position
random_array.argmin()#Returns the lowest value's index position

#Figuring out a shape of a vector
arr.shape #No parenthesis because you're calling the attribute of the var.

#Retrieving data-type of an array/vector
arr.dtype

#If you want to remove the repetitive package calling to access the Numpy's Random feature
from numpy.random import randint
from numpy.random import randn
#allows you to just use the methods without calling numpy.random... e.g,
randint(10)
randn(10)