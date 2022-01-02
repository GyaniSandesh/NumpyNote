# Hello everyone this is me Sandesh Regmi. I tried my best to create this one shot note for you and I hope you are a bit familier with numpy and basics of python such as loops concept, list, dictionaries and I took the reference of some pdf's and even with some of the videos from YouTube. Don't forget to rate this note.
# Uncomment the piece of line when you feel it necessary
# At first, you need to install numpy module using the command "pip install numpy" in your integrated terminal. However if you are using advanced notebook such as jupyter and other you don't need to install this module at all.
# Now, see how I imported that module
import numpy as n
from numpy import *#This will include all the functions that numpy have
from numpy.random.mtrand import rand
# Keep in mind that axis 1 is for row and axis 0 is for column.However, if you don't have any idea about that, then you will know it's uses once you'll go through those lines of codes

# Creating 1D Array
# a = n.array([2,3,4])
# print(a)
# Or you can even create an array by using the following way
# b = [2,3,4]
# print(n.array(b))

# For creating an array in which user can give the input of the elements
# ab = []
# no = int(input("Enter the size of the array:\t"))
# for i in range(no):
#     v = int(input("Enter the array element\t"))
#     ab.append(v)
# print("Your array element is as follows:")
# print(n.array(ab))

# Creating 2D Array using Numpy
# This is a simple 2D Array
# print(n.array([[10,9,8],[7,6,5],[4,3,2]]))
# Here,you can use the same concept that you used while creating your 1D array just like creating an empty array and later on appending the element of 2D array just like and know other functions that you can use along with that
# ba = n.array([[10,9,8],[7,6,5],[4,3,2]])
# print(ba)
# You will know other ways of creating 2D array as you go through the lines of code
# print(f"Total dimension of your array is {ba.ndim}")
# print("Shape of your array('At 1st it tells the number of rows and then number of columns') is ",ba.shape)
# Some other numpy functions that we can use
# Using Zeros/Ones to create array and fill all the values with 0/1 coresspondingly
# print(n.zeros(3))
# print(n.ones((3,4)))#Creating matrix of 3*4 size with 3 columns and 4 rows
# arr = n.ones((4,4))
# t = arr[1:3,1:3]
# print(t)# t will be a 2x2 matrix with 4 elements

# Identity function that will return an identity matrix of r row and r columns
# arr_i = n.identity(4)
# print(arr_i)

# Eye function creates an array with all the diagonal elements 1 and rest of the elements with 0
# print(n.eye(3))#Will create a square matrix of N*N
# print(n.eye(3,4))#At first it will create 3*3 matrix with rest remaining filled with 0 and you will get the better understanding once you will uncomment this line and run it

# Using diag function
# print(n.diag([6,7,8,9]))#Now this will create create an square matrix with diagonal that is given and enclosed inside parenthesis
# To get the diagonal elements use the following
# bb = n.diag([2,3,4])
# print("The diagonal elements is as follows:")
# print(n.diag(bb))

# Using randint function to generate a random number within a given range and the syntax is as follows::        rand(min,max,total_values) and here you don't need to import a module named random
# print(n.random.randint(1,101,10))
# print(n.random.rand(3,4))#This will create 3*4 matrix from the value ranging from 0 to 1 and this will include decimal number.
# print(n.random.randn(2))#This will generate a random value close to 0 and it may return both +ve or -ve number and this will give total number of value 2

# Some useful programmes for building the clear concepts in array
# Finding the sum and multiplication of all the elements of array
# c = []
# num = int(input("Enter the size of your array:"))
# print("Now enter the elements of your array and make sure that after entering one element of your array you should hit enter and get ready to enter another one::")
# for i in range(num):
#     va = int(input(""))
#     c.append(va)
# ac = n.array(c)
# Slicing in an array and then printing it
# ac1 = ac[-1:]#And while slicing mention the number from where your slicing will be started and till a step over of your required number
# print("Printing the array after slicing it")
# print(ac1)
# sum = 0
# mul = 1
# for i in range(ac.size):
#     sum = sum+ac[i]
#     mul = mul*ac[i]
# print("The sum of your array is ",sum," and the nultiplication is ",mul)

# Reshaping of an array i.e. converting 1D array to 2D array and vice-versa

# abc = n.random.randint(1,51,8) #If you are running this code till line number 86 , then uncomment this line
# 1D => 2D
# print("Printing that 1D array:")
# print(abc)
# Well reshape function is used to arrange the array element as per the program of the programmers and make sure that the multiplication of those two numbers must be 12
# print(abc.reshape(2,4))#Now, this will create an array of size 2*4

# 2D => 1D
# print(acb.reshape(8))

# There is another concept of creating 2D array
# print(abc.reshape(4,-1))#Here, initially it will divide 8 with the number 4 and with the quotient it will ceate a matrix.In this condition, it will create 4*2 matrix

# Seed function (I hope till now you are well know about Pseudo-Random Numbers)
# n.random.seed(8)#Well this will generate set of random numbers with 8 number of elements and will fix that and won't let it's value be changed
# acb = n.random.randint(low = 1,high = 51,size = 8)#And this is also another way of creating random array using randint
# print(acb)
# n.random.seed(1)
# cc = n.random.randint(1,100,8)
# print(cc)#After seeding with some number, the value that I got will be similar to the value that you got in your device and you can use other functions such as size with this one.

