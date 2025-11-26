#Tuple: ordered, immutable, allows duplicate elements
my_tuple = "MAX",28,"Boston","Boston"#allows different data types,()is optional,turple = is the same as turple = ()
print(my_tuple)#('MAX', 28, 'Boston')

MAX =("MAX")#This is a string, not recognized as a tuple
print(type(MAX))#<class 'str'>
MAXtotuple =("MAX",)#This is a tuple with one element
print(type(MAXtotuple))#<class 'tuple'>

my_tuple_from_list = tuple(["MAX",28,"Boston"])#convert list to tuple
print(my_tuple_from_list)#('MAX', 28, 'Boston')

item = my_tuple[0]#accessing tuple elements by index,the index usage is the same as lists
print(item)#MAX

#my_tuple[0] = "John"#tuples are immutable, this will raise an error

for i in my_tuple:#iterating through a tuple
    print(i)

if "MAX" in my_tuple:#check if an element exists in a tuple
    print("YES")
else:
    print("NO")

print(len(my_tuple))#3,check the length of a tuple

print(my_tuple.count("MAX"))#1,count occurrences of an element in a tuple
print(my_tuple.count("Boston"))#2

print(my_tuple.index(28))#1,find the index of an element in a tuple

my_list = list(my_tuple)#convert tuple to list
print(my_list)#['MAX', 28, 'Boston', 'Boston']

my_tuple2 = tuple(my_list)#convert list back to tuple
print(my_tuple2)#('MAX', 28, 'Boston', 'Boston')

numbers = (1,2,3,4,5,6,7,8,9,10)

a = numbers[2:5]#slicing a tuple, similar to lists
print(a)#(3, 4, 5)

name ,age, city = my_tuple#unpacking a tuple into variables, the number of variables must match the number of elements in the tuple
print(name)#MAX
print(age)#28
print(city)#Boston
#Note: Since there are two "Boston" in the tuple, only the first one is assigned to city variable,the same element is assigned to only one variable.

numbersto_unpack = (1,2,3,4,5)
i1 ,*i2, i3 = numbersto_unpack#using * to unpack remaining elements into a list
print(i1)#1
print(i2)#[2, 3, 4]
print(i3)#5

import sys
print(sys.getsizeof(my_tuple))#check the memory size of the tuple
print(sys.getsizeof(my_list))#check the memory size of the list
#Tuples generally use less memory than lists, making them more memory efficient for storing data that does not need to be modified.

import timeit
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
list_time = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
print(f"Tuple creation time: {tuple_time}")
print(f"List creation time: {list_time}")
#Tuples are generally faster than lists for certain operations, such as iteration and access, due to their immutability.
