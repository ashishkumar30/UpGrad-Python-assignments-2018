import numpy as np


'''
#Q1.Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.


array=np.random.rand(10,1)
print("Array:\n",array)
print("Mean: ",array.mean(axis=0))

'''



'''
#Q2.Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements. 

array=np.random.rand(20,1)
print("Array:\n",array)

print("Mean: ",array.mean(axis=0))
print("Variance: ",array.var(axis=0))
print("Standar Deviation: ",array.std(axis=0))

'''




'''
#Q3.Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

x=np.random.rand(10,20)
y=np.random.rand(20,25)

z=x.dot(y)
print(z)
print("Shape of new array: ",np.shape(z))
print("Sum of elements in new array: ",np.sum(z))
'''



'''
#Q4.Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A.
#f(x)=1 / (1 + exp(-x)) 
#Apply this function to each element of A and print the new array holding the value the function returns
#Example:
#a=[a1,a2,a3]   
#n(new array to be printed )=[ f(a1), f(a2), f(a3)]



A=np.random.rand(10,1)
print("\nArray A:\n",A)

f=lambda x:(1/(1+np.exp(-x)))

print("\nNew array:\n",np.array(list(map(f,A))))

'''