# Using searchsorted function
# sandesh_array = n.array([1,2,3,5,6.7])
# print(n.searchsorted(sandesh_array,4))#Well, this will do a binary search and returns the position where the given value must be sorted.Take one thing in consideration that the elements of the array must be sorted.If it is not sorted you can use sort() function to sort it.
# print(n.searchsorted(sandesh_array,4,side='right'))
# print(n.searchsorted(sandesh_array,4,side='left'))

# Creating 2D Array that has user input as well(I hope you are well know about indexing using double bracket notation)
# emp_mat = []
# r = int(input("Enter the number of rows\t"))
# c = int(input("Enter the number of columns\t"))
# print("Enter the elemets of array")
# for i in range(r):
#     emp = []
#     for j in range(c):
#         va = int(input(""))
#         emp.append(va)
#     emp_mat.append(emp)
# # Printing your 2D Array
# n.array(emp_mat)
# print("\n\nNow, printing your 2D array")
# for i in range(r):
#     for j in range(c):
#         print(emp_mat[i][j],end=" ")
#     print()
# print(type(emp_mat))

# There is a simple way of finding the transpose of a matrix using transpose function
# a =n.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12]
# ])
# print("Shape of your array is ",a.shape)
# print(n.transpose(a))

# Using where method to find the value of the numpy element position or index.However, you can use loop to find the position but using where method is much more faster
# za = n.array([1,2,3,4,5,6,3,7,3,8,2,4,7])
# print(za)
# print('Indexing 2',n.where(za==2))
# print('Indexing 3',n.where(za==3))
# print('Indexing 4',n.where(za==4))
# print('Indexing 7',n.where(za==7))

# Slicing of 2D Array
# Syntax :- array_name[row_range,column_range]
# exp_array = n.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12]
# ])
# print(exp_array[:2,:3])#Index start from 0 to 1 in row and 0 to 3 in column

# n.random.seed(336)
# a = n.random.randint(1,100,20).reshape(4,5)[:5,:4]#Notice that I am slicing and seeding along with using random module at a same time.You should be familier with this to make your code short and 
# print(a)

# Difference between View and Copy function
# This is an example of View
# a1 = n.array([1,2,3,4,5])
# sl = a1[1:4]
# sl[:]=00
# print(a1)
# This is an example of Copy
# a2 = n.array([1,2,3,4,5])
# sl1 = a2[1:4].copy()
# sl1[:]=00
# print(sl1)
# print(a2)

# Conditional seletion statement in Python Numpy
# Let us consider an array
# aaa =  n.array([1,2,3,4,5,6,7,8,9,10])
# bbb = aaa%2==0
# ccc = aaa<=5
# print(bbb, '\t' ,ccc)
# You can use various
# And also the array value can be updated for example
# aaa[aaa%2==1] = 1111
# print(aaa)

# Operation on array
# Operation in 1D Array
# aabbcc = n.arange(5,10)#The function will create a list of array ranging from given number and here it will include from 5 to 10 
# Then you can perform different operation with that array such as multiplication, divisioin, addition, substraction and many more.
# print(((aabbcc+2)*4)/2)#Take one thing in consideration that whenan array of numpy is divided by 0, then it will give the result as infinity instead of giving other type of error
# Operation in 2D Array
# x = n.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# y = n.array([6,7,8,9,10,11,11,12,13]).reshape(3,3)
# print(x.dot(y))
# print(n.matmul(y,x))#Matmul and dot function is used to find the multiplication of two matrix.

# There are some other functions in numpy used for various purpose.Here are some of the important functions used in Numpy
# zzz = n.arange(1,6)
# print(n.cos(zzz))#Will return the cosine of element of array
# In the same way, you can use functions such as min for finding minimum number, max for maximum number, sqrt for square root, exp for exponential, log for logarithm, std for standard deviation, sin and tan for finding sine and tangent value of given element, argmin and argmax for finding the position of maximum and minimum number, sort for sortening array element in ascending order, mean for finding the mean of the elements, flatten to reduce the n-dimensional array into a single entity, cumsum for finding cummulative summation and so on.For finding the sum of matrix elements you can use either numpy.sum(matrix_name) or matrix_name.sum().
# print(n.linspace(1,-10,5))#Here linspace function is creating such 5 numbers that includes 1 and -10 at beginnig and ending respectively where the difference between each number is equal

# Let us take an array
# az = array([
#     [1,2,3],[4,5,6],[7,8,9]
# ])
# print('The sum of column is ',n.sum(az,axis=0))
# print('The sum of the row is ',n.sum(az,axis=1))
# n.random.seed(122)
# azb = n.array([1,2,3,4,5,2,3,4])
# print(azb)
# print(n.random.shuffle(azb))
# print(n.unique(azb,return_index=True,return_counts=True,return_inverse=True))
# print(n.unique(azb).size)

# Stacking 1D Array
# e1 = n.arange(1,6)
# e2 = n.arange(7,12)
# print('Using hstack ',n.hstack((e1,e2)))#Arranges the matrix horizontally
# print('\nUsing vstack \n',n.vstack((e1,e2)))#Arranges the matrix vertically
# print(n.vstack((e2,e1)))
# print(n.vstack((e1,e1)))

# Stacking 2D Array
# e3 = n.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8]])
# e4 = n.array([[0, 0, 0, 0],
#                 [1, 1, 1, 1]])
# print('This one is horizontal stack\n',n.vstack((e4,e3)))
# print('Well, this one is vertical stack\n',n.vstack((e3,e4)))

# This was everything that I know and found about Numpy. You can share your knowledge if you know more about numpy. If I had made mistakes at any point, feel free to tell me. I will try my best to improve it.