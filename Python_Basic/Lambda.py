#lambda arguments : expression
add10 = lambda x: x + 10#assign a lambda expression to the variable add10
print(add10(5))#use the lambda expression with add10(),input numbers in ()

def add10_func(x):
    return x + 10
#add10 and add10_func do the same thing and add10 with lambda function is shorter in one line

#lambda for sort
point2D = [(1,2),(15,1),(5,-1),(10,4)]
point2D_sorted = sorted(point2D)
point2D_sorted_lambda = sorted(point2D, key = lambda x:x[1])#sorted by the second element.(x,y),by y

print(point2D)
print(point2D_sorted)
print(point2D_sorted_lambda)

def sort_by_y(x):
    return x[1]

point2D_sorted_func = sorted(point2D, key=sort_by_y)
print(point2D_sorted_lambda)

#lambda for map
a = [1,2,3,4,5]
b = map(lambda x : x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)#c and b do the same thing

#lambda for filter
filter_a = [1,2,3,4,5,6]
filter_b = filter(lambda x: x%2 ==0,filter_a)
print(list(filter_b))

filter_c = [x for x in a if x%2 ==0]
print(c)

#lambda for product
from functools import reduce
product_a = [1,2,3,4,5,6]

reduce_a = reduce(lambda x,y: x*y,product_a)
print(reduce_a)