import numpy as np

n1 = np.zeros([3, 4])
n2 = np.empty([3, 4])
n3 = np.arange(10)
n4 = np.arange(-5, 10, 5)  # -5  0   5

n5 = np.linspace(0, 20, num=5)
n6 = np.full([2, 5], 99)

# print(n1[0, 0])    # printing index value
# print(n1[0][0])    # printing index value
n1[0][0] = 10
print("-----------------------------------------------------------------------------")
# shape and size
print("shape and size\n")
print("it gives the number of dimensions or axes = ", n1.ndim)  # it gives the number of dimensions or axes
print("inserted values in the n1 empty tag (3, 4) = ", n1.shape)     # inserted values in the n1 empty tag (3, 4)
print("no of values in the n1's total array = ", n1.size)  # no of values in the n1's total array
print("it telling the data type present in the array = ", n1.dtype)     # it telling the data type present in the array
print("data type in byte = ", n1.itemsize)     # data type byte
print("total bytes size for the array = ", n1.nbytes)        # total bytes size for the array
print("-----------------------------------------------------------------------------")
# Sorting
print("Sorting\n")
print("sorting the n3 in row wise (axis = 1) = ", np.sort(n3))  # row wise sort # default axis = 1 (row wise)

# column wise sorting
print("sorting the n3 in col wise (axis = 0) = ", np.sort(n3, axis=0))  # col wise sort and 1(default) for row wise sort

print("-----------------------------------------------------------------------------")
# resizing and array conversion
print("resizing and array conversion\n")
n10 = np.array([3, 4, 5, 6, 7, 8, 9, 10])
print("array created using np.array and the array values = ", n10)
print("-----------------------------------------------------------------------------")
# creating a matrix using the reshape
print("creating a matrix using the reshape\n")
n12 = n10.reshape(2, 4)     # 2 x 4 matrix
print("a linear array was reshaped into 2 x 4 matrix using reshape function = ", n12)
print("-----------------------------------------------------------------------------")
# concat
print("\n\nConcat")
n13 = np.concatenate((n1, n2))
print("concat value of n1 and n2 = ", n13)
print("The values are in zeros due to created the two using the random arange function")

print("-----------------------------------------------------------------------------")
# creating a 2d array from 1d array
print("creating a 2d array from 1d array\n")
n14 = np.arange(9)  # creating a array with 9 words
print("n14 created using the arange = ", n14)
n15 = n14[np.newaxis, :]    # it convert 2d array to 3d and 1d array to 2d array
n16 = n14[:, np.newaxis]
print("converting 1d array to 2d array with using n14 array values = ", n15)
print("n15 shape(matrix row and col len) value = ", n15.shape)
print("n16 ?????? doubt = ", n16)
print("n16 shape(matrix row and col len) value = ", n16.shape)
print("-----------------------------------------------------------------------------")
# alter for converting 1d to 2d array and 2d array to 3d array
# expand dimension
print("alter for converting 1d to 2d array and 2d array to 3d array\n")
print("n19 :-")
n19 = np.expand_dims(n14, axis=0)  # 0 for horizontal expand and 1 for vertical expand
print("alter method for converting 1d to 2d array with using expand_dims with n14 array values (axis = 0) = ", n19)
print("-----------------------------------------------------------------------------")
# indexing and slicing
print("indexing and slicing\n")
n21 = np.arange(10)
print("n21 created using arange = ", n21)
print("values lesser than 3 and greater than 8= ", n21[(n21 > 3) & (n21 < 8)])

n21[6] = 100
# it printing the index value not the array values
print("values are lesser than 5 = ", np.nonzero(n21 > 5))

print("-----------------------------------------------------------------------------")
print("stack and split\n")
# stack and split
# output be like
# 1 2 5 6
# 3 4 7 8
n22 = np.array([[1, 2], [3, 4]])
n23 = np.array([[5, 6], [7, 8]])
print("h-stack values by combining n22 and n23 = ", np.hstack((n22, n23)))    # horizondal stock

#vertical stock
# 1 2
# 3 4
# 5 6
# 7 8
print("v-stock")
print(np.vstack((n22, n23)))

# split
# h split (horizontal split)
n24 = np.arange(20)
print("h-split")
print(n24)
print(np.hsplit(n24, 4))    # splited into 4 values of array one array consists 4 values
#   print(np.vsplit())

print("-----------------------------------------------------------------------------")
# copy
print("copy\n")
n25 = n24
n24[0] = 100

print("\n\nin shallow copy the newly created variable only reference the old n24 array ")
print("\n\nshallow copy\nn24 = ", n24)
print("n25 = ", n25)


# deep copy
print("\n\nin deep copy new variable created and it stores the values of n24 separately ")
n26 = n24.copy()
n24[2] = 100
print("\n\ndeep copy\nn24 = ", n24)
print("n26 = ", n26)

print("-----------------------------------------------------------------------------")
# math
print("math\n")
print("n22 array created = ", n22)
print("n23 array created = ", n23)
print("adding n22 and n23 = ", n22 + n23)
print("mul n23 with n23 = ", n23 * n23)
print("n26 = ", n26)
print("sum of n26 = ", n26.sum)

print("-----------------------------------------------------------------------------")
# random number in the array
print("random number in the array using random.rand\n")
print("\n\nprinting random numbers  = ")
n27 = np.random.rand(3, 3)  # 3 x 3  matrix will created
print(n27)

# random number between 20 numbers
print("\n\nrandom number between 20 numbers using random.randient")
print("\n\nPrinting random numbers between 1 to 20 = ")
n28 = np.random.randint(20, size=(3, 3))    # the array contains the numbes from 1 to 20
print(n28)

print("-----------------------------------------------------------------------------")
# cos, sin values for the array values
print("cos, sin values for the array values\n")
print("\nPrinting the cos values for n26 = ")
print(np.cos(n26))

