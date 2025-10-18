#  NumPy Introduction
# NumPy is a powerful library for numerical computing in Python. It provides support for arrays,

#example :
'''import numpy 

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
'''
#example :
'''import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)'''

#example :
'''import numpy as np
print(np.__version__)'''

#=================================================================================

# NumPy Arrays
# NumPy arrays are the core data structure of the NumPy library. They are similar to Python lists but offer better performance and more functionality for numerical operations.

#create a numpy array ndarray object 

'''import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(type(arr))'''

#Dimensions in Arrays
# A NumPy array can have multiple dimensions, which allows for more complex data structures.

#0-D Arrays: 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

#example :
'''import numpy as np
arr = np.array(42)
print(arr)
print(arr.ndim) #ndim is an attribute that returns the number of dimensions of the array.'''

#1-D Arrays: 1-D arrays are like a list of values. They have one dimension.
#example :
'''import numpy as np 
arr_1d = np.array([1,2,3,4,5])
print(arr_1d)
print(arr_1d.ndim)'''

#2-D Arrays: An array that has 1-D arrays as its elements is called a 2-D array. These are often used to represent matrix or 2nd order tensors . 
#example : Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6.
'''import numpy as np 
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
print(arr_2d.ndim)
'''
#3-D Arrays: An array that has 2-D arrays as its elements is called a 3-D array. These are often used to represent a cube or 3rd order tensors.
#example : Create a 3-D array containing two 2-D arrays.
'''import numpy as np
arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_3d)'''

#=================================================================================

#Check Number of Dimensions?
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
'''import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)'''
#================================================================================= 
#Asssigment 
#Create a 0D array with the value 25 and print its dimension.
'''import numpy as np
arr = np.array(25)
print(arr)'''

#Make a 1D array containing numbers from 10 to 50 with a step of 10.
'''import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)'''

#Print the 3rd element of a 1D array [5, 10, 15, 20, 25].
'''import numpy as np
arr = np.array([5,10,15,20,25])
print(arr[2])'''

#Create a 2D array of shape (2,3) with random integers between 1 and 9.
'''import numpy as np
arr = np.random.randint(1,10,(2,3))
print(arr)'''

#Access the element in the 2nd row, 1st column of that 2D array
'''import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr[1,0])'''
 
#Find the shape and number of dimensions of this array:np.array([[1,2,3],[4,5,6]])
'''import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim) '''

#Create a 3D array using np.arange(12).reshape(2,2,3) and print it.
'''import numpy as np 
arr = np.arange(12).reshape(2,2,3)
print(arr)'''
#Access the element in block 2, row 1, column 3 of that 3D array.
'''import numpy as np
arr = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
print(arr[1,0,2])
print(arr.ndim)'''
#Find the toal number of elements in the 3d array.
'''import numpy as np
arr = np.arange(12).reshape(2,2,3)
arr = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
print(arr.size)'''
#Flatten the 3D array into 1D using .ravel() and print the result.
'''import numpy as np
arr = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
flat_arr = arr.ravel()
print(flat_arr)'''

#=================================================================================
#NumPy Array Indexing:
"""Access Array Elements: Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc."""
#example :
# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr[0])  # Accessing the first element
# print(arr[2])  # Accessing the third element

#example :
'''import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[0]+arr[4])  # Accessing and adding the first and fifth elements
print(arr[2]-arr[6])  # Accessing and subtracting the third and seventh elements
print(arr[1]*arr[3])  # Accessing and multiplying the second and fourth elements
print(arr[8]/arr[5])  # Accessing and dividing the ninth and sixth elements'''

#Access 2-D Arrays
"""To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column."""
#example :
'''import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2nd element on 1st row:", arr[0,1])  # Accessing the second element of the first row
print("5th element on 2nd row:", arr[1,4])  # Accessing the fifth element of the second row'''

#Access 3-D Arrays
"""To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element."""
#example :
'''import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("2nd element of 1st array of 1st dimension:", arr[0,0,1])  # Accessing the second element of the first array in the first dimension
print("3rd element of 2nd array of 2nd dimension:", arr[1,1,2])  # Accessing the third element of the second array in the second dimension'''

#Negative Indexing:Use negative indexing to access an array from the end.
#example :
"""import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Last element:" , arr[1,-1])  # Accessing the last element of the second row
print("2nd last element:", arr[0,-2])  # Accessing the second last element of the first row"""