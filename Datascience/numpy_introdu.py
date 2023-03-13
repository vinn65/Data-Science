import numpy as np

arr = np.array([1,2,3])

print(arr)
print(type(arr))

# #2-d array

arr1 = np.array([[2,4],[3,4]])
print(arr1)

print(arr1.ndim)
print(type(arr1))

# #shape of an array
# #reshaping means changing the shape of array
# #flattening array - converting a multidimensional array into a 1D array.
# #use reshape(-1)
arr2 = np.array([1,2,3,4,5,6])
print(arr2.shape)

arr2_new = arr2.reshape(3,2)
print(arr2_new)

arr2_back = arr2_new.reshape(-1)
print(arr2_back)

#iteration 2d
arr3  = np.array([[1,2,3,],[4,5,6]])
for x in arr3:
    print(x)

# #iteration on each element of 2d array

for x in arr3:
    for y in x:
        print(y)

# #iteration on each element of 3d array


#array slicing -  taking an elemnt from one index to another
arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr4[1,1:4])
print(arr4[1,:4])

#searching arrays - where()
#sorting - sort()
arr5 = np.array([4,2,3,1,5,6])
x = np.where(arr5 == 3)
print(x)
arr5.sort()
print(arr5)


