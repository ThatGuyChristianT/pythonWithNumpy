# NumPy Indexing and Selection
import numpy as np

# Indexing 1D-Array

# Instantiation of 1D-array
arr = np.arange(0, 11)

# Retrieving index 8 inside the Array(Retrieving is the same way we retrieve from list, tuple, set, etc.)
arr[8]

# Retrieving index values from specific indexes
arr[0:4]  # Retrieves array from index 0 (Starting point) until before index 4(Ending point)

# Retrieving all indexes after specified index
arr[3:]  # Grabs everything from index 3 ~ arr's Last Index
# Note: Keep in-mind that numPy arrays are different from Lists because of their ability to broadcast. e.g,
arr[0:5] = 100  # Overwrite 0~4 index values to value of 100

# Retrieving all of the values of an array
arr[:]

# Overwriting all of the array values to one
arr[:] = 1

# Setting a pointer than handles a portion of the array
array_portion_handler_pointer = arr[0:3]  # this var represents a pointer than handles index 0~2 from array var "arr"
# Note: If user attempts to change array_portion_handler_pointer's value(s), it will affect arr's array values. Keep in-mind,
# array_portion_handler_pointer is presented as a pointer/viewer than handles specific range of indexes. e.g,
array_portion_handler_pointer[
:] = 2  # Retrieves all indexes the pointer has a portion of and overwriting the all the data to 2.
# If the code is executed, arr data will be altered from 0,1,2,3,4,5... to 2,2,2,3,4,5.
# Note: The data is not copied to avoid memory issues with large arrays. NumPy does not automatically copy an array value.

# Copying an array value and storing it to another var
arr_copy_another_array_value = arr.copy()

# Indexing 2D Arrays

# Instantiation of 2D-array
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

# Two general formats for grabbing element(s) from the Array/Matrix
# Format 1: Grabbing digit 5
arr_2d[0][0]
# Format 2: Grabbing digit 5
arr_2d[0, 2]
# Note: Format 2 is recommended because it is less prone to error.

# Retrieving chunks of the 2D-Array
arr_2d[:2, 2:]  # Retrieves 15 and 30 from the 2D-Array
# Grabbing 10, 25, 40
arr_2d[:3, 1:2]
# Note, first position is always going to be the row, while second will be the column.

# Conditional Selection

# Re-instantiation of 1D-array for conditional selection
arr = np.arange(1, 11)

# Assert all index's value if they're greater than 5.
boolean_arr = arr > 5  # Returns array of Boolean values

# Retrieve values where all boolean returned true
arr[boolean_arr]

# One-liner to do both Line 60 & 63
arr[arr > 5]

# Assert all index's value if they're less than 3.
arr[arr < 3]