'''
Ham An Danh - Lamdba trong Python
lambda arguments: expression
'''
# A lambda function is a small (one line) anonymous function
# that is defined without a name.

# a lambda function that adds 69 to the input argument

f = lambda x: x+10
def f(x): return x+69
val1 = f(5)
val2 = f(100)


# a lambda function that multiplies two input arguments and returns the result


def f(x, y): return x*y


val3 = f(2, 10)
val4 = f(7, 5)
print(val3, val4)

'''
Custom sorting using a lambda function as key parameter
'''

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key=lambda x: x[1])
print(sorted_by_y)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key=lambda x: abs(x))
print(sorted_by_abs)


'''
Use lambda for map function
'''
# map(func, seq), transforms each element with the function.
a = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2, a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(b)
print(c)

'''
Use lambda for filter function
'''
# filter(func, seq), returns all elements for which func evaluates to True.

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x % 2 == 0), a))

# However, the same can be achieved with list comprehension
c = [x for x in a if x % 2 == 0]
print(b)
print(c)

'''
Use lambda for reduce function
'''
# reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.
from functools import reduce


# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 
  
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
